
from flask import Flask, render_template, request, make_response
import os
import record
from record import *
from label_image import *
import json


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/result")
def result():
    return render_template("result.html")
@app.route("/start", methods=["GET", "POST"])
def start():
    r = Record()
    r.recording("test2.wav")
    r.calc_mfcc("test1.png")
    labels, values = prediction()
    values = [str(v) for v in values]
    result = dict(zip(labels, values))

    return make_response(json.dumps(result))

@app.route("/test", methods=["GET", "POST"])
def test():
    r = Record()
    r.recording("test1.wav")
    r.calc_mfcc("test1.png")
    hoge()
    return render_template("test.html")

@app.route("/record", methods=["GET","POST"])
def record():
    return render_template("record.html")

@app.route("/menu", methods=["GET","POST"])
def get():
#    if request.method == "POST":
#        instance = Record()
#        instance.record("test.wav")
#        instance.calc_mfcc("test1,png")
#        print("you are here")
#        hoge()
#        print("you passed the exam")
#        return render_template("test")
#        instance = Record()
#        instance.record("test.wav")

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(port = port)

