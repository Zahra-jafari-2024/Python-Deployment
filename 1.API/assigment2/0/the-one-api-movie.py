import requests
import json
import os
import dotenv

dot=dotenv.load_dotenv()
one_api_key =os.getenv("one_api_key")
url="https://the-one-api.dev/v2/movie"

h={
   "Authorization": one_api_key
}
response=requests.get(url, headers=h)
print(response.status_code)
json.loads(response.text)
print(response.json())

