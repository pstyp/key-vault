from application import db, login_manager, app
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask import url_for, redirect
from flask_admin import Admin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    admin = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
        'Email: ', self.email, '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
        ])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


from flask_admin import AdminIndexView, expose
class MyHomeView(AdminIndexView):

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.admin
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home'))


admin = Admin(app, index_view=MyHomeView())
#admin = Admin(app)

admin.add_view(ModelView(Users, db.session))


'''
class LoginModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.admin
        else:
            return False
'''