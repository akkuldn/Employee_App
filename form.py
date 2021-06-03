"""
This Module Contains the Form classes
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class EmployeeForm(FlaskForm):
    "Class for employee form"
    name = StringField('Name',validators=[DataRequired()])
    department = SelectField('Department', choices=["Development","Testing","Customer Support","Marketing"])
    email = StringField('Email',validators=[Email()])
    submit = SubmitField('Submit')



