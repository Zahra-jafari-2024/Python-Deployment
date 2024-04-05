import requests
import json
import dotenv
import os

dotenv.load_dotenv()
api_illusion=os.getenv("api_illusion")
url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
    "prompt": "(masterpiece:1.4), (best quality), (detailed), landscape, Rainy forest of northern Canada",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
}
# Status Code 401 - Unauthorized
headers = {
    "Authorization": api_illusion,
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.text)
