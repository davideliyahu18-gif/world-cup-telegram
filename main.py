import os
import requests

API_KEY = os.getenv("API_KEY")

headers = {
    "x-apisports-key": API_KEY
}

r = requests.get(
    "https://v3.football.api-sports.io/status",
    headers=headers
)

print(r.status_code)
print(r.text)
