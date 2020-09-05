from flask import Flask, current_app, url_for, redirect

# import demo

# 创建flask的应用对象
# __name__表示当前模块名字
#           模块名,flask以这个模块所在的目录为总目录 默认static为静态目录 templates为模板目录
# app = Flask(__name__)

# http://127.0.0.1:5000/static/index.html    http://127.0.0.1:5000/python/index.html   对应static下的静态资源  可以访问静态资源
app = Flask(__name__, static_url_path="/static",  # 访问静态资源的前缀
            static_folder="static",
            # 相对路径static 当前模块所在的静态文件目录  也可以写绝对路径/Users/wjj/PycharmProjects/code/static   默认就是static
            template_folder="templates"  # 模板文件目录
            )


# app = Flask("abc") abc 是一个标准库
# app = Flask("abcdefg")

# 配置参数的使用方式
# 1. 从系统变量中加载
# app.config.from_envvar()  # 从操作系统中取参数
# 2. 使用配置文件
# app.config.from_pyfile("config.cfg")  # 从配置文件中一次性读取

# 3. 使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = "python"


# app.config.from_object(Config)


# 4.直接操作app.config
# app.config['DEBUG'] = True

# flask 1.0.2 不能使用config加上'DEBUG'=True 开启debug模式

@app.route('/')
@app.route('/default')
def hello_world():
    # i = 1 / 0
    print(app.config.get('ITCAST'))
    # 通过current_app   也能取到值
    print(current_app.config.get('ITCAST'))
    return 'Hello World!'


# @app.route("/post_only", methods=["POST"])
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"


@app.route("/hello", methods=["POST"])
def hello1():
    return "hello 1"


@app.route("/hello", methods=["GET"])
def hello2():
    return "hello 2"


@app.route("/login")
def login():
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    # 函数反推
    url = url_for("hello_world")
    print(url)
    return redirect(url)


if __name__ == '__main__':
    # 查看整个flask中的路由信息
    print(app.url_map)
    # app.run()
    # app.run(host="192.168.2.1", port=8080)
    # 5.直接设置app
    # app.debug = True
    # 6.启动项里面那选择
    # app.run(host="192.168.199.195", port=8080, debug=True)
    app.run(host="127.0.0.1", port=8080, debug=True)
