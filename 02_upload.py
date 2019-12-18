# coding:utf-8
from flask import Flask, request

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    """接手前端穿过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        # 未上传文件
        return "未上传文件"
    """
    # 1. 创建一个文件
    f = open("./demo.jpg", "wb")
    # 2. 向文件写内容
    data = file_obj.read()
    f.write(data)
    # 3. 关闭文件
    f.close()
    """
    # 直接使用上传对象保存
    file_obj.save("./demo.jpg")
    return "上传成功"


if __name__ == '__main__':
    app.run(debug=True)
