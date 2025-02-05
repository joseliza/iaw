from flask import Flask, render_template
from agenda import agenda

app = Flask(__name__)

@app.route("/")
def listar():
    return render_template("listar.html", agenda=agenda)

if __name__ == "__main__":
    app.run(debug=True)
