# coding:utf-8

from _18_main import app


@app.route('/get_goods')
def get_goods():
    return "get_goods page"
