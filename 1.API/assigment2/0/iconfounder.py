import requests
import dotenv
import os
dotenv.load_dotenv()
api_iconfinder=os.getenv("api_iconfinder")

url = "https://api.iconfinder.com/v4/icons/search"
payload={
       "query":"arrow",
        "count":"10"
}

headers = {
    "accept": "application/json",
    "Authorization":api_iconfinder
}

response = requests.get(url, headers=headers,params=payload)

print(response.text)