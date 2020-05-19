import time
import os
import requests

from twilio.rest import Client
from dotenv import load_dotenv


def get_status(user_id):
    load_dotenv()
    params = {
        'user_ids':user_id,
        'v':5.92,
        'access_token':os.getenv("access_token"),
        'fields':'online'
    }
    url = 'https://api.vk.com/method/users.get'
    status = requests.post(url=url, params=params)
    return status.json()["response"][0]['online'] 


def sms_sender(sms_text):
    load_dotenv()
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("token")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=sms_text,
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO')
        )

    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
