import requests
import json
url = 'https://api.github.com/users/Sig42/repos'
resp = requests.get(url)
json_resp = resp.json()
repos = [i['name'] for i in json_resp]
print(repos)
