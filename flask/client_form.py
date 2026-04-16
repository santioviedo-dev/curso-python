from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    id = HiddenField("id")
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    membership = IntegerField("Membership", validators=[DataRequired()])
    save = SubmitField("Save")