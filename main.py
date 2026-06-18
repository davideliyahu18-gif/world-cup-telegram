
import requests
 
BOT_TOKEN ="8648426108:AAHhM-5ioqeiVPYSDfyVcOgfIl2VL1Q9NdI"
CHAT_ID = "@israelmood"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🚀 בדיקת בוט מונדיאל - החיבור עובד!"
}

r = requests.post(url, data=data)
print(r.text)
