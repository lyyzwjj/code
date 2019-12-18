# coding:utf-8
from flask import Flask, request, abort, Response, make_response, jsonify
import json

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie
    resp.set_cookie("Itcast", "Python")
    resp.set_cookie("Itcast1", "Python1")
    resp.set_cookie("Itcast2", "Python2", max_age=3600)  # 单位s
    resp.headers["Set-Cookie"] = "Itcast3=Python3; Expires=Tue, 09-Feb-2019 15:09:46 GMT; Max-Age=3600; Path=/"
    return resp


@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Itcast2")
    return c


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    # 删除cookie
    resp.delete_cookie("Itcast1")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
