#Flask lib
from flask import flash, redirect, url_for,render_template

#Auth lib
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

#Database
from Database import collection_users

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class User(UserMixin):
    
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        
    def register(form):
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = {
        '_id': collection_users.count_documents({}) + 1,
        'username': form.username.data,
        'email': form.email.data,
        'password': hashed_password
        }
        collection_users.insert_one(new_user)
        flash('Your account has been created!', 'success')
        
    def login(form):
        user_data = collection_users.find_one({'email': form.email.data})
        if user_data and check_password_hash(user_data['password'], form.password.data):
            user = User(id=user_data['_id'], username=user_data['username'], email=user_data['email'], password=user_data['password'])
            login_user(user)
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    def logout():
        logout_user()
        
    def home():
        pass

class Admin:
    
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        
    def register():
        pass
    
    def login():
        pass
    
    def logout():
        pass
    
    def home():
        pass