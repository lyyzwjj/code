# coding:utf-8

from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config["SECRET_KEY"] = "WZZST310"


# 定义表单模型类
class RegisterForm(FlaskForm):
    #                       名字             验证器
    # DataRequired 保证数据必须填写, 并且不能为空
    user_name = StringField(label=u"用户名", validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField(label=u"密码", validators=[DataRequired(u"密码不能为空")])
    password2 = PasswordField(label=u"确认密码", validators=[DataRequired(u"确认密码不能为空"), EqualTo("password", u"两次密码不一致")])
    submit = SubmitField(label=u"提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    # 创建表单对象
    form = RegisterForm()
    # 判断form中数据是否合理
    # 如果form中的数据完成满足所有的验证器,则返回为真,否则返回为假
    if form.validate_on_submit():
        # 表示验证合格
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        session["user_name"] = uname

        return redirect(url_for("register_success_index"))
    return render_template("register.html", form=form)


@app.route("/register_success_index")
def register_success_index():
    user_name = session.get("user_name", "")
    return "register_success_index page %s" % user_name


if __name__ == '__main__':
    app.run(debug=True)
