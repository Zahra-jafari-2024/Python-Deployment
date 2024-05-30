import os
import requests

username = input("Please enter your username:")
url = "https://api.github.com/users/"+username
response = requests.get(url)
data = response.json()
followers = data['followers']
following = data['following']
print(f'user={username}')
print(f'followers={followers}')
print(f'followers={following}')
