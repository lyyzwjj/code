# coding:utf-

from flask import render_template
from . import app_cart


@app_cart.route("/get_cart")
def get_cart():
    # 已总的为主
    return render_template("cart.html")
