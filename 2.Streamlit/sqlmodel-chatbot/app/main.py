import re
import streamlit as st
import streamlit_authenticator as stauth
from database import insert_user, get_users, get_user_id,insert_message,show
import os
import dotenv
from models import Message,User
import json
import requests
import psycopg2



env = dotenv.load_dotenv()

api_key=os.getenv("API_KEY")

def main():
    st.sidebar.title(":green[ChatBot-streamlit]")
    try:
        
        users = get_users()
        usernames = []
        emails = []
        passwords = []

        for user in users:
            usernames.append(user.username)
            emails.append(user.email)
            passwords.append(user.password)

        credentials = {"usernames": {}}

        for index in range(len(emails)):
            credentials["usernames"][usernames[index]] = {"name": emails[index], "password": passwords[index]}
        
        authenticator = stauth.Authenticate(credentials, cookie_name="chatbot", cookie_key="abcdef", cookie_expiry_days=7)
        email, st.session_state["authentication_status"], username = authenticator.login(fields={'Form name':':blue[Login]','Login':':green[Login]'},location="main")

        if not st.session_state["authentication_status"]:
            sign_up()

        if username:
            if username in usernames:
                if st.session_state["authentication_status"]:
                    with st.sidebar:
                        st.sidebar.subheader(f":blue[Welcome {username}]")
                        authenticator.logout(button_name=":green[Logout]")
                         
                    user_id = get_user_id(username)
                    ai_assistant(user_id)

                elif not st.session_state["authentication_status"]:
                    st.error("Incorrect Username or Password")
            else: st.warning("Username Does Not Exist, Please Sign Up")

    except:
        st.info("Refresh Page")


def sign_up():
    with st.form(key="register", clear_on_submit=True):
        st.subheader(":blue[Sign Up]")
        name = st.text_input("Name")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Repeat Password", type="password")
        btn_register = st.form_submit_button(":green[Sign Up]")
        insert_user(name=name, username=username, email=email, password=password)


def get_edenai_response(prompt: str) -> str:


    headers = {"Authorization": api_key}
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": prompt,
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": "OpenAI - gpt-3.5-turbo, OpenAI - gpt-3.5-turbo-1106, OpenAI ,  OpenAI - gpt-3.5-turbo-0301"
    }
    response = requests.post(url,json=payload, headers=headers)
    result = json.loads(response.text)
    generated_text = result['openai']['generated_text']
    print(result)
    
    if response.status_code == 200:
        return generated_text
    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        print(error_message)
        return "Error: Unable to fetch response from Eden AI"


def process(user_message, user_id):
    ai_message = get_edenai_response(user_message)
    # add messages to database
    insert_message(type_message="user", text_message=user_message, user_id=user_id)
    insert_message(type_message="ai", text_message=ai_message, user_id=user_id)
    # add messages to list
    st.session_state.messages.append(Message(type="user", text=user_message, user_id=user_id))
    st.session_state.messages.append(Message(type="ai", text=ai_message, user_id=user_id))
    return ai_message


def ai_assistant(user_id):
    st.session_state.messages = show(user_id)

    for message in st.session_state.messages:
        with st.chat_message(message.type):
            st.markdown(message.text) 

    if user_text_message := st.chat_input("Send a message..."):
        with st.chat_message("user"):
            st.markdown(user_text_message)

        with st.spinner("please Wait..."):
            ai_message = process(user_text_message, user_id)
        with st.chat_message("ai"):
            st.markdown(ai_message)


if __name__ == "__main__":
      main()