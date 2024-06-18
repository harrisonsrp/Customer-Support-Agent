#Flask lib
from flask import flash

#Auth lib
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

#Database
from User import Users
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
        new_user = Users.create(username=form.username.data, email=form.email.data, password=hashed_password)
        flash('Your account has been created!', 'success')
        
    def login(form):
        user_data = Users.read(form.email.data)  # Assuming `read()` expects plain email
        if user_data and check_password_hash(user_data.password, form.password.data):
            user = User(id=user_data.id, username=user_data.username, email=user_data.email, password=user_data.password)
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