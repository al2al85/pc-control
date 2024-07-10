import flask
import socketio
import influxdb
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
sio = socketio.Server()
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

connections = {}

@app.route('/')
def index():
    return 'Serveur Socket.IO est en cours d\'exécution!'

@sio.event
def connect(sid, environ):
    print('Client connecté:', sid)
    connections[sid] = None

@sio.event
def message(sid, data):
    print('Message reçu:', data)
    sio.send(sid, 'Message reçu: ' + data)

@sio.on('identification')
def identification(sid, data):
    connections[sid] = data
    print('Identification:', data)

@sio.on('battery_info')
def battery_info(sid, data):
    print('Battery info:', data)
    data['device_id'] = connections[sid]['id']
    if connections[sid] is not None:
        influxdb.write_battery_data(data)
        print('Client:', connections[sid])


@sio.event
def disconnect(sid):
    print('Client déconnecté:', sid)

def run():
    app.run(host='0.0.0.0', port=5000)
