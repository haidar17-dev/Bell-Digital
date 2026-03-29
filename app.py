from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

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

# WAJIB SEPERTI INI:
if __name__ == "__main__":
    app.run(debug=True)