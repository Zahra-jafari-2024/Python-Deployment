import requests
import dotenv
import os

dotenv.load_dotenv()
api_getclip=os.getenv("api_getclip")

url = "https://api.d-id.com/clips/clp_8ffYJrStUgxDuoP-mKAm5"

headers = {
    "accept": "application/json",
    "Authorization": api_getclip
}

response = requests.get(url, headers=headers)

print(response.text)