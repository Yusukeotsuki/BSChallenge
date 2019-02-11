
from flask import Flask, render_template
import os
import record

app = Flask(__name__)
app.debug = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["GET","POST"])
def post():
    if request.method == "POST":
        instance = Record()
        instance.record("test.wav")

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(port = port)

