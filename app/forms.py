from flask_wtf import FlaskForm
from wtforms import IntegerField, validators
from wtforms.validators import InputRequired, DataRequired, NumberRange
class ImageDimension(FlaskForm):
    width = IntegerField('width', validators=[InputRequired(), DataRequired('Should be non-zero integer'), NumberRange(1,4096)])
    height = IntegerField('height', validators=[InputRequired(), DataRequired('Should be non-zero integer'), NumberRange(1,4096)])