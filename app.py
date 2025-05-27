from flask import Flask, request
import requests

app = Flask(__name__)

VK_TEAMS_BOT_TOKEN = '001.3178612650.2918330597:1011985736'
CHAT_ID = 'https://myteam.mail.ru/profile/AoLN6eB3tUZsMMI21hs'

def send_to_vk_teams(message):
    url = f'https://bots.vkteam.dev/messages/sendText'
    headers = {
        'Authorization': f'Bearer {VK_TEAMS_BOT_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, headers=headers, json=payload)

@app.route('/send', methods=['POST'])
def receive_webhook():
    data = request.json
    try:
        lead = data['leads']['add'][0]
        message = f"🆕 Новая сделка: {lead['name']} на сумму {lead['price']} руб."
        send_to_vk_teams(message)
        return 'OK', 200
    except Exception as e:
        return f'Ошибка: {e}', 500

if __name__ == '__main__':
    app.run()
#добавил app.ру
