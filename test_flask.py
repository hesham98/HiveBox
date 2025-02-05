"""First helloWorld module for testing flask you can rung it using flask --app test_flask run"""
from flask import Flask
app = Flask(__name__)

"""this tells how you can reach the website, and you can reach it on http://127.0.0.1:5000/test"""
@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"
