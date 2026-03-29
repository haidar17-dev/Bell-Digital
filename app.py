from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="templates", static_folder="static")
socketio = SocketIO(app)


@app.route("/")
def index():
    return redirect(url_for('app_run'))

@app.route("/home")
def app_run():
    return render_template('home.html')

@app.route("/sender")
def sender():
    return render_template("sender.html")

@app.route("/receiver")
def receiver():
    return render_template("receiver.html")

@socketio.on("connect")
def handle_connect():
    print("Client terhubung")

@socketio.on("bell")
def handle_bell():
    print("BEL DITEKAN")
    socketio.emit("bell")

if __name__ == "__main__":
    socketio.run(app, debug=True,host="0.0.0.0", port=5001)
