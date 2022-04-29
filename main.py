from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import true


app = Flask(__name__)
app.secret_key = "Ofort"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = request.form['name']
        second_name = request.form['second_name']
        age = request.form['age']
        school = request.form['school']
        curs = request.form['curs']
        gender = request.form['gender']
        session["user"] = name+second_name
        if (curs == "1" or curs == "2"):
            return redirect(url_for('infantil_primaria'))
        elif (curs == "3" or curs == "4"):
            return redirect(url_for('secundaria_bat'))
        else:
            return render_template("index.html")
    return render_template("index.html")

@app.route("/infantil_primaria", methods=["GET", "POST"])
def infantil_primaria():
    if "user" in session:
        user = session["user"]
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
    if "user" in session:
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

if __name__ == "__main__":
    app.run(debug=true)