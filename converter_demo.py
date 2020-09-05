from flask import Flask, current_app, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 转换器语法  int float path
# @app.route("/goods/<int:goods_id>")   # int
@app.route("/goods/<goods_id>")  # 普通字符串 除了"/"
def goods_detail(goods_id):
    return "goods detail page %s" % goods_id


# 1.定义自己的转换器
# 万能转换器
class RegexConverter(BaseConverter):
    """"""

    # 整个app路由映射列表url_map
    # 自定义的regex
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象属性中，flask回去使用这个属性来进行路由的正则匹配
        self.regex = regex

    # 此处的value就是转换器取到的url中的值
    def to_python(self, value):
        return 123

    def to_url(self, value):
        return value


# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter


# 3.使用

# 手机号码转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        # 调用父类的初始化方法
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'

    # 此处的value就是转换器取到的url中的值
    def to_python(self, value):
        print("to_python被调用")
        # return "123"
        return value

    # url_for用到的
    def to_url(self, value):
        # 使用url_for的时候被调用
        print("to_url被调用")
        # return "18984954312"
        return value


app.url_map.converters["mobile"] = MobileConverter


# @app.route("/send/<re(r'1[34578]\d{9}'):mobile>")  # 普通字符串 除了"/"
@app.route("/send/<mobile:mobile>")  # 普通字符串 除了"/"
def send_sms(mobile):
    return "send sms to %s" % mobile


@app.route("/call/<re(r'1[34578]\d{9}'):tel>")
def call_tel(tel):
    pass


@app.route("/index")
def index():
    # 此处mobile的值先传递给to_url 再加进url中
    url = url_for("send_sms", mobile="18984954311")
    return redirect(url)


if __name__ == '__main__':
    # 查看整个flask中的路由信息
    print(app.url_map)
    # app.run()
    # app.run(host="192.168.2.1", port=8080)
    # 5.直接设置app
    # app.debug = True
    # 6.启动项里面那选择
    app.run(host="127.0.0.1", port=8080, debug=True)
