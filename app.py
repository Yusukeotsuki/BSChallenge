import os
from flask import Flask,request,jsonify
from flask import render_template

app = Flask(__name__)



@app.route('/echo', methods=['POST'])
def echo():
    message = request.json.get("result").get("parameters").get("message")
    response = {
        "speech": message + message
    }
    return jsonify(response)

