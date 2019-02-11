
from flask import Flask, render_template, request
import os
import record
from record import *

app = Flask(__name__)
app.debug = False

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        name = request.form["record"]
        r = Record()
        r.recording("test1.wav")
        r.calc_mfcc("test1.png")
    else:
        name = "no name."
    return render_template("test.html",name=name)

@app.route("/record", methods=["GET","POST"])
def get():
    if request.method == "POST":
        instance = Record()
        instance.record("test.wav")
        instance.calc_mfcc("test1,png")
        return render_template("test")
#        instance = Record()
#        instance.record("test.wav")

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(port = port)

