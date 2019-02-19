# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:Wzzst310@163.com@129.204.35.106:3306/author_book_py"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "wzzst310"


app.config.from_object(Config)
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

# 创建flask脚本管理工具对象
manager = Manager(app)

# 创建数据库迁移工具对象
Migrate(app, db)

# 向manager对象中添加数据库的操作命令
manager.add_command("db", MigrateCommand)


class Author(db.Model):
    __tablename__ = "tbl_authors"  # 指明数据库的表名
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键,会默认设置自增主键
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64), unique=True)
    books = db.relationship("Book", backref="author")
    addr = db.Column(db.String(64))
    mobile = db.Column(db.String(64))


class Book(db.Model):
    __tablename__ = "tbl_books"  # 指明数据库的表名
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键,会默认设置自增主键
    info = db.Column(db.String(64), unique=True)
    lead = db.Column(db.String(32))
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


class AuthorBookForm(FlaskForm):
    author_name = StringField(label=u"作者", id=u"author_name", validators=[DataRequired(u"作者必填")])
    book_info = StringField(label=u"书籍", id=u"book_info", validators=[DataRequired(u"书籍必填")])
    submit = SubmitField(label=u"保存")


@app.route("/", methods=["GET", "POST"])
def index():
    form = AuthorBookForm()
    if form.validate_on_submit():
        # 验证表单成功
        author_name = form.author_name.data
        book_info = form.book_info.data
        # 保存数据库
        print(author_name)
        print(book_info)
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        # book = Book(info=book_info, author_id=author.id)
        book = Book(info=book_info, author=author)
        db.session.add(book)
        db.session.commit()
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)


@app.route("/delete_book", methods=["POST"])
def delete_book():
    # 提取参数
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")
    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    # return redirect(url_for("index"))
    return jsonify(code=0, message="OK")


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # # 生成数据
    # au_xi = Author(name='我吃西红柿', email='xihongshi@163.com')
    # au_qian = Author(name='萧潜', email='xiaoqian@126.com')
    # au_san = Author(name='唐家三少', email='sanshao@163.com')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    # bk_xi = Book(info='吞噬星空', lead='罗峰', author_id=au_xi.id)
    # bk_xi2 = Book(info='寸芒', lead='李杨', author_id=au_xi.id)
    # bk_qian = Book(info='飘渺之旅', lead='李强', author_id=au_qian.id)
    # bk_san = Book(info='冰火魔厨', lead='融念冰', author_id=au_san.id)
    # # 把数据提交给用户会话
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # # 提交会话
    # db.session.commit()
    # app.run(debug=True)
    manager.run()
    # python _16_author_book.py db init 初始化生成migrations文件夹
    # python _16_author_book.py db migrate 生成迁移文件
    # python _16_author_book.py db migrate -m "Author添加手机字段" 生成迁移文件
    # python _16_author_book.py db upgrade 执行
    # python _16_author_book.py db history 查看历史记录
    # python _16_author_book.py db downgrade 161093c18654 回退版本
