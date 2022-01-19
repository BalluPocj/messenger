import requests
from time import *


host = 'http://127.0.0.1:1060'
url = '/get_messages'
after = 0


def print_message(message):
    time_local = localtime(message['timestamp'])
    time_str = strftime('%H:%M:%S', time_local)
    date_str = strftime('%d.%m.%Y', time_local)
    print(message['username'], f'{time_str} {date_str}')
    print('Сообщение:', message['text'])


while True:
    response = requests.get(host+url)

    messages = response.json()['messages']
    for message in messages:
        if message['timestamp'] > after:
            print_message(message)
    after = message['timestamp']
    sleep(1)
