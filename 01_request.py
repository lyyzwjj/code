# coding:utf-8
from flask import Flask, request

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有请求信息
    # request.form可以直接提取请求体中的表单格式的数据,是一个类字典的对象
    name = request.form.get("name")
    age = request.form.get("age")
    return "name =  %s , age = %s" % (name, age)


if __name__ == '__main__':
    app.run(debug=True)
