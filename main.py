from flask import Flask, render_template, url_for, request, redirect, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
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
        if (course == "Infantil" or course == "Primària"):
            return redirect(url_for('infantil_primaria'))
        elif (course == "Secundària" or course == "Batxillerat"):
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
            school = request_school(email, password)
            session["school"] = school
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
        school = request.form['school'].upper()
        gender = request.form['gender']
        role ="Viewer"
        if not find_user(email):
            create_user(email, password, name, second_name, school, gender, role)
            return redirect(url_for('login'))
        flash('EMAIL REGISTRAT PREVIAMENT')
        return redirect(url_for('signin'))
    return render_template("signin.html")

@app.route("/graphics", methods=["GET", "POST"])
def graphics():
    if "email" in session:
        email = session["email"]
        school = session["school"]
        if request.method == 'POST':
            genere = request.form['genere']
            curs = request.form['course']
            min_edat = "3"
            max_edat = "19"
            if (school != "ADMIN"):
                courses = get_school(email)
                pri_tab = ""
                sec_tab = ""
                data_sec = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                data_inf = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0],[0,0,0]]
                if ("Infantil" in courses) or ("Primària" in courses):
                    data_inf = get_data2(school,genere,curs,min_edat,max_edat)
                    pri_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Infantil-Primaria</button>
                </li>"""
                if ("Secundària" in courses) or ("Batxillerat" in courses):
                    data_sec = get_data(school,genere,curs,min_edat,max_edat)
                    sec_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Secundaria-Batxillerat</button>
                </li>"""
                school_select = ""
                admin_tab = ""
            else:
                school_form = request.form['school']
                list_school = list_schools()
                data_sec = get_data(school_form,genere,curs,min_edat,max_edat)
                data_inf = get_data2(school_form,genere,curs,min_edat,max_edat)
                pri_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Infantil-Primaria</button>
                </li>"""
                sec_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Secundaria-Batxillerat</button>
                </li>"""
                school_select = """<div class="form-group col-md-3 mx-0 px-2">
                    <label class="text-dark fw-bold col-12 fs-5" for="school">Escola:</label>
                    <select class="border border-dark rounded" name="school" id="school-select" style="background-color: #A9F0BA; min-width: 100%;">
                """
                admin_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                    <button class="nav-link text-dark border border-dark border-2" id="admin-tab" data-bs-toggle="tab" data-bs-target="#admin" type="button" role="tab" aria-controls="admin" aria-selected="false">Administrar</button>
                </li> """
                options_schools = """<option value="">Totes les escoles</option>\n"""
                for i in list_school:
                    options_schools += "<option value="+i+">"+i+"</option>\n"
                school_select += options_schools
                school_select += """</select>
                </div>"""

            labels = [[1,2,3,4,5],["JOCS DE TAULA","VIDEOJOCS","ESPORTS"],["MATES","ESPORTS","LLENGUA"]]
            return render_template("graphics.html",display_email=email, display_school=school, labels=labels, data_inf=data_inf, data_sec=data_sec,school_select=school_select,admin_tab=admin_tab,pri_tab=pri_tab,sec_tab=sec_tab,sel_school=school_form,sel_course=curs,gender=genere)
        else:
            if (school != "ADMIN"):
                courses = get_school(email)
                pri_tab = ""
                sec_tab = ""
                data_sec = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                data_inf = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0],[0,0,0]]
                if ("Infantil" in courses) or ("Primària" in courses):
                    data_inf = get_data2(school,"","","","")
                    pri_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Infantil-Primaria</button>
                </li>"""
                if ("Secundària" in courses) or ("Batxillerat" in courses):
                    data_sec = get_data(school,"","","","")
                    sec_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Secundaria-Batxillerat</button>
                </li>"""
                school_select = ""
                admin_tab = ""
            else:
                list_school = list_schools()
                data_sec = get_data("","","","","")
                data_inf = get_data2("","","","","")
                pri_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Infantil-Primaria</button>
                </li>"""
                sec_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                <button class="nav-link text-dark border border-dark border-2" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Secundaria-Batxillerat</button>
                </li>"""
                school_select = """<div class="form-group col-md-3 mx-0 px-2">
                    <label class="text-dark fw-bold col-12 fs-5" for="school">Escola:</label>
                    <select class="border border-dark rounded" name="school" id="school-select" style="background-color: #A9F0BA; min-width: 100%;">
                """
                admin_tab = """<li class="nav-item" role="presentation" style="background-color: #A9F0BA;">
                    <button class="nav-link text-dark border border-dark border-2" id="admin-tab" data-bs-toggle="tab" data-bs-target="#admin" type="button" role="tab" aria-controls="admin" aria-selected="false">Administrar</button>
                </li> """
                options_schools = """<option value="">Totes les escoles</option>\n"""
                for i in list_school:
                    options_schools += "<option value="+i+">"+i+"</option>\n"
                school_select += options_schools
                school_select += """</select>
                </div>"""

            labels = [[1,2,3,4,5],["JOCS DE TAULA","VIDEOJOCS","ESPORTS"],["MATES","ESPORTS","LLENGUA"]]
            return render_template("graphics.html",display_email=email, display_school=school, labels=labels, data_inf=data_inf, data_sec=data_sec,school_select=school_select,admin_tab=admin_tab,pri_tab=pri_tab,sec_tab=sec_tab)
    return redirect(url_for('login'))

@app.route("/datatable1", methods=["GET", "POST"])
def datatable1():
    if "email" in session:
        if request.method == 'POST':
            school = session["school"]
            school_var = school
            if school == "ADMIN":
                school_var = ""
            data = create_datatable1(school_var)
            total = get_total_entries1(school_var)

            response = {
                'iTotalRecords': total,
                'iTotalDisplayRecords': total,
                'aaData': data,
            }
            return jsonify(response)
    return redirect(url_for('login'))

@app.route("/datatable2", methods=["GET", "POST"])
def datatable2():
    if "email" in session:
        if request.method == 'POST':
            school = session["school"]
            school_var = school
            if school == "ADMIN":
                school_var = ""
            else:
                school_var = "UPC"
            data = create_datatable2(school_var)
            total = get_total_entries2(school_var)

            response = {
                'iTotalRecords': total,
                'iTotalDisplayRecords': total,
                'aaData': data,
            }
            return jsonify(response)
    return redirect(url_for('login'))

@app.route("/datatable_admin", methods=["GET", "POST"])
def datatable_admin():
    if "email" in session:
        if request.method == 'POST':
            data = create_datatable_admin()
            total = get_total_entries_admin()

            response = {
                'iTotalRecords': total,
                'iTotalDisplayRecords': total,
                'aaData': data,
            }
            return jsonify(response)
    return redirect(url_for('login'))

if __name__ == "__main__":

    # Inicialitza la base de dades
    init_bd()

    app.run(debug=true)