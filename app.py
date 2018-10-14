import os
from flask import Flask,request,jsonify
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return u"test"

@app.route("/hello/<name>")
def hello(name=""):
    if name == "":
        name = u"anonimous"
    return render_template("hello.html",name=name)

@app.route("/debug")
def debug():
    return render_template("notemplate.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(port=port)


