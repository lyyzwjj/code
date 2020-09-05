# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:Wzzst310@163.com@129.204.35.106:3306/flask"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键,会默认设置自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        """定义之后,可以让显示对象的时候更直观"""
        return "User object : name=%s" % self.name


class Role(db.Model):
    """用户角色表"""
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 不是数据库真实存在的
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """定义之后,可以让显示对象的时候更直观"""
        return "Role object : name=%s" % self.name


@app.route("/")
def macro():
    return "index page"


if __name__ == '__main__':
    # 清除数据库的所有数据
    db.drop_all()
    # 创建所有的表
    db.create_all()
    role1 = Role(name="admin")
    db.session.add(role1)
    db.session.commit()
    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()
    us1 = User(name="wang", email="wang@163.com", password="123456", role_id=role1.id)
    us2 = User(name="zhang", email="zhang@163.com", password="201512", role_id=role2.id)
    us3 = User(name="chen", email="chen@163.com", password="987654", role_id=role2.id)
    us4 = User(name="zhou", email="zhou@163.com", password="456789", role_id=role1.id)
    # 一次保存多个值
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
    app.run(debug=True)

"""
Role.query.all()
Role.query.first()
Role.query.get(1)
# filter_by
User.query.filter_by(name="wang") # BaseQuery对象
User.query.filter_by(name="wang").first()
User.query.filter_by(name="wang",role_id = 1).first() && 
# filter
User.query.filter(User.name=="wang",User.role_id==1).first() 
User.query.filter(or_(User.name=="wang", User.email.endwith("@163.com")) 
User.query.filter().offset().limit().order_by().all()
offset 跳过几条 偏移
User.query.offset(2).all()
limit
User.query.offset(1).limit(2).all()
order_by
User.query.order_by("-id").all()
官方推荐
User.query.order_by(User.id.desc()).all() 
group_by
分组排序之后出来的结果就不是一个类对象了  分组就不是类对象 需要手动指明要查询的东西
db.session.query(User.role_id).group_by(User.role_id) 
db.session.query(User.role_id,func.count(User.role_id)).group_by(User.role_id).all() 


关联查询
Role找users
ro = Role.query.get(1) 
ro.users[0].name 
User找Role
user = User.query.get(1)  
role = Role.query.get(user.role_id)
若有backref 则可直接使用
user.role.name

改变值
user = User.query.get(1) 
user.name = "python" 
db.session.add(user) 
db.session.commit()
更新  
User.query.filter_by(name="zhou").update({"name":"python1","email":"python@itcast.cn"}) 
db.session.commit()  
删除
user = user.query.get(3)
db.session.delete(user)
db.session.commit()
"""
 