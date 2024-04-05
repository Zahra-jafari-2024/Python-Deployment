import json
import requests
import dotenv
import os
import urllib.request
import argparse
def plan(self):
    api_key = os.getenv("api_key")
    url = "http://my-api.plantnet.org/v2/identify/all"
    payload = {
        "api-key":  api_key
    }
    FILES = {
        "images": open("generated_img.jpg", "rb")
    }
    try:
       response = requests.post(url, params=payload, files=FILES)
       print(response.json()["results"][0]["species"]["genus"]["scientificName"])
    except:
        print(response.status_code)

parser1 = argparse.ArgumentParser()
parser1.add_argument('name', help='enter your favorite flower?')
args = parser1.parse_args()
dotenv.load_dotenv()
api_illusion = os.getenv("api_illusion")
url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png",
    "prompt": "(masterpiece:1.4), (best quality), (detailed), landscape,"+args.name,
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
          }
headers = {
        "Authorization": api_illusion,
        "Content-Type": "application/json"
  }
try:
        response = requests.post(url, json=payload, headers=headers)
        urllib.request.urlretrieve(response.json()["image"]["url"], "generated_img.jpg")
        plan()
except:
        print(response.status_code)












