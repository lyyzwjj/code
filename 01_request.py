# coding:utf-8
from flask import Flask, request

app = Flask(__name__)


# http://localhost:5000/index?city=changsha  changsha 查询字符串 QueryString
@app.route("/index", methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有请求信息
    # request.form可以直接提取请求体中的表单格式的数据,是一个类字典的对象
    # form 还是data只能从请求体中拿到,如果在url中的就取不出来
    # 如果是form 就已经自动取出来封装到了request.form里面  如果是其他如json xml则在request.data里面(body里面的数据)
    # city = request.form.get("city") url中的取不出来
    # form中的参数统一放到form里面
    # 通过get方法只能拿到多个同名参数的第一个
    name = request.form.get("name")
    age = request.form.get("age")
    # 如果传过来的form有多个同名参数 则可以用getlist取出
    name_li = request.form.getlist("name")
    # 既不是form也不是url 就放在data里面
    print("request.data: %s" % request.data)
    # url中的参数被统一放到args字典里面
    city = request.args.get("city")
    return "name = %s , name_li = %s , age = %s , city = %s " % (name, name_li, age, city)
    # if request.method == "GET":
    #     pass
    # elif request.method == "POST":
    #     pass


if __name__ == '__main__':
    app.run(debug=True)
