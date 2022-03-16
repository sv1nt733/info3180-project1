from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class createPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    bedrooms = StringField('No. of Rooms', validators=[InputRequired()], default="3")
    bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()], default="2")
    price = StringField('Price', validators=[InputRequired()], default="15,000,000")
    propertyType = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()], default="House")
    location = StringField('Location', validators=[InputRequired()], default="10 Waterloo Rd")
    photo = FileField('Photo', validators = [FileRequired(), FileAllowed(["jpg","png","jpeg"], "Images Only!")])