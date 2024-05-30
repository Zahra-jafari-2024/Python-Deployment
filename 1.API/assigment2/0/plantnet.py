import requests
import dotenv
import dotenv
import os

dotenv.load_dotenv()
plnet_key = os.getenv("planet_api")
url="http://my-api.plantnet.org/v2/identify/all"
payload={
    "api-key":plnet_key
}
FILES={
    "images" : open("image/02555.jpg","rb")
}
response=requests.post(url,params=payload,files=FILES)
print(response.status_code)
print(response.text)