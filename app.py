import os
from random import random
from flask import Flask, render_template

PROJECT_DIR = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(PROJECT_DIR, "static", "images")

app = Flask(__name__, template_folder="templates")
app.config["IMAGES"] = IMAGES_FOLDER


@app.route("/")
def hello():
    return render_template('home.html')


def images_file_name(name: str):
    return os.path.join(app.config["IMAGES"], name)


@app.route("/flip")
def coin_flip():
    num = random()

    if num >= 0.5:
        image = images_file_name("heads.jpg")
        return render_template("page_with_image.html", image=image, alt_text="HEADS!")
        # return "HEADS!"

    if num < 0.5:
        image = images_file_name("tails.jpg")
        return render_template("page_with_image.html", image=image, alt_text="TAILS!")
        # return "TAILS!"


if __name__ == "__main__":
    app.run()
