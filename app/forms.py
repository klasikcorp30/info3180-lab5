from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class AddProfile(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField('Gender',choices=[('Male', 'Male'), ('Female', 'Female')],validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField ('Biography', validators=[InputRequired()])
    image = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'],'Only images allowed!')])


