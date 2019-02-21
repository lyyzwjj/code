# coding:utf-8

from flask import Flask

# 推迟一方导入
from _19_users import register
from _20_goods import get_goods
from _21_orders import app_orders
from cart import app_cart

app = Flask(__name__)

app.route("/get_goods")(get_goods)
app.route("/register")(register)
# 注册蓝图
# app.register_blueprint(app_orders)
# 加上前缀
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route('/')
def index():
    # from _19_users import register
    # from _20_goods import get_goods
    return "index page"


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
