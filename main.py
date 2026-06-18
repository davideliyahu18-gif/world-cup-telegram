
import requests

BOT_TOKEN = "8648426108:AAHhM-5ioqeiVPYSDfyVcOgfIl2VL1Q9NdI"
CHAT_ID = "@eliyahucup"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "בדיקה"
    }
)

print(r.text)
