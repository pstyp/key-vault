from application import app, db, bcrypt, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from application.forms import LoginForm
from application.models import Users
from os import getenv


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            flash('You have logged in!', 'success')
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('home')
    else:
        flash("We couldn't log you in", 'danger')
    return render_template('login.html', title="Home Page", login_form=login_form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))
