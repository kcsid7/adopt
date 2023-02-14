from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, BooleanField

class NewPetForm(FlaskForm):
    """ Form to add new pet """
    name = StringField("Pet Name")
    species = StringField("Pet Species")
    photo = StringField("Pet Photo")
    age = IntegerField("Pet Age")
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """ Form to edit pets """
    
    name = StringField("Pet Name")
    species = StringField("Pet Species")
    photo = StringField("Pet Photo")
    notes = StringField("Notes")
    available = SelectField("Available")
