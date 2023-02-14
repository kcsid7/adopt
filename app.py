from flask import Flask, render_template, redirect, request, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "ita-asdfasd-aasdfaklas"

toolbar = DebugToolbarExtension()

connect_db(app)

def create_db_func():
    with app.app_context():
        db.create_all()


@app.route("/")
def root_route():
    """ Root Route """
    pets = Pet.query.order_by(Pet.id).all()

    return render_template("root.html", pets=pets)


@app.route("/pet/<int:id>")
def pet_route(id):
    """ Individual Pet Route """

    pet = Pet.query.get(id)

    return render_template("pet.html", pet=pet)


@app.route("/pet/add", methods=["GET", "POST"])
def add_new_pet():
    """ Add New Pet """

    form = NewPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo.data,
            age = form.age.data,
            notes = form.notes.data
        )

        db.session.add(new_pet)
        db.session.commit()

        flash(f"New Pet Added!")
        return redirect("/")
    else:
        return render_template("new_pet.html", form=form)


@app.route("/pet/<int:id>/edit", methods=["POST"])
def edit_pet_form(id):

    pet = Pet.query.get(id)
    form = EditPetForm()
    form.available.choices = [ ("Yes", "Yes"), ("No", "No")]

    if form.validate_on_submit():
        print("Hello World!")
        pet.name = form.name.data,
        pet.species = form.species.data,
        pet.photo_url = form.photo.data,
        pet.available = form.available.data,
        pet.notes = form.notes.data

        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} updated!!")
        return redirect("/")


@app.route("/pet/<int:id>/editform")
def get_edit_form(id):
    """ Edit Form Pet """
    pet = Pet.query.get(id)
    form = EditPetForm()
    form.available.choices = [ ("Yes", "Yes"), ("No", "No")]

    form.name.data = pet.name
    form.species.data = pet.species
    form.photo.data = pet.photo_url
    form.available.data = pet.available
    form.notes.data = pet.notes

    return render_template("edit_pet_form.html", form=form, pet=pet)


@app.route("/pet/<int:id>/delete")
def delete_pet(id):
    """ Delete Pet """

    pet = Pet.query.get(id)

    db.session.delete(pet)
    db.session.commit()

    flash(f"{pet.name} removed!")
    return redirect("/")











