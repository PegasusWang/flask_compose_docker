from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


# Database Configurations
app = Flask(__name__)
DATABASE = 'wordpress'
PASSWORD = 'p@ssw0rd123'
USER = 'root'
HOSTNAME = 'mysqlserver'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (
    USER, PASSWORD, HOSTNAME, DATABASE
)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(120), unique=True)
    fax = db.Column(db.String(120), unique=False)

    def __init__(self, username, email, phone, fax):
        self.username = username
        self.email = email
        self.phone = phone
        self.fax = fax

    def __repr__(self):
        return '<User %r>' % self.username


class CreateDB(object):
    def __init__(self, hostname=None):
        if hostname is not None:
            HOSTNAME = hostname
        import sqlalchemy
        mysql_url = 'mysql://%s:%s@%s' % (USER, PASSWORD, HOSTNAME)
        engine = sqlalchemy.create_engine(
            mysql_url
        )  # connect to server
        engine.execute("CREATE DATABASE IF NOT EXISTS %s " % (DATABASE))

if __name__ == '__main__':
    manager.run()
