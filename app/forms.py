from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    last_name = StringField('Last Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    address = PasswordField('Address 1', validators=[DataRequired()])
    city = PasswordField('City', validators=[DataRequired()])
    state = PasswordField('State', validators=[DataRequired()])
    zip_code = PasswordField('Zip Code', validators=[DataRequired()])
    submit = SubmitField()

