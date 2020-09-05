# coding:utf-8
from flask import Flask
from flask_script import Manager, Server

'''
（1）Flask Script扩展提供向Flask插入外部脚本的功能，包括运行一个开发用的服务器，一个定制的Python shell，设置数据库的脚本，cronjobs，及其他运行在web应用之外的命令行任务；使得脚本和系统分开；
（2）Flask Script和Flask本身的工作方式类似，只需定义和添加从命令行中被Manager实例调用的命令；
（3）flask_script的作用是可以通过命令行的形式来操作flask例如通过一个命令跑一个开发版本的服务器，设置数据库，定时任务等
（4）通过使用Flask-Script扩展，我们可以在Flask服务器启动的时候，通过命令行的方式传入参数。而不仅仅通过app.run()方法中传参，比如我们可以通过python hello.py runserver --host ip地址，告诉服务器在哪个网络接口监听来自客户端的连接。默认情况下，服务器只监听来自服务器所在计算机发起的连接，即localhost连接。
'''
# 实例化Flask对象
app = Flask(__name__)
# app = Flask(__name__, template_folder='templates')

# 创建Manager管理类的对象
# 将Flask实例对象传入Manager
manager = Manager(app)

# 添加Manager实例调用的命令
manager.add_command("runserver", Server("localhost", port=8080))


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    # 通过管理对象启动flask
    manager.run()
