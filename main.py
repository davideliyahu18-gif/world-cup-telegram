
import requests

API_KEY = "d1afcf8ed3852939ef24767220889871"

url = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)

print(response.json())
