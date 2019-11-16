from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

##班级
class Grade(db.Model):
    ##班级id
    g_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    ##班级名
    g_name = db.Column(db.String(20),unique=True)
    ##班级创建时间
    g_create_time = db.Column(db.DATETIME,default=datetime.now())
    ##建立一对多的关系
    students = db.relationship('Student',backref='grade')
    ##自定义表名
    __tablename__ = 'grade'

    def __init__(self,g_name):
        self.g_name = g_name

    def save(self):
        db.session.add(self)
        db.session.commit()


##学生
class Student(db.Model):
    ##学生id
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ##学生名
    s_name = db.Column(db.String(20))
    ##学生性别
    s_sex = db.Column(db.Integer)
    ##关联班级
    grade_id = db.Column(db.Integer,db.ForeignKey('grade.g_id'),nullable=True)
    ##自定义表名
    __tablename__ = 'student'

    def __init__(self,s_name,s_sex,grade_id):
        self.s_name = s_name
        self.s_sex = s_sex
        self.grade_id = grade_id

    def save(self):
        db.session.add(self)
        db.session.commit()

##系统用户
class User(db.Model):
    ##用户id
    u_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    ##用户名
    u_name = db.Column(db.String(16),unique=True)
    ##用户密码
    u_password = db.Column(db.String(200))
    ##创建时间
    u_create_time = db.Column(db.DATETIME,default=datetime.now())
    ##用户组
    role_id = db.Column(db.Integer, db.ForeignKey('role.r_id'))
    ##表名
    __tablename__ = 'user'


    def __init__(self,u_name,u_password,role_id):
        self.u_name = u_name
        self.u_password = u_password
        self.role_id = role_id

    def save(self):
        db.session.add(self)
        db.session.commit()

##定义一个r_p表，存储用户组和权限之间多对多的关系
r_p = db.Table('r_p',db.Column('r_id',db.Integer,db.ForeignKey('role.r_id'),primary_key=True),db.Column('p_id',db.Integer,db.ForeignKey('permisstion.p_id'),primary_key=True))

##用户组
class Role(db.Model):
    ##用户组id
    r_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    ##用户组名
    r_name = db.Column(db.String(100),unique=True)
    ##创建时间
    r_create_time = db.Column(db.DATETIME,default=datetime.now())

    users = db.relationship('User',backref='role')

    __tablename__ = 'role'

    def __init__(self,r_name):
        self.r_name = r_name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Permisstion(db.Model):
    ##权限id
    p_id = db.Column(db.Integer,autoincrement=True,primary_key=True)

    p_name = db.Column(db.String(20),unique=True)

    p_er = db.Column(db.String(20),unique=True)

    p_url = db.Column(db.String(20),unique=True)

    p_create_time = db.Column(db.DATETIME,default=datetime.now())

    roles = db.relationship('Role',secondary=r_p,backref=db.backref('permisstion',lazy=True))

    __tablename__ = 'permisstion'

    def __init__(self,p_name,p_er):
        self.p_name = p_name
        self.p_er = p_er


    def save(self):
        db.session.add(self)
        db.session.commit()




