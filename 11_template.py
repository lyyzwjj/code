# coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": 18,
        "my_dict": {"city": "ShangHai"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 0
    }
    # return render_template("index.html", name="python", age="18")
    # **dict 自动解包
    return render_template("index.html", **data)


# 自定义过滤器
# 1. 以函数的方式,再注册
def list_step_2(list):
    # 切片语法
    return list[::2]


# 注册过滤器
app.add_template_filter(list_step_2, "list2")  # 第二个参数是给过滤器取名字 模板中用到的


# 2.使用装饰器
@app.template_filter("list3")
def list_step_3(list):
    # 切片语法
    return list[::3]


if __name__ == '__main__':
    app.run(debug=True)
