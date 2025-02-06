"""import flask from Flask class and app_version function from app_version module"""
from flask import Flask
from app_version import app_version

app = Flask(__name__)

"""this tells how you can reach the website, and you can reach it on http://127.0.0.1:5000/test"""
@app.route("/version")
def get_app_version():
    """call app_version() from app_version module this fuction prints the application version"""
    version = app_version()
    return f"<p>Version: {version}</p>"
