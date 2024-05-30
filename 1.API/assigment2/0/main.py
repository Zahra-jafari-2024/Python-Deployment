import requests


url = "https://the-one-api.dev/v2/book/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

