from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    greeting = "<h1>Hello World!</h1>"
    return render_template("index.html", greeting=greeting)


# def helloWorld():
#     return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run()
