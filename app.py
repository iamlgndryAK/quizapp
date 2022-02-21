from requests import get
from html import unescape
from flask import Flask, render_template, redirect, url_for
from random import choice

parameter = {
    "amount": 10,
    "type": "boolean"
}

data= []


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    global data
    response = get(url="https://opentdb.com/api.php", params=parameter)
    data = response.json()["results"]
    for i in data:
        i["question"] = unescape(i["question"])
    return render_template("index.html", item=choice(data), data=data)


@app.route("/check_true/<int:index>", methods=["GET", "POST"])
def check_true(index):
    global data
    if data[index]["correct_answer"] == "True":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")


@app.route("/check_false/<int:index>", methods=["GET", "POST"])
def check_false(index):
    global data
    if data[index]["correct_answer"] == "False":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")


if __name__ == "__main__":
    app.run(debug=True)
