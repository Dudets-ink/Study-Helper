from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import user_bp
from .forms import LoginForm, RegisterForm
from ..models import User
from .. import login_manager, db


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@user_bp.route('login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
        
    if request.method == 'POST':
            user = User.query.filter_by(
                username=form.data['username']).first()
            if user:
                if check_password_hash(user.password,
                                       form.data['password']):
                    login_user(user) 
                    flash('You successfully logged in!', 'success')
                    return redirect(url_for('main_page.index'))
            else:
                flash('Wrong username or password...', 'error')
                return redirect(url_for('main_page.index'))
        
    return render_template('login.html', form=form)

@user_bp.route('register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        username = form.data['username']
        password = generate_password_hash(form.data['password']) 
        user = User.query.filter_by(
                username=form.data['username']).first()
        if not user:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            
            flash('You have successfully registered', 'success')
            return redirect(url_for('main_page.index'))
        else:
            flash('Username already taken by someone...', 'error')
            return redirect(url_for('main_page.index'))
        
    return render_template('register.html', form=form)


@user_bp.route('/logout')
def logout():
    flash('You logged out', 'success')
    logout_user()
    return redirect(url_for('main_page.index'))