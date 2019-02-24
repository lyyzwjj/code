# coding:utf-8
from flask import Flask, request, abort, Response, make_response, jsonify, session, g
import json


app = Flask(__name__)


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)
