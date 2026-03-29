from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")
import pusher

pusher_client = pusher.Pusher(
    app_id = "2134043",
    key = "bcf0f5714b9e9a5b86d1",
    secret = "2aa54de5497b0a0857a6",
    cluster = "ap1",
    ssl=True
)

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

@app.route("/push-bell", methods=["POST"])
def push_bell():
    pusher_client.trigger('bell-channel', 'bell-event', {'message': 'BEL DITEKAN'})
    return jsonify({"status": "success"})
    
if __name__ == "__main__":
    app.run(debug=True)