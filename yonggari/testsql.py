from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config['SQLALCHEMY_CATABASE_URL'] = 'mysql://CapsinFirst:capsinfirst@capsinfirst.ckzc9c4vvmcm.eu-central-1.rds.amazonaws.com/CapsinFirst'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@application.route('/hello')
def hello_world():
    return 'Hello World'

@application.route("/")
def hello():
    guest = User(username='guest', email='guest@example.com')
    db.create_all()
    user = User.query.all()
    return "hello world! {user.username}"

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True)
