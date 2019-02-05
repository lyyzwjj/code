# coding:utf-8
from flask import Flask, request, abort, Response, make_response, jsonify, session
import json

session_dict = {
    "1": {

    },
    "2": {

    }
}
app = Flask(__name__)

# flask的session需要用到的密钥字符串
app.config["SECRET_KEY"] = "wzzst310"


# flask 默认把session保存到了cookie中

# 如果浏览器不能保存cookie name就讲cookie 保存在url中

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "wjj"
    session["mobile"] = "18684954312"
    # global session_dict
    # session_dict["1"][] =
    return "login success"


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)
