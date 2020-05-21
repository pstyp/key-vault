from wtforms import StringField, BooleanField, SubmitField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, NumberRange
from flask_wtf import FlaskForm
from application import bcrypt
from application.models import Users
from flask_login import current_user


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
            ])
    password = PasswordField('Password',
    validators=[
            DataRequired(),
		])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_password(self, password):
        user = Users.query.filter_by(email=self.email.data).first()
        if user:
            if not bcrypt.check_password_hash(user.password, self.password.data):
                raise ValidationError('Incorrect Email or Password')
        else:
            raise ValidationError('Incorrect Email or Password')