# coding:utf-8
from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    # name = request.form.get("name")
    # pwd = request.form.get("pwd")
    name = ""
    pwd = ""
    if name != "wjj" or pwd != "wzzst310":
        # 使用abort可以立即终止视图函数的进行
        # 并可以返回给前端特定的信息
        # 1. 传递状态吗信息,必须是http标准状态码
        abort(404)
        # 2. 传递响应信息
        # resp = Response("login failed")
        # abort(resp)
    else:
        pass
    return "login success"


@app.errorhandler(404)
def handle_404_error(err):
    """自定义处理错误方法"""
    # 这个函数的返回值会是前端前端用户看到的最终结果
    return u"出现了404错误，错误信息： %s" % err


if __name__ == '__main__':
    app.run(debug=True)
