# coding:utf-8
from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    # 1. 使用元组，返回自定义的信息
    #       相应体        状态吗 响应头
    # return "index page", 400, [("Itcast", "python"), ("City", "ShangHai")]
    # return "index page", 666, {"Itcast1": "python1", "City": "ShangHai"}
    # return "index page", "666 itcast status", {"Itcast1": "python1", "City": "ShangHai"}
    # return "index page", "666 itcast status"
    # 2. 使用make——response 来构造响应信息
    resp = make_response("index page 2")
    resp.status = "999 itcast"  # 设置状态吗
    resp.headers["city"] = "ShangHai"
    return resp


if __name__ == '__main__':
    app.run(debug=True)
