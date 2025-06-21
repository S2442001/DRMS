from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField,TextAreaField,IntegerField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    name=StringField('name', validators=[DataRequired()])
    email=EmailField('email', validators=[DataRequired(), Email()])
    password=PasswordField('password', validators=[DataRequired()])
    submit=SubmitField('Submit')


class LoginForm(FlaskForm):
    email=EmailField('email', validators=[DataRequired(), Email()])
    password=PasswordField('password', validators=[DataRequired()])
    submit=SubmitField('Submit')

class CreateSOS(FlaskForm):
    location=StringField('location', validators=[DataRequired()])
    description=TextAreaField('description', validators=[DataRequired()])
    submit=SubmitField('Submit')

class ManageResource(FlaskForm):
    type=StringField('type of resource (food/water/medicine etc)', validators=[DataRequired()])
    location=StringField('location', validators=[DataRequired()])
    quantity=IntegerField('quantity', validators=[DataRequired()])
    submit=SubmitField('Submit')

class ShelterForm(FlaskForm):
    name=StringField('name', validators=[DataRequired()])
    capacity=IntegerField('capacity',validators=[DataRequired()])
    available_beds=IntegerField('available_beds', validators=[DataRequired()])
    location=StringField('location', validators=[DataRequired()])
    submit=SubmitField('Submit')