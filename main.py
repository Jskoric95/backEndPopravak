from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(use_reloader=True)