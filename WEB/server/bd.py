# BD
import sqlite3
import json

def init_bd():

    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    cursor.execute("""PRAGMA foreign_keys = ON""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS ALUMNE(
    ID INT NOT NULL,
    NAME CHAR(20) NOT NULL,
    SECOND_NAME CHAR(20) NOT NULL,
    AGE CHAR(10) NOT NULL,
    SCHOOL CHAR(30) NOT NULL,
    COURSE CHAR(30) NOT NULL,
    GENDER CHAR(30) NOT NULL,
    PRIMARY KEY(ID)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PREGUNTES_INF_PRI(
    ID INT NOT NULL,
    PREGUNTA_1 CHAR(30) NOT NULL,
    PREGUNTA_2 CHAR(30) NOT NULL,
    PREGUNTA_3 CHAR(30) NOT NULL,
    PREGUNTA_4 CHAR(30) NOT NULL,
    PREGUNTA_5 CHAR(30) NOT NULL,
    PREGUNTA_6 CHAR(30) NOT NULL,
    PREGUNTA_7 CHAR(30) NOT NULL,
    PREGUNTA_8 CHAR(30) NOT NULL,
    PREGUNTA_9 CHAR(30) NOT NULL,
    PREGUNTA_10 CHAR(30) NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY (ID) REFERENCES ALUMNE(ID)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PREGUNTES_SEC_BAT(
    ID INT NOT NULL,
    PREGUNTA_1 CHAR(30) NOT NULL,
    PREGUNTA_2 CHAR(30) NOT NULL,
    PREGUNTA_3 CHAR(30) NOT NULL,
    PREGUNTA_4 CHAR(30) NOT NULL,
    PREGUNTA_5 CHAR(30) NOT NULL,
    PREGUNTA_6 CHAR(30) NOT NULL,
    PREGUNTA_7 CHAR(30) NOT NULL,
    PREGUNTA_8 CHAR(30) NOT NULL,
    PREGUNTA_9 CHAR(30) NOT NULL,
    PREGUNTA_10 CHAR(300) NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY (ID) REFERENCES ALUMNE(ID)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS SCHOOLS(
    SCHOOL_ID INT NOT NULL,
    SCHOOL_NAME CHAR(20) NOT NULL,
    PRIMARY KEY(SCHOOL_ID)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS LOGGED_USERS(
    EMAIL CHAR(40) NOT NULL,
    PASSWORD CHAR(40) NOT NULL,
    NAME CHAR(20) NOT NULL,
    SECOND_NAME CHAR(20) NOT NULL,
    SCHOOL CHAR(30) NOT NULL,
    GENDER CHAR(30) NOT NULL,
    ROLE CHAR(30) NOT NULL,
    PRIMARY KEY(EMAIL),
    FOREIGN KEY (SCHOOL) REFERENCES SCHOOLS(SCHOOL_NAME)
    )""")

def insert_alumne(id, name, second_name, age, school, course, gender):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO ALUMNE (ID, NAME, SECOND_NAME, AGE, SCHOOL, COURSE, GENDER) VALUES(?,?,?,?,?,?,?)""", (id, name, second_name, age, school, course, gender))
        db.commit()
    except:
        pass
    return 0

def insert_inf_pri(id, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO PREGUNTES_INF_PRI (ID,PREGUNTA_1,PREGUNTA_2,PREGUNTA_3,PREGUNTA_4,PREGUNTA_5,PREGUNTA_6,PREGUNTA_7,PREGUNTA_8,PREGUNTA_9,PREGUNTA_10) VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (id, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))
        db.commit()
    except:
        pass
    return 0

def insert_sec_bat(id, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO PREGUNTES_SEC_BAT (ID,PREGUNTA_1,PREGUNTA_2,PREGUNTA_3,PREGUNTA_4,PREGUNTA_5,PREGUNTA_6,PREGUNTA_7,PREGUNTA_8,PREGUNTA_9,PREGUNTA_10) VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (id, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))
        db.commit()
    except:
        pass
    return 0

def insert_school(school_name):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO SCHOOLS (SCHOOL_NAME) VALUES(?)""", (school_name))
        db.commit()
    except:
        pass
    return 0

def create_user(email, password, name, second_name, school, gender, role):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO LOGGED_USERS (EMAIL, PASSWORD, NAME, SECOND_NAME, SCHOOL, GENDER, ROLE) VALUES(?,?,?,?,?,?,?)""", (email, password, name, second_name, school, gender, role))
        db.commit()
    except:
        pass
    return 0

def request_user(email, password):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    cursor.execute("""SELECT EMAIL FROM LOGGED_USERS WHERE EMAIL = ? AND PASSWORD = ? """, (email, password))
    for row in cursor:
        if ('{0}'.format(row[0])) == email:
            return True
    return False

def request_school(email, password):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()

    cursor.execute("""SELECT SCHOOL, ROLE FROM LOGGED_USERS WHERE EMAIL = ? AND PASSWORD = ? """, (email, password))
    for row in cursor:
        if ('{0}'.format(row[1])) == "Admin":
            return "ADMIN"
        else:
            return '{0}'.format(row[0])
    return False

def find_user(email):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    cursor.execute("""SELECT EMAIL FROM LOGGED_USERS WHERE EMAIL = ?""", (email,))
    for row in cursor:
        if ('{0}'.format(row[0])) == email:
            return True
    return False

def last_alumne_id():
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    cursor.execute("""SELECT ID FROM ALUMNE ORDER BY ID DESC LIMIT 1""")
    for row in cursor:
        id = '{0}'.format(row[0])
        return id
    return 0

def get_data(school):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    if school == "":
        sql = "SELECT * FROM PREGUNTES_SEC_BAT i WHERE i.ID IN (SELECT ID FROM ALUMNE)"
    else:
        sql = "SELECT * FROM PREGUNTES_SEC_BAT i WHERE i.ID IN (SELECT ID FROM ALUMNE WHERE SCHOOL = '"+school+"')"
    cursor.execute(sql)
    data = []
    chart_1 = [0,0,0,0,0]
    chart_2 = [0,0,0,0,0]
    chart_3 = [0,0,0,0,0]
    chart_4 = [0,0,0,0,0]
    chart_5 = [0,0,0,0,0]
    chart_6 = [0,0,0,0,0]
    chart_7 = [0,0,0,0,0]
    chart_8 = [0,0,0,0,0]
    chart_9 = [0,0,0,0,0]
    for row in cursor:
        pregunta_1 = '{0}'.format(row[1])
        if (pregunta_1 == "1"):
            chart_1[0] += 1
        elif (pregunta_1 == "2"):
            chart_1[1] += 1
        elif (pregunta_1 == "3"):
            chart_1[2] += 1
        elif (pregunta_1 == "4"):
            chart_1[3] += 1
        elif (pregunta_1 == "5"):
            chart_1[4] += 1
        pregunta_2 = '{0}'.format(row[2])
        if (pregunta_2 == "1"):
            chart_2[0] += 1
        elif (pregunta_2 == "2"):
            chart_2[1] += 1
        elif (pregunta_2 == "3"):
            chart_2[2] += 1
        elif (pregunta_2 == "4"):
            chart_2[3] += 1
        elif (pregunta_2 == "5"):
            chart_2[4] += 1
        pregunta_3 = '{0}'.format(row[3])
        if (pregunta_3 == "1"):
            chart_3[0] += 1
        elif (pregunta_3 == "2"):
            chart_3[1] += 1
        elif (pregunta_3 == "3"):
            chart_3[2] += 1
        elif (pregunta_3 == "4"):
            chart_3[3] += 1
        elif (pregunta_3 == "5"):
            chart_3[4] += 1
        pregunta_4 = '{0}'.format(row[4])
        if (pregunta_4 == "1"):
            chart_4[0] += 1
        elif (pregunta_4 == "2"):
            chart_4[1] += 1
        elif (pregunta_4 == "3"):
            chart_4[2] += 1
        elif (pregunta_4 == "4"):
            chart_4[3] += 1
        elif (pregunta_4 == "5"):
            chart_4[4] += 1
        pregunta_5 = '{0}'.format(row[5])
        if (pregunta_5 == "1"):
            chart_5[0] += 1
        elif (pregunta_5 == "2"):
            chart_5[1] += 1
        elif (pregunta_5 == "3"):
            chart_5[2] += 1
        elif (pregunta_5 == "4"):
            chart_5[3] += 1
        elif (pregunta_5 == "5"):
            chart_5[4] += 1
        pregunta_6 = '{0}'.format(row[6])
        if (pregunta_6 == "1"):
            chart_6[0] += 1
        elif (pregunta_6 == "2"):
            chart_6[1] += 1
        elif (pregunta_6 == "3"):
            chart_6[2] += 1
        elif (pregunta_6 == "4"):
            chart_6[3] += 1
        elif (pregunta_6 == "5"):
            chart_6[4] += 1
        pregunta_7 = '{0}'.format(row[7])
        if (pregunta_7 == "1"):
            chart_7[0] += 1
        elif (pregunta_7 == "2"):
            chart_7[1] += 1
        elif (pregunta_7 == "3"):
            chart_7[2] += 1
        elif (pregunta_7 == "4"):
            chart_7[3] += 1
        elif (pregunta_7 == "5"):
            chart_7[4] += 1
        pregunta_8 = '{0}'.format(row[8])
        if (pregunta_8 == "1"):
            chart_8[0] += 1
        elif (pregunta_8 == "2"):
            chart_8[1] += 1
        elif (pregunta_8 == "3"):
            chart_8[2] += 1
        elif (pregunta_8 == "4"):
            chart_8[3] += 1
        elif (pregunta_8 == "5"):
            chart_8[4] += 1
        pregunta_9 = '{0}'.format(row[9])
        if (pregunta_9 == "1"):
            chart_9[0] += 1
        elif (pregunta_9 == "2"):
            chart_9[1] += 1
        elif (pregunta_9 == "3"):
            chart_9[2] += 1
        elif (pregunta_9 == "4"):
            chart_9[3] += 1
        elif (pregunta_9 == "5"):
            chart_9[4] += 1

    data += [chart_1]
    data += [chart_2]
    data += [chart_3]
    data += [chart_4]
    data += [chart_5]
    data += [chart_6]
    data += [chart_7]
    data += [chart_8]
    data += [chart_9]
    return data

def get_data2(school):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    if school == "":
        sql = "SELECT * FROM PREGUNTES_INF_PRI i WHERE i.ID IN (SELECT ID FROM ALUMNE)"
    else:
        sql = "SELECT * FROM PREGUNTES_INF_PRI i WHERE i.ID IN (SELECT ID FROM ALUMNE WHERE SCHOOL = '"+school+"')"
    cursor.execute(sql)
    data = []
    chart_1 = [0,0,0,0,0]
    chart_2 = [0,0,0,0,0]
    chart_3 = [0,0,0,0,0]
    chart_4 = [0,0,0,0,0]
    chart_5 = [0,0,0,0,0]
    chart_6 = [0,0,0,0,0]
    chart_7 = [0,0,0]
    chart_8 = [0,0,0]
    for row in cursor:
        pregunta_1 = '{0}'.format(row[1])
        if (pregunta_1 == "1"):
            chart_1[0] += 1
        elif (pregunta_1 == "2"):
            chart_1[1] += 1
        elif (pregunta_1 == "3"):
            chart_1[2] += 1
        elif (pregunta_1 == "4"):
            chart_1[3] += 1
        elif (pregunta_1 == "5"):
            chart_1[4] += 1
        pregunta_2 = '{0}'.format(row[2])
        if (pregunta_2 == "1"):
            chart_2[0] += 1
        elif (pregunta_2 == "2"):
            chart_2[1] += 1
        elif (pregunta_2 == "3"):
            chart_2[2] += 1
        elif (pregunta_2 == "4"):
            chart_2[3] += 1
        elif (pregunta_2 == "5"):
            chart_2[4] += 1
        pregunta_3 = '{0}'.format(row[3])
        if (pregunta_3 == "1"):
            chart_3[0] += 1
        elif (pregunta_3 == "2"):
            chart_3[1] += 1
        elif (pregunta_3 == "3"):
            chart_3[2] += 1
        elif (pregunta_3 == "4"):
            chart_3[3] += 1
        elif (pregunta_3 == "5"):
            chart_3[4] += 1
        pregunta_4 = '{0}'.format(row[4])
        if (pregunta_4 == "1"):
            chart_4[0] += 1
        elif (pregunta_4 == "2"):
            chart_4[1] += 1
        elif (pregunta_4 == "3"):
            chart_4[2] += 1
        elif (pregunta_4 == "4"):
            chart_4[3] += 1
        elif (pregunta_4 == "5"):
            chart_4[4] += 1
        pregunta_5 = '{0}'.format(row[5])
        if (pregunta_5 == "1"):
            chart_5[0] += 1
        elif (pregunta_5 == "2"):
            chart_5[1] += 1
        elif (pregunta_5 == "3"):
            chart_5[2] += 1
        elif (pregunta_5 == "4"):
            chart_5[3] += 1
        elif (pregunta_5 == "5"):
            chart_5[4] += 1
        pregunta_6 = '{0}'.format(row[6])
        if (pregunta_6 == "1"):
            chart_6[0] += 1
        elif (pregunta_6 == "2"):
            chart_6[1] += 1
        elif (pregunta_6 == "3"):
            chart_6[2] += 1
        elif (pregunta_6 == "4"):
            chart_6[3] += 1
        elif (pregunta_6 == "5"):
            chart_6[4] += 1
        pregunta_7 = '{0}'.format(row[7])
        if (pregunta_7 == "JOCS DE TAULA"):
            chart_7[0] += 1
        elif (pregunta_7 == "VIDEOJOCS"):
            chart_7[1] += 1
        elif (pregunta_7 == "ESPORTS"):
            chart_7[2] += 1
        pregunta_8 = '{0}'.format(row[8])
        if (pregunta_8 == "MATES"):
            chart_8[0] += 1
        elif (pregunta_8 == "ESPORTS"):
            chart_8[1] += 1
        elif (pregunta_8 == "LLENGUA"):
            chart_8[2] += 1

    data += [chart_1]
    data += [chart_2]
    data += [chart_3]
    data += [chart_4]
    data += [chart_5]
    data += [chart_6]
    data += [chart_7]
    data += [chart_8]
    return data

def get_school(email):
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    course = []
    cursor.execute("""SELECT DISTINCT COURSE FROM ALUMNE WHERE SCHOOL = (SELECT SCHOOL FROM LOGGED_USERS WHERE EMAIL = ?)""", (email,))
    for row in cursor:
        data = '{0}'.format(row[0])
        course += [data]
    return course

def list_schools():
    db = sqlite3.connect('dades.db')                                   
    cursor = db.cursor()
    
    schools = []
    cursor.execute("""SELECT DISTINCT SCHOOL FROM ALUMNE""")
    for row in cursor:
        data = '{0}'.format(row[0])
        schools += [data]
    return schools

def create_datatable1(school):
    db = sqlite3.connect('dades.db')
    db.row_factory = sqlite3.Row                                 
    cursor = db.cursor()

    if school == "":
        sql = "SELECT A.ID, NAME, SECOND_NAME, AGE, SCHOOL, COURSE, GENDER, PREGUNTA_1, PREGUNTA_2, PREGUNTA_3, PREGUNTA_4, PREGUNTA_5, PREGUNTA_6, PREGUNTA_7, PREGUNTA_8, PREGUNTA_9, PREGUNTA_10 FROM PREGUNTES_INF_PRI i, ALUMNE a WHERE a.ID = i.ID"
    else:
        sql = "SELECT A.ID, NAME, SECOND_NAME, AGE, SCHOOL, COURSE, GENDER, PREGUNTA_1, PREGUNTA_2, PREGUNTA_3, PREGUNTA_4, PREGUNTA_5, PREGUNTA_6, PREGUNTA_7, PREGUNTA_8, PREGUNTA_9, PREGUNTA_10 FROM PREGUNTES_INF_PRI i, ALUMNE a WHERE a.ID = i.ID AND a.SCHOOL = '"+school+"'"
    cursor.execute(sql)
    data = []
    for row in cursor:
        data.append({
            'name': '{0}'.format(row[1]),
            'second_name': '{0}'.format(row[2]),
            'age': '{0}'.format(row[3]),
            'school':'{0}'.format(row[4]),
            'course': '{0}'.format(row[5]),
            'gender': '{0}'.format(row[6]),
            'pregunta_1': '{0}'.format(row[7]),
            'pregunta_2': '{0}'.format(row[8]),
            'pregunta_3': '{0}'.format(row[9]),
            'pregunta_4': '{0}'.format(row[10]),
            'pregunta_5': '{0}'.format(row[11]),
            'pregunta_6': '{0}'.format(row[12]),
            'pregunta_7': '{0}'.format(row[13]),
            'pregunta_8': '{0}'.format(row[14]),
            'pregunta_9': '{0}'.format(row[15]),
            'pregunta_10': '{0}'.format(row[16]),
        })
    return data

def create_datatable2(school):
    db = sqlite3.connect('dades.db')
    db.row_factory = sqlite3.Row                                 
    cursor = db.cursor()

    if school == "":
        sql = "SELECT A.ID, NAME, SECOND_NAME, AGE, SCHOOL, COURSE, GENDER, PREGUNTA_1, PREGUNTA_2, PREGUNTA_3, PREGUNTA_4, PREGUNTA_5, PREGUNTA_6, PREGUNTA_7, PREGUNTA_8, PREGUNTA_9, PREGUNTA_10 FROM PREGUNTES_SEC_BAT i, ALUMNE a WHERE a.ID = i.ID"
    else:
        sql = "SELECT A.ID, NAME, SECOND_NAME, AGE, SCHOOL, COURSE, GENDER, PREGUNTA_1, PREGUNTA_2, PREGUNTA_3, PREGUNTA_4, PREGUNTA_5, PREGUNTA_6, PREGUNTA_7, PREGUNTA_8, PREGUNTA_9, PREGUNTA_10 FROM PREGUNTES_SEC_BAT i, ALUMNE a WHERE a.ID = i.ID AND a.SCHOOL = '"+school+"'"
    cursor.execute(sql)
    data = []
    for row in cursor:
        data.append({
            'name': '{0}'.format(row[1]),
            'second_name': '{0}'.format(row[2]),
            'age': '{0}'.format(row[3]),
            'school':'{0}'.format(row[4]),
            'course': '{0}'.format(row[5]),
            'gender': '{0}'.format(row[6]),
            'pregunta_1': '{0}'.format(row[7]),
            'pregunta_2': '{0}'.format(row[8]),
            'pregunta_3': '{0}'.format(row[9]),
            'pregunta_4': '{0}'.format(row[10]),
            'pregunta_5': '{0}'.format(row[11]),
            'pregunta_6': '{0}'.format(row[12]),
            'pregunta_7': '{0}'.format(row[13]),
            'pregunta_8': '{0}'.format(row[14]),
            'pregunta_9': '{0}'.format(row[15]),
            'pregunta_10': '{0}'.format(row[16]),
        })
    return data

def create_datatable_admin():
    db = sqlite3.connect('dades.db')
    db.row_factory = sqlite3.Row                                 
    cursor = db.cursor()

    sql = "SELECT EMAIL, NAME, SECOND_NAME, GENDER, SCHOOL, ROLE FROM LOGGED_USERS"
    cursor.execute(sql)
    data = []
    for row in cursor:
        data.append({
            'email': '{0}'.format(row[0]),
            'name': '{0}'.format(row[1]),
            'second_name': '{0}'.format(row[2]),
            'gender': '{0}'.format(row[3]),
            'school':'{0}'.format(row[4]),
            'role': '{0}'.format(row[5]),
            
        })
    return data

def get_total_entries2(school):
    db = sqlite3.connect('dades.db')
    db.row_factory = sqlite3.Row                                 
    cursor = db.cursor()

    if school == "":
        sql = "SELECT count(*) FROM PREGUNTES_SEC_BAT i, ALUMNE a WHERE a.ID = i.ID"
    else:
        sql = "SELECT count(*) FROM PREGUNTES_SEC_BAT i WHERE i.ID IN (SELECT ID FROM ALUMNE WHERE SCHOOL = '"+school+"')"
    cursor.execute(sql)
    for row in cursor:
        return '{0}'.format(row[0])

def get_total_entries1(school):
    db = sqlite3.connect('dades.db')
    db.row_factory = sqlite3.Row                                 
    cursor = db.cursor()

    if school == "":
        sql = "SELECT count(*) FROM PREGUNTES_INF_PRI i, ALUMNE a WHERE a.ID = i.ID"
    else:
        sql = "SELECT count(*) FROM PREGUNTES_INF_PRI i WHERE i.ID IN (SELECT ID FROM ALUMNE WHERE SCHOOL = '"+school+"')"
    cursor.execute(sql)
    for row in cursor:
        return '{0}'.format(row[0])

def get_total_entries_admin():
    db = sqlite3.connect('dades.db')
    db.row_factory = sqlite3.Row                                 
    cursor = db.cursor()

    sql = "SELECT count(*) FROM LOGGED_USERS"
    cursor.execute(sql)
    for row in cursor:
        return '{0}'.format(row[0])