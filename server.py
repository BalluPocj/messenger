from flask import Flask, request
import time

app = Flask(__name__)
owner = "Volodya"
server_start_time = time.time()

messages = [
    {'username': 'Иван М', 'text': 'привет', 'timestamp': time.time()},
    {'username': 'Миша Б', 'text': 'И тебе привет', 'timestamp': time.time()},
    {'username': 'dim-akim', 'text': 'И тебе привет', 'timestamp': time.time()}
]


users = [
    {'username': 'Иван М', 'password': '12345'}
    {'username': 'Миша Б', 'password': '12321'}
    {'username': 'dim-akim', 'password': '54321'}
        ]

@app.route('/')
def hello():
    return "<h1><u>Добро пожаловать в мой уютный мессенджер</u> :) <a target = '_blank' href=/status>Его статус</a></h1>"


@app.route('/status')
def status():
    return {
        'status': 'Ok',
        'name': f'Messanger by {owner}',
        'time': time.ctime(time.time())
    }


@app.route('/get_messages')
def get_messages():
    return {
        'messages': messages
    }


@app.route('/send_messages', methods = ['GET', 'POST'])
def send_messages():
    username = request.json['username']
    text = request.json['text']

    messages.append(
        {
            'username': username,
            'text': text,
            'timestamp': time.time()
        }
    )
    return {
        'ok': True
    }


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['passord']

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                login_ok = True
                break
    return {'ok': login_ok}


if __name__ == '__main__':
    app.run(port=int('1060'), debug=True)
