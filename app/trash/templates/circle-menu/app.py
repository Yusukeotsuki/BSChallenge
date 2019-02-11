
from flask import Flask, render_template
import os


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return "test"

@app.route("/test")
def test():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(port = port)
