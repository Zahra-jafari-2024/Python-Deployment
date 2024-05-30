import requests
import dotenv
import os

dotenv.load_dotenv()
api_id=os.getenv("api_id")

url = "https://api.d-id.com/clips"

payload = {
    "script": {
        "type": "text",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false",
        "input":"happy new your . "
    },
    "config": { "result_format": "mp4" },
    "presenter_config": { "crop": { "type": "rectangle" } },
    "presenter_config": { "crop": { "type": "wide" } },
    "background": { "color": "false" },
    "presenter_id": "anita-6_uTzyZtNR"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": api_id
}
# id=clp_8ffYJrStUgxDuoP-mKAm5
response = requests.post(url, json=payload, headers=headers)

print(response.text)
