from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

# Home route to load the chat page
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event to handle incoming messages
@socketio.on('message')
def handle_message(data):
    print(f"Message from {data['username']}: {data['text']}")
    send(data, broadcast=True)  # Send message to all connected clients

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
