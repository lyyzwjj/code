# coding:utf-8

from flask import Flask
from main._19_users import register
from main._20_goods import get_goods

app = Flask(__name__)

@app.route('/')
def index():
    return "index page"


if __name__ == "__main__":
    print(app.url_map)
    app.run()
