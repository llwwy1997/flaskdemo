from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from App.models import User,Grade,Role,Permisstion
from App.models import db
from utils.functions import create_app

app = create_app()

migrate = Migrate(app,db)

manage = Manager(app=app)

manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()