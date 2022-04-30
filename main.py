from flask import Flask, render_template, url_for, request, redirect, session
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
        
        session["id"] = 1
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
        user = session["id"]
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
            return redirect(url_for('end'))
        return render_template("infantil_primaria.html")
    else:
        return redirect(url_for('index'))

@app.route("/secundaria_bat", methods=["GET", "POST"])
def secundaria_bat():
    if "id" in session:
        user = session["id"]
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
            return redirect(url_for('end'))
        return render_template("secundaria_bat.html")
    else:
        return redirect(url_for('index'))

@app.route("/end")
def end():
    return render_template("end.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    return render_template("signin.html")


if __name__ == "__main__":

    # Inicialitza la base de dades
    db = sqlite3.connect('server/dades.db')
    cursor = db.cursor()
    init_bd()

    app.run(debug=true)