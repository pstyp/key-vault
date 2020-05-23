from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from os import getenv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('ADMIN_DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
admin = Admin(app)
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

@app.route('/')
def index():
    return "Hello"

admin.add_view(ModelView(Users, db.session))



if __name__ == '__main__':
    app.run(debug=True)



