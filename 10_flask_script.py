# coding:utf-8
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

# 创建Manager管理类的对象
manager = Manager(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    # 通过管理对象启动flask
    manager.run()
