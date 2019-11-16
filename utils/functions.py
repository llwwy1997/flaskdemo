import os
from flask import Flask
from App.views import user_blueprint
from App.models import db

def create_app():
    ##定义系项目路径变量
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    ##静态文件路径
    STATIC_dir = os.path.join(BASE_DIR,'static')
    ##模板文件路径
    TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
    ##初始化app
    app = Flask(__name__,static_folder=STATIC_dir,template_folder=TEMPLATES_DIR)
    ##注册蓝图
    app.register_blueprint(blueprint=user_blueprint,url_prefix='/user')
    ##mysql连接配置
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lwyayt1997@192.168.226.131:3306/student'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    ##设置session秘钥
    app.config['SECRET_KEY'] = 'secret_key'

    db.init_app(app=app)
    return app

