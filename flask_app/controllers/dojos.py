from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja


@app.route('/')
def index():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route('/save_dojo', methods = ['POST'])
def create_dojo():
    data = {
        'dname': request.form['dname']
    }
    id = Dojo.save(data)
    return redirect('/')

@app.route('/dojo_ninjas/<int:id>')
def dojo_ninjas(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojo_ninjas(data)
    return render_template('dojo_ninjas.html', one_dojo = dojo)