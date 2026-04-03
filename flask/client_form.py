from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired

class ClientForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    membership = IntegerField("Membership", validators=[DataRequired()])
    save = SubmitField("Save")