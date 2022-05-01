from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
from bd import *

from sqlalchemy import true

db = SQLAlchemy()

app = Flask(__name__)

app.secret_key = "Ofort"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server/dades.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = request.form['name']
        second_name = request.form['second_name']
        age = request.form['age']
        school = request.form['school']
        course = request.form['course']
        gender = request.form['gender']
        id = int(last_alumne_id())+1
        insert_alumne(id, name, second_name, age, school, course, gender)
        session["id"] = id
        if (course == "1" or course == "2"):
            return redirect(url_for('infantil_primaria'))
        elif (course == "3" or course == "4"):
            return redirect(url_for('secundaria_bat'))
        else:
            return render_template("index.html")
    return render_template("index.html")

@app.route("/infantil_primaria", methods=["GET", "POST"])
def infantil_primaria():
    if "id" in session:
        id = session["id"]
        if request.method == 'POST':
            question1 = request.form['question1']
            question2 = request.form['question2']
            question3 = request.form['question3']
            question4 = request.form['question4']
            question5 = request.form['question5']
            question6 = request.form['question6']
            question7 = request.form['question7']
            question8 = request.form['question8']
            question9 = request.form['question9']
            question10 = request.form['question10']
            insert_inf_pri(id, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)
            return redirect(url_for('end'))
        return render_template("infantil_primaria.html")
    else:
        return redirect(url_for('index'))

@app.route("/secundaria_bat", methods=["GET", "POST"])
def secundaria_bat():
    if "id" in session:
        id = session["id"]
        if request.method == 'POST':
            question1 = request.form['question1']
            question2 = request.form['question2']
            question3 = request.form['question3']
            question4 = request.form['question4']
            question5 = request.form['question5']
            question6 = request.form['question6']
            question7 = request.form['question7']
            question8 = request.form['question8']
            question9 = request.form['question9']
            question10 = request.form['question10']
            insert_sec_bat(id, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)
            return redirect(url_for('end'))
        return render_template("secundaria_bat.html")
    else:
        return redirect(url_for('index'))

@app.route("/end")
def end():
    return render_template("end.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == "" or password == "":
            return redirect(url_for('login'))
        if request_user(email, password):
            session["email"] = email
            return redirect(url_for('graphics'))
        flash('ERROR INICI DE SESSIÓ')
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        second_name = request.form['second_name']
        school = request.form['school']
        gender = request.form['gender']
        role ="Viewer"
        if not find_user(email):
            create_user(email, password, name, second_name, school, gender, role)
            return redirect(url_for('graphics'))
        flash('EMAIL REGISTRAT PREVIAMENT')
        return redirect(url_for('signin'))
    return render_template("signin.html")

@app.route("/graphics", methods=["GET", "POST"])
def graphics():
    if "email" in session:
        email = session["email"]
        return render_template("graphics.html")
    return redirect(url_for('login'))


if __name__ == "__main__":

    # Inicialitza la base de dades
    init_bd()

    app.run(debug=true)