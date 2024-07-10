import socketio
import system_info
import json
import time

def get_identification():
    with open('client/computer/config.json') as f:
        config_data = json.load(f)
        return config_data.get('identification')

# Créer une instance de Socket.IO Client
sio = socketio.Client()

# Définir des gestionnaires d'événements pour le client
@sio.event
def connect():
    print('Connecté au serveur')
    sio.emit('identification', get_identification())
    while True:
        time.sleep(10)
        sio.emit('battery_info', system_info.get_battery_info())


@sio.event
def message(data):
    print('Réponse du serveur:', data)

@sio.event
def disconnect():
    print('Déconnecté du serveur')

# Se connecter au serveur
with open('client/computer/config.json') as f:
        config_data = json.load(f)
        sio.connect(config_data.get('server_url'))
        sio.wait()
