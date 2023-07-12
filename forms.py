from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class Query(FlaskForm):
    question = StringField("Enter here", validators=[InputRequired(), Length(11, 186, message="Enter a valid question")])
    submit = SubmitField("Submit")
