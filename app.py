from random import random
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/flip")
def coin_flip():
    num = random()

    if num >= 0.5:
        return "HEADS!"

    if num < 0.5:
        return "TAILS!"


if __name__ == "__main__":
    app.run()
