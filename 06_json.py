# coding:utf-8
from flask import Flask, request, abort, Response, make_response, jsonify
import json

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    # json就是字符串
    data = {
        "name": "python",
        "age": 21
    }
    # json.dumps(字典） 将python的字典转换成json字符串
    # json.loads（字符串） 将字符串转换为python中的字典
    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type": "application/json"}
    # jsonify 帮助转换为json数据，并设置响应头{"Content-Type":"application/json"}
    # return jsonify(data)
    # 另一种方式
    return jsonify(city="Shanghai", country="china", age=18)


if __name__ == '__main__':
    app.run(debug=True)
