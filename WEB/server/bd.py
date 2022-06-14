# BD
import sqlite3

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
    PREGUNTA_10 CHAR(30) NOT NULL,
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

    