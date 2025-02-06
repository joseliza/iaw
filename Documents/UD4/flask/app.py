from flask import Flask, render_template
from agenda import agenda

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/listar")
def listar():
    return render_template("listar.html", agenda=agenda)
