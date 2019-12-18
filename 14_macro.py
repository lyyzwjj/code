# coding:utf-8

from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

flag = True
app.config["SECRET_KEY"] = "WZZST310"


@app.route("/macro")
def macro():
    global flag
    if flag:
        # 添加闪现信息 闪现信息只能看到一次
        flash("hello1")
        flash("hello2")
        flash("hello3")

        flag = False
    return render_template("macro.html")


if __name__ == '__main__':
    app.run(debug=True)
