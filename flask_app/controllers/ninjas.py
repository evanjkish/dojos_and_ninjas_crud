from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/ninjas/')
def show_ninjas():
    # call the get all classmethod to get all friends
    ninjas = Ninja.get_all()
    return render_template("ninjas.html", ninjas=ninjas, dojos =  Dojo.get_all())

@app.route('/add_ninja')
def add_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    id = Ninja.save(data)
    return redirect(f"/dojo_ninjas/{request.form['dojo_id']}")