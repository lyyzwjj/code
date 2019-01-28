from flask import Flask, current_app

# import demo

# 创建flask的应用对象
# __name__表示当前模块名字
#           模块名,flask以这个模块所在的目录为总目录 默认static为静态目录 templates为模板目录
# app = Flask(__name__)

# http://127.0.0.1:5000/static/index.html    http://127.0.0.1:5000/python/index.html   对应static下的静态资源  可以访问静态资源
app = Flask(__name__, static_url_path="/python",  # 访问静态资源的前缀
            static_folder="static",
            # 相对路径static 当前模块所在的静态文件目录  也可以写绝对路径/Users/wjj/PycharmProjects/code/static   默认就是static
            template_folder="templates"  # 模板文件目录
            )


# app = Flask("abc") abc 是一个标准库
# app = Flask("abcdefg")

# 配置参数的使用方式
# 1. 使用配置文件
# app.config. () # 从操作系统中取参数
# app.config.from_pyfile("config.cfg")  # 从配置文件中一次性读取

# 2. 使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = "python"


app.config.from_object(Config)


# 3.直接操作app.config
# app.config['DEBUG'] = True

# flask 1.0.2 不能使用config加上'DEBUG'=True 开启debug模式

@app.route('/')
def hello_world():
    # i = 1 / 0
    print(app.config.get('ITCAST'))
    # 通过current_app   也能取到值
    print(current_app.config.get('ITCAST'))
    return 'Hello World!'


if __name__ == '__main__':
    # app.run(host="192.168.2.1", port=8080)
    app.run(host="127.0.0.1", port=8080)
