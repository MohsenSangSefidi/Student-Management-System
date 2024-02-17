import sqlite3

def startUp():
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS allAccount(id INTEGER PRIMARY KEY AUTOINCREMENT, userName VARCHAR, password VARCHAR);')
    cursor.execute('CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, userName VARCHAR, fatherName VARCHAR, motherName VARCHAR, adress VARCHAR, phone VARCHAR, email VARCHAR, dateBirth VARCHAR, kindStudent VARCHAR, money VARCHAR, moneyGive VARCHAR);')
    cursor.execute('CREATE TABLE IF NOT EXISTS library(id INTEGER PRIMARY KEY AUTOINCREMENT, userName VARCHAR, bookName VARCHAR, dateBook VARCHAR, timeBook VARCHAR);')

    conection.commit()
    conection.close()

def newAccount(userName, password):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('INSERT INTO allAccount (userName, password) VALUES (?,?);',(userName,password,))

    conection.commit()
    conection.close()

def login(userName):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    data = cursor.execute('SELECT * FROM allAccount WHERE userName = ?;',(userName,))
    try:
        return data.fetchone()[2]
    except:
        return 0


    conection.commit()
    conection.close()

def addStudentInData(userName,fatherName,motherName,adrees,phone,email,date,kindStudent,money,moneyGive):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('INSERT INTO student (userName,fatherName,motherName,adress,phone,email,dateBirth,kindStudent,money,moneyGive) VALUES (?,?,?,?,?,?,?,?,?,?);', (userName,fatherName,motherName,adrees,phone,email,date,kindStudent,money,moneyGive,))

    conection.commit()
    conection.close()

def addBookInData(userName,bookName,date,time):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('INSERT INTO library (userName,bookName,dateBook,timeBook) VALUES (?,?,?,?);', (userName,bookName,date,time,))

    conection.commit()
    conection.close()

def searchBookInData(userName):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    data = cursor.execute('SELECT * FROM library WHERE userName = ?', (userName,))
    return list(data)

    conection.commit()
    conection.close()

def deletBookInData(userName):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('DELETE FROM library WHERE userName = ?', (userName,))

    conection.commit()
    conection.close()

def allBookInData():
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    data = cursor.execute('SELECT * FROM library')
    return list(data)

    conection.commit()
    conection.close()

def saveBookInData(userName,bookName,date,time,name):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('UPDATE library SET userName = ?,bookName = ?,dateBook = ?,timeBook = ? WHERE userName = ?;',(userName, bookName, date, time,name))

    conection.commit()
    conection.close()
def searchBookInData(userName):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    data = cursor.execute('SELECT * FROM library WHERE userName = ?', (userName,))
    return list(data)

    conection.commit()
    conection.close()

def deletStudentInData(userName):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('DELETE FROM student WHERE userName = ?', (userName,))

    conection.commit()
    conection.close()

def allStudentInData():
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    data = cursor.execute('SELECT * FROM student')
    return list(data)

    conection.commit()
    conection.close()

def saveStudentInData(userName,fatherName,motherName,adress,phone,email,dateBirth,kindStudent,money,moneyGive,name):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    cursor.execute('UPDATE student SET userName = ?,fatherName = ?,motherName = ?,adress = ?,phone = ?,email = ?,dateBirth = ?,kindStudent = ?,money = ?,moneyGive = ? WHERE userName = ?;',(userName,fatherName,motherName,adress,phone,email,dateBirth,kindStudent,money,moneyGive,name,))

    conection.commit()
    conection.close()

def searchStudentInData(userName):
    conection = sqlite3.connect('./DataBase.bd')
    cursor = conection.cursor()

    data = cursor.execute('SELECT * FROM student WHERE userName = ?', (userName,))
    return list(data)

    conection.commit()
    conection.close()
startUp()