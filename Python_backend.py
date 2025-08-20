# this is a simple python project aimed to impplement my practical knowledge in Backend
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime as date_time

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")   # must match filename

@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return redirect("/thank-you")
    return '''
        <form method="post">
            Name: <input type="text" name="name" required><br>
            Email: <input type="email" name="email" required><br>
            <input type="submit" value="Join">
        </form>
    '''

@app.route("/thank-you")
def thank_you():
    return "Thank you for joining!"




@app.route("/play-video")
def play_video():
    return render_template("video.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port =5000, debug=True)
