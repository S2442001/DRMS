from flask import Blueprint, redirect,render_template, request, flash, url_for
from flask_login import login_user, logout_user, login_required
from app.models import User, db
from app.forms import LoginForm, RegisterForm


auth=Blueprint('auth', __name__)


@auth.route('/')
def home():
      return render_template('index.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form=RegisterForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        pwd=form.password.data

        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return redirect(url_for('auth.register'))
        

        role = 'admin' if User.query.count() == 0 else 'user'
        user=User(name=name, email=email, role=role)
        user.set_password(pwd)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Please log in.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])

def login():
    form=LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        pwd=form.password.data
        user=User.query.filter_by(email=email).first()
        if user and user.check_password(password=pwd):
            login_user(user)
            return redirect(url_for('sos.dashboard' if user.role=='user' else 'admin.admin_dashboard'))
        
        flash('Invalid email or password.')
        return redirect(url_for('auth.login'))
    
    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))