import os
import threading
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from pyscripts.main import *

app = Flask(__name__, static_folder='build/', static_url_path='/')
CORS(app)
app.debug = 'DEBUG' in os.environ
socketio = SocketIO(app, cors_allowed_origins="*")

clients = dict()
clients_location = dict()

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

@socketio.on('connect')
def on_connect():
    socket_id = request.sid
    print(socket_id, "connected!")

@socketio.on('new user')
def handle_new_user(data):
    socket_id = request.sid
    clients[socket_id] = data
    main(clients)
    emit("update", clients, broadcast=True)

@socketio.on('update ping')
def handle_update_ping(data):
    socket_id = request.sid
    clients_location[socket_id] = data
    emit("update", clients_location, broadcast=True)

@socketio.on('disconnect')
def on_disconnect():
    socket_id = request.sid
    if socket_id in clients:
        del clients[socket_id]
    if socket_id in clients_location:
        del clients_location[socket_id]
    main(clients)
    print("disconnected!")

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    socketio.run(app)
