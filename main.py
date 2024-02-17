import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import DataBase

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.schoolImage()
        self.pushButton()
        self.label()
        self.click()
        self.styleApp()

    def pushButton(self):
        self.loginBtn = QPushButton('ورود', self)
        self.loginBtn.setGeometry(200,340,400,50)

        self.newAccountBtn = QPushButton('ایجاد حساب جدید', self)
        self.newAccountBtn.setGeometry(200, 420, 400, 50)

    def label(self):
        self.welcomelbl = QLabel('برنامه مدریت مدرسه', self)
        self.welcomelbl.move(310,250)

    def schoolImage(self):
        self.schoolIcon = QLabel(self)
        self.schoolIcon.move(290,20)
        self.schoolIcon.setPixmap(QPixmap('./resources/Welcome.png'))

    def styleApp(self):
        # Button
        self.loginBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 25px; background: #19A7CE; font: 57 15pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.newAccountBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 25px; background: #19A7CE; font: 57 15pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # leble
        self.welcomelbl.setStyleSheet('font: 57 20pt "Dubai Medium";')

    def click(self):
        self.loginBtn.clicked.connect(self.goLogin)
        self.newAccountBtn.clicked.connect(self.goNewAccount)

    def goLogin(self):
        widget.addWidget(LoginPage())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goNewAccount(self):
        widget.addWidget(NewAccountPage())
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginPage(QWidget):
    user = ''
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.pushButton()
        self.lineEdit()
        self.lable()
        self.loginImage()
        self.click()
        self.styleApp()

    def pushButton(self):
        self.loginBtn = QPushButton('ورود', self)
        self.loginBtn.setGeometry(230,430,350,50)

        self.backBtn = QPushButton('بازگشت', self)
        self.backBtn.setGeometry(230, 500, 350, 50)

    def lineEdit(self):
        self.userNameLE = QLineEdit(self)
        self.userNameLE.setGeometry(150,240,300,40)

        self.passwordLE = QLineEdit(self)
        self.passwordLE.setGeometry(150, 320, 300, 40)
        self.passwordLE.setEchoMode(QLineEdit.Password)

    def lable(self):
        self.userNamelbl = QLabel('نام کاربری :', self)
        self.userNamelbl.move(550,240)

        self.passwordlbl = QLabel('رمز عبور :', self)
        self.passwordlbl.move(550, 320)

        self.wronglbl = QLabel(self)
        self.wronglbl.move(550, 320)

    def loginImage(self):
        self.loginIcan = QLabel(self)
        self.loginIcan.move(340,40)
        self.loginIcan.setPixmap(QPixmap('./resources/UserLogin.png'))

    def styleApp(self):
        # Button
        self.loginBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 25px; background: #19A7CE; font: 57 15pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.backBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 25px; background: #19A7CE; font: 57 15pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # label
        self.userNamelbl.setStyleSheet('font: 57 15pt "Dubai Medium";')
        self.passwordlbl.setStyleSheet('font: 57 15pt "Dubai Medium";')
        # LineEdit
        self.userNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.passwordLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')

    def click(self):
        self.backBtn.clicked.connect(self.BackPage)
        self.loginBtn.clicked.connect(self.login)

    def login(self):
        userName = self.userNameLE.text()
        password = self.passwordLE.text()
        data = DataBase.login(userName)

        if data == password:
            LoginPage.user = userName
            widget.addWidget(MenuPage())
            widget.setCurrentIndex(widget.currentIndex() + 1)
        elif len(userName) == 0 or len(password) == 0:
            self.wronglbl.setText('لطفا کادر ها را پر کنید')
            self.wronglbl.setStyleSheet('font: 57 11pt "Dubai Medium"; color:red;')
            self.wronglbl.move(360, 385)
        else:
            self.wronglbl.setText('اطلاعات حساب شما اشتباه است.')
            self.wronglbl.setStyleSheet('font: 57 11pt "Dubai Medium"; color:red;')
            self.wronglbl.move(320, 385)
        self.wronglbl.adjustSize()

    def BackPage(self):
        widget.removeWidget(widget.currentWidget())

class NewAccountPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.pushButton()
        self.lineEdit()
        self.lable()
        self.loginImage()
        self.click()
        self.styleApp()

    def pushButton(self):
        self.newAccountBtn = QPushButton('ایجاد حساب جدید', self)
        self.newAccountBtn.setGeometry(230, 430, 350, 50)

        self.backBtn = QPushButton('بازگشت', self)
        self.backBtn.setGeometry(230, 500, 350, 50)

    def lineEdit(self):
        self.userNameLE = QLineEdit(self)
        self.userNameLE.setGeometry(150, 220, 300, 40)

        self.passwordLE = QLineEdit(self)
        self.passwordLE.setGeometry(150, 275, 300, 40)
        self.passwordLE.setEchoMode(QLineEdit.Password)

        self.repasswordLE = QLineEdit(self)
        self.repasswordLE.setGeometry(150, 330, 300, 40)
        self.repasswordLE.setEchoMode(QLineEdit.Password)

    def lable(self):
        self.userNamelbl = QLabel('نام کاربری :', self)
        self.userNamelbl.move(550, 220)

        self.passwordlbl = QLabel('رمز عبور :', self)
        self.passwordlbl.move(550, 275)

        self.repasswordlbl = QLabel('رمز عبور :', self)
        self.repasswordlbl.move(550, 330)

        self.wronglbl = QLabel(self)

    def loginImage(self):
        self.loginIcan = QLabel(self)
        self.loginIcan.move(340, 40)
        self.loginIcan.setPixmap(QPixmap('./resources/Users.png'))

    def styleApp(self):
        # Button
        self.newAccountBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 25px; background: #19A7CE; font: 57 15pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.backBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 25px; background: #19A7CE; font: 57 15pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # label
        self.userNamelbl.setStyleSheet('font: 57 15pt "Dubai Medium";')
        self.passwordlbl.setStyleSheet('font: 57 15pt "Dubai Medium";')
        self.repasswordlbl.setStyleSheet('font: 57 15pt "Dubai Medium";')

        # LineEdit
        self.userNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.passwordLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.repasswordLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')

    def click(self):
        self.backBtn.clicked.connect(self.BackPage)
        self.newAccountBtn.clicked.connect(self.newAccount)

    def newAccount(self):
        userName = self.userNameLE.text()
        password = self.passwordLE.text()
        repassword = self.repasswordLE.text()

        if len(userName) == 0 or len(password) == 0 or len(repassword) == 0:
            self.wronglbl.setText('لطفا کادر ها را پر کنید.')
            self.wronglbl.setStyleSheet('font: 57 11pt "Dubai Medium"; color:red;')
            self.wronglbl.move(360, 390)
        elif password != repassword:
            self.wronglbl.setText('اطلاعات وارد شده اشتباه است.')
            self.wronglbl.setStyleSheet('font: 57 11pt "Dubai Medium"; color:red;')
            self.wronglbl.move(325, 390)
        elif len(password) < 8 or len(repassword) < 8:
            self.wronglbl.setText('رمز عبور باید بزرگ تر از هشت رقم باشد.')
            self.wronglbl.setStyleSheet('font: 57 11pt "Dubai Medium"; color:red;')
            self.wronglbl.move(300, 390)
        elif len(userName) > 0 and len(password) > 0 and len(repassword) > 0 and password == repassword:
            DataBase.newAccount(userName, password)
            self.wronglbl.setText('حساب کاربری شما ایجاد شد.')
            self.wronglbl.setStyleSheet('font: 57 11pt "Dubai Medium"; color:green;')
            self.wronglbl.move(330, 390)
        self.wronglbl.adjustSize()

    def BackPage(self):
        widget.removeWidget(widget.currentWidget())

class MenuPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.background()
        self.pushButton()
        self.icon()
        self.label()
        self.click()
        self.styleApp()

    def background(self):
        self.back = QLabel(self)
        self.back.setGeometry(0,0,600,600)
        self.back.setStyleSheet('background-color:#d6d2d2;')

    def pushButton(self):
        self.studentBtn = QPushButton('         ثبت دانش آموز        ', self)
        self.studentBtn.setIcon(QIcon('./resources/StudentBtn.png'))
        self.studentBtn.setGeometry(615,50,170,35)

        self.libraryBtn = QPushButton('           کتاب خانه             ', self)
        self.libraryBtn.setIcon(QIcon('./resources/Library.png'))
        self.libraryBtn.setGeometry(615, 100, 170, 35)

        self.libraryListBtn = QPushButton('       لیست کتاب خانه       ', self)
        self.libraryListBtn.setIcon(QIcon('./resources/SearchStudentBtn.png'))
        self.libraryListBtn.setGeometry(615, 150, 170, 35)

        self.studentListBtn = QPushButton('       لیست دانش آموز       ', self)
        self.studentListBtn.setIcon(QIcon('./resources/SearchLibraryBtn.png'))
        self.studentListBtn.setGeometry(615, 200, 170, 35)

    def icon(self):
        self.iconlbl = QLabel(self)
        self.iconlbl.move(40,20)
        self.iconlbl.setPixmap(QPixmap('./resources/Student.png'))

    def label(self):
        self.userlbl = QLabel(LoginPage.user,self)
        self.userlbl.move(680,555)

        self.image = QLabel(self)
        self.image.move(620,540)
        self.image.setPixmap(QPixmap('./resources/UserMenu.png'))

    def styleApp(self):
        # Button
        self.studentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.studentListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # leble
        self.userlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')

    def click(self):
        self.studentBtn.clicked.connect(self.studentPage)
        self.libraryBtn.clicked.connect(self.libraryPage)
        self.libraryListBtn.clicked.connect(self.libraryListPage)
        self.studentListBtn.clicked.connect(self.studentListPage)

    def studentPage(self):
        widget.addWidget(StudentPage())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def libraryPage(self):
        widget.addWidget(LibraryPage())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def studentListPage(self):
        widget.addWidget(StudentListPage())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def libraryListPage(self):
        widget.addWidget(LibraryListPage())
        widget.setCurrentIndex(widget.currentIndex()+1)

class StudentPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.background()
        self.pushButton()
        self.label()
        self.lineEdit()
        self.click()
        self.table()
        self.styleApp()


    def background(self):
        self.back = QLabel(self)
        self.back.setGeometry(0, 0, 600, 600)
        self.back.setStyleSheet('background-color:#d6d2d2;')

    def pushButton(self):
        self.studentBtn = QPushButton('         ثبت دانش آموز        ', self)
        self.studentBtn.setIcon(QIcon('./resources/StudentBtn.png'))
        self.studentBtn.setGeometry(615, 50, 170, 35)

        self.libraryBtn = QPushButton('           کتاب خانه             ', self)
        self.libraryBtn.setIcon(QIcon('./resources/Library.png'))
        self.libraryBtn.setGeometry(615, 100, 170, 35)

        self.libraryListBtn = QPushButton('       لیست کتاب خانه       ', self)
        self.libraryListBtn.setIcon(QIcon('./resources/SearchStudentBtn.png'))
        self.libraryListBtn.setGeometry(615, 150, 170, 35)

        self.studentListBtn = QPushButton('       لیست دانش آموز       ', self)
        self.studentListBtn.setIcon(QIcon('./resources/SearchLibraryBtn.png'))
        self.studentListBtn.setGeometry(615, 200, 170, 35)

        self.addStudentBtn = QPushButton('اضافه کردن', self)
        self.addStudentBtn.setGeometry(265,250,100,30)

        self.deletStudentBtn = QPushButton('حذف', self)
        self.deletStudentBtn.setGeometry(370, 250, 100, 30)

        self.deletAllStudentBtn = QPushButton('خالی کردن لیست', self)
        self.deletAllStudentBtn.setGeometry(475, 250, 100, 30)

        self.saveStudentBtn = QPushButton('ذخیره در پایگاه داده', self)
        self.saveStudentBtn.setGeometry(40, 250, 100, 30)

    def label(self):
        self.userlbl = QLabel(LoginPage.user, self)
        self.userlbl.move(680, 555)

        self.image = QLabel(self)
        self.image.move(620, 540)
        self.image.setPixmap(QPixmap('./resources/UserMenu.png'))

        self.userNamelbl = QLabel('نام', self)
        self.userNamelbl.move(540, 12)

        self.fatherNamelbl = QLabel('نام پدر', self)
        self.fatherNamelbl.move(540, 62)

        self.motherNamelbl = QLabel('نام مادر', self)
        self.motherNamelbl.move(540, 112)

        self.adresslbl = QLabel('آدرس', self)
        self.adresslbl.move(540, 162)

        self.phonelbl = QLabel('شماره موبایل', self)
        self.phonelbl.move(250, 12)

        self.emaillbl = QLabel('آدرس ایمیل', self)
        self.emaillbl.move(250, 62)

        self.dateBirthlbl = QLabel('تاریخ تولد', self)
        self.dateBirthlbl.move(250, 112)

        self.moneylbl = QLabel('شهریه', self)
        self.moneylbl.move(250, 162)

        self.moneyGivelbl = QLabel('پرداختی', self)
        self.moneyGivelbl.move(540, 212)

        self.kindeStudentlbl = QLabel('جنسیت', self)
        self.kindeStudentlbl.move(250, 212)

    def lineEdit(self):
        self.userNameLE = QLineEdit(self)
        self.userNameLE.setGeometry(330,10,200,30)

        self.fatherNameLE = QLineEdit(self)
        self.fatherNameLE.setGeometry(330, 60, 200, 30)

        self.motherNameLE = QLineEdit(self)
        self.motherNameLE.setGeometry(330, 110, 200, 30)

        self.adressLE = QLineEdit(self)
        self.adressLE.setGeometry(330, 160, 200, 30)

        self.phoneLE = QLineEdit(self)
        self.phoneLE.setGeometry(40, 10, 200, 30)

        self.emailLE = QLineEdit(self)
        self.emailLE.setGeometry(40, 60, 200, 30)

        self.dateBirthLE = QLineEdit(self)
        self.dateBirthLE.setGeometry(40, 110, 200, 30)

        self.moneyLE = QLineEdit(self)
        self.moneyLE.setGeometry(40, 160, 200, 30)

        self.moneyGiveLE = QLineEdit(self)
        self.moneyGiveLE.setGeometry(330, 210, 200, 30)

        self.kindeStudent = QComboBox(self)
        self.kindeStudent.addItem('هیچکدام', self)
        self.kindeStudent.addItem('دختر', self)
        self.kindeStudent.addItem('پسر', self)
        self.kindeStudent.setGeometry(40,210,200,30)
        self.kindeStudent.activated[str].connect(self.kindeStudentText)
        self.kindeStudentTx = 'هیچکدام'

    def kindeStudentText(self, Text):
        self.kindeStudentTx = Text

    def table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(40,300,530,270)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['نام','نام پدر','نام مادر','آدرس','شماره موبایل','آدرس ایمیل','تاریخ تولد','جنسیت','شهریه','پرداختی'])

    def styleApp(self):
        # Button
        self.studentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.studentListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.addStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.deletStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.deletAllStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.saveStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # leble
        self.userlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.userNamelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.fatherNamelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.motherNamelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.adresslbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.phonelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.emaillbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.dateBirthlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.moneylbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.moneyGivelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.kindeStudentlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        # LineEdit
        self.userNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.fatherNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.motherNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.adressLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.phoneLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.emailLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.dateBirthLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.moneyLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.moneyGiveLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.kindeStudent.setStyleSheet('QComboBox { color: #000000; border: 2px solid #19A7CE; background: #AFD3E2; font: 57 10pt "Dubai Medium";}')
        # table
        self.tableWidget.setStyleSheet('QTableWidget { color: #000000; border: 2px solid #19A7CE;}')
    def click(self):
        self.studentBtn.clicked.connect(self.studentPage)
        self.libraryBtn.clicked.connect(self.libraryPage)
        self.libraryListBtn.clicked.connect(self.libraryListPage)
        self.studentListBtn.clicked.connect(self.studentListPage)
        self.addStudentBtn.clicked.connect(self.addTableItem)
        self.deletStudentBtn.clicked.connect(self.removeTableItem)
        self.deletAllStudentBtn.clicked.connect(self.removeAllItem)
        self.saveStudentBtn.clicked.connect(self.saveAllStudent)

    def studentPage(self):
        widget.addWidget(StudentPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryPage(self):
        widget.addWidget(LibraryPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def studentListPage(self):
        widget.addWidget(StudentListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryListPage(self):
        widget.addWidget(LibraryListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def addTableItem(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount+1)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(self.userNameLE.text()))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(self.fatherNameLE.text()))
        self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(self.motherNameLE.text()))
        self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(self.adressLE.text()))
        self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(self.phoneLE.text()))
        self.tableWidget.setItem(rowCount, 5, QTableWidgetItem(self.emailLE.text()))
        self.tableWidget.setItem(rowCount, 6, QTableWidgetItem(self.dateBirthLE.text()))
        self.tableWidget.setItem(rowCount, 7, QTableWidgetItem(self.kindeStudentTx))
        self.tableWidget.setItem(rowCount, 8, QTableWidgetItem(self.moneyLE.text()))
        self.tableWidget.setItem(rowCount, 9, QTableWidgetItem(self.moneyGiveLE.text()))

        self.userNameLE.setText('')
        self.fatherNameLE.setText('')
        self.motherNameLE.setText('')
        self.adressLE.setText('')
        self.phoneLE.setText('')
        self.emailLE.setText('')
        self.dateBirthLE.setText('')
        self.moneyLE.setText('')
        self.moneyGiveLE.setText('')

    def removeTableItem(self):
        row = self.tableWidget.currentRow()
        self.tableWidget.removeRow(row)

    def removeAllItem(self):
        rowCount = self.tableWidget.rowCount()
        for row in range(0,rowCount):
            self.tableWidget.removeRow(0)

    def saveAllStudent(self):
        rowCount = self.tableWidget.rowCount()
        for row in range(0,rowCount):
            userName = self.tableWidget.item(row,0).text()
            fatherName = self.tableWidget.item(row,1).text()
            motherName = self.tableWidget.item(row,2).text()
            adrees = self.tableWidget.item(row,3).text()
            phone = self.tableWidget.item(row,4).text()
            email = self.tableWidget.item(row,5).text()
            date = self.tableWidget.item(row,6).text()
            kindStudent = self.tableWidget.item(row,7).text()
            money = self.tableWidget.item(row,8).text()
            moneyGive = self.tableWidget.item(row,9).text()
            DataBase.addStudentInData(userName,fatherName,motherName,adrees,phone,email,date,kindStudent,money,moneyGive)
        for row in range(0,rowCount):
            self.tableWidget.removeRow(0)

class LibraryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.background()
        self.pushButton()
        self.label()
        self.lineEdit()
        self.click()
        self.table()
        self.styleApp()

    def background(self):
        self.back = QLabel(self)
        self.back.setGeometry(0, 0, 600, 600)
        self.back.setStyleSheet('background-color:#d6d2d2;')

    def pushButton(self):
        self.studentBtn = QPushButton('         ثبت دانش آموز        ', self)
        self.studentBtn.setIcon(QIcon('./resources/StudentBtn.png'))
        self.studentBtn.setGeometry(615, 50, 170, 35)

        self.libraryBtn = QPushButton('           کتاب خانه             ', self)
        self.libraryBtn.setIcon(QIcon('./resources/Library.png'))
        self.libraryBtn.setGeometry(615, 100, 170, 35)

        self.libraryListBtn = QPushButton('       لیست کتاب خانه       ', self)
        self.libraryListBtn.setIcon(QIcon('./resources/SearchStudentBtn.png'))
        self.libraryListBtn.setGeometry(615, 150, 170, 35)

        self.studentListBtn = QPushButton('       لیست دانش آموز       ', self)
        self.studentListBtn.setIcon(QIcon('./resources/SearchLibraryBtn.png'))
        self.studentListBtn.setGeometry(615, 200, 170, 35)

        self.addStudentBtn = QPushButton('اضافه کردن', self)
        self.addStudentBtn.setGeometry(265, 250, 100, 30)

        self.deletStudentBtn = QPushButton('حذف', self)
        self.deletStudentBtn.setGeometry(370, 250, 100, 30)

        self.deletAllStudentBtn = QPushButton('خالی کردن لیست', self)
        self.deletAllStudentBtn.setGeometry(475, 250, 100, 30)

        self.saveStudentBtn = QPushButton('ذخیره در پایگاه داده', self)
        self.saveStudentBtn.setGeometry(40, 250, 100, 30)

    def label(self):
        self.userlbl = QLabel(LoginPage.user, self)
        self.userlbl.move(680, 555)

        self.image = QLabel(self)
        self.image.move(620, 540)
        self.image.setPixmap(QPixmap('./resources/UserMenu.png'))

        self.userNamelbl = QLabel('نام', self)
        self.userNamelbl.move(520, 92)

        self.bookNamelbl = QLabel('نام کتاب', self)
        self.bookNamelbl.move(520, 162)

        self.datelbl = QLabel('تاریخ تحویل', self)
        self.datelbl.move(220, 92)

        self.timelbl = QLabel('مدت زمان', self)
        self.timelbl.move(220, 162)

    def lineEdit(self):
        self.userNameLE = QLineEdit(self)
        self.userNameLE.setGeometry(320, 90, 180, 30)

        self.bookNameLE = QLineEdit(self)
        self.bookNameLE.setGeometry(320, 160, 180, 30)

        self.dateLE = QLineEdit(self)
        self.dateLE.setGeometry(20, 90, 180, 30)
        date = datetime.now().strftime('%Y-%m-%d')
        self.dateLE.setText(date)


        self.timeLE = QLineEdit(self)
        self.timeLE.setGeometry(20, 160, 180, 30)

    def table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(40, 300, 530, 270)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 131)
        self.tableWidget.setColumnWidth(3, 125)
        self.tableWidget.setHorizontalHeaderLabels(['نام', 'نام کتاب', 'تاریخ تحویل', 'مدت'])

    def styleApp(self):
        # Button
        self.studentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.studentListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.addStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.deletStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.deletAllStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.saveStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # leble
        self.userlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.userNamelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.bookNamelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.datelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        self.timelbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        # LineEdit
        self.userNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.bookNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.dateLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        self.timeLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        # table
        self.tableWidget.setStyleSheet('QTableWidget { color: #000000; border: 2px solid #19A7CE;}')

    def click(self):
        self.studentBtn.clicked.connect(self.studentPage)
        self.libraryBtn.clicked.connect(self.libraryPage)
        self.libraryListBtn.clicked.connect(self.libraryListPage)
        self.studentListBtn.clicked.connect(self.studentListPage)
        self.addStudentBtn.clicked.connect(self.addTableItem)
        self.deletStudentBtn.clicked.connect(self.removeTableItem)
        self.deletAllStudentBtn.clicked.connect(self.removeAllItem)
        self.saveStudentBtn.clicked.connect(self.saveAllStudent)

    def studentPage(self):
        widget.addWidget(StudentPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryPage(self):
        widget.addWidget(LibraryPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def studentListPage(self):
        widget.addWidget(StudentListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryListPage(self):
        widget.addWidget(LibraryListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def addTableItem(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount + 1)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(self.userNameLE.text()))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(self.bookNameLE.text()))
        self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(self.dateLE.text()))
        self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(self.timeLE.text()))

        self.userNameLE.setText('')
        self.bookNameLE.setText('')
        self.timeLE.setText('')

    def removeTableItem(self):
        row = self.tableWidget.currentRow()
        self.tableWidget.removeRow(row)

    def removeAllItem(self):
        rowCount = self.tableWidget.rowCount()
        for row in range(0, rowCount):
            self.tableWidget.removeRow(0)

    def saveAllStudent(self):
        rowCount = self.tableWidget.rowCount()
        for row in range(0, rowCount):
            userName = self.tableWidget.item(row, 0).text()
            bookName = self.tableWidget.item(row, 1).text()
            date = self.tableWidget.item(row, 2).text()
            time = self.tableWidget.item(row, 3).text()

            DataBase.addBookInData(userName,bookName,date,time)
        for row in range(0, rowCount):
            self.tableWidget.removeRow(0)

class StudentListPage(QWidget):
    libraryBookName = []

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.background()
        self.pushButton()
        self.label()
        self.lineEdit()
        self.click()
        self.table()
        self.styleApp()
        self.showAllItem()

    def background(self):
        self.back = QLabel(self)
        self.back.setGeometry(0, 0, 600, 600)
        self.back.setStyleSheet('background-color:#d6d2d2;')

    def pushButton(self):
        self.studentBtn = QPushButton('         ثبت دانش آموز        ', self)
        self.studentBtn.setIcon(QIcon('./resources/StudentBtn.png'))
        self.studentBtn.setGeometry(615, 50, 170, 35)

        self.libraryBtn = QPushButton('           کتاب خانه             ', self)
        self.libraryBtn.setIcon(QIcon('./resources/Library.png'))
        self.libraryBtn.setGeometry(615, 100, 170, 35)

        self.libraryListBtn = QPushButton('       لیست کتاب خانه       ', self)
        self.libraryListBtn.setIcon(QIcon('./resources/SearchStudentBtn.png'))
        self.libraryListBtn.setGeometry(615, 150, 170, 35)

        self.studentListBtn = QPushButton('       لیست دانش آموز       ', self)
        self.studentListBtn.setIcon(QIcon('./resources/SearchLibraryBtn.png'))
        self.studentListBtn.setGeometry(615, 200, 170, 35)

        self.searchStudentBtn = QPushButton('جستجو', self)
        self.searchStudentBtn.setGeometry(475, 10, 100, 30)

        self.deletStudentBtn = QPushButton('حذف', self)
        self.deletStudentBtn.setGeometry(475, 50, 100, 30)

        self.showAllStudentBtn = QPushButton('نمایش همه', self)
        self.showAllStudentBtn.setGeometry(225, 50, 100, 30)

        self.saveStudentBtn = QPushButton('ذخیره در پایگاه داده', self)
        self.saveStudentBtn.setGeometry(40, 50, 100, 30)

    def label(self):
        self.userlbl = QLabel(LoginPage.user, self)
        self.userlbl.move(680, 555)

        self.image = QLabel(self)
        self.image.move(620, 540)
        self.image.setPixmap(QPixmap('./resources/UserMenu.png'))

    def lineEdit(self):
        self.userNameLE = QLineEdit(self)
        self.userNameLE.setGeometry(225, 10, 210, 35)

    def table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(40, 100, 530, 470)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['نام','نام پدر','نام مادر','آدرس','شماره موبایل','آدرس ایمیل','تاریخ تولد','جنسیت','شهریه','پرداختی'])

    def styleApp(self):
        # Button
        self.studentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.studentListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.searchStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.deletStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.showAllStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.saveStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # leble
        self.userlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        # LineEdit
        self.userNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
        # table
        self.tableWidget.setStyleSheet('QTableWidget { color: #000000; border: 2px solid #19A7CE;}')

    def click(self):
        self.studentBtn.clicked.connect(self.studentPage)
        self.libraryBtn.clicked.connect(self.libraryPage)
        self.libraryListBtn.clicked.connect(self.libraryListPage)
        self.studentListBtn.clicked.connect(self.studentListPage)
        self.searchStudentBtn.clicked.connect(self.searchTableItem)
        self.deletStudentBtn.clicked.connect(self.removeTableItem)
        self.showAllStudentBtn.clicked.connect(self.showAllItem)
        self.saveStudentBtn.clicked.connect(self.saveAllStudent)

    def studentPage(self):
        widget.addWidget(StudentPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryPage(self):
        widget.addWidget(LibraryPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def studentListPage(self):
        widget.addWidget(StudentListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryListPage(self):
        widget.addWidget(LibraryListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def searchTableItem(self):
        LibraryListPage.libraryBookName.clear()
        rowCount = self.tableWidget.rowCount()
        userName = self.userNameLE.text()
        data = DataBase.searchStudentInData(userName)
        for row in range(0, rowCount):
            self.tableWidget.removeRow(0)
        for item in data:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rowCount + 1)
            self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(item[2]))
            self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(item[3]))
            self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(item[4]))
            self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(item[5]))
            self.tableWidget.setItem(rowCount, 5, QTableWidgetItem(item[6]))
            self.tableWidget.setItem(rowCount, 6, QTableWidgetItem(item[7]))
            self.tableWidget.setItem(rowCount, 7, QTableWidgetItem(item[8]))
            self.tableWidget.setItem(rowCount, 8, QTableWidgetItem(item[9]))
            self.tableWidget.setItem(rowCount, 9, QTableWidgetItem(item[10]))
            LibraryListPage.libraryBookName.append(item[1])

    def removeTableItem(self):
        try:
            currentRow = self.tableWidget.currentRow()
            userName = self.tableWidget.item(currentRow, 0).text()
            DataBase.deletStudentInData(userName)
            row = self.tableWidget.currentRow()
            self.tableWidget.removeRow(row)
        except:
            pass

    def showAllItem(self):
        LibraryListPage.libraryBookName.clear()
        data = DataBase.allStudentInData()
        rowCount = self.tableWidget.rowCount()
        for row in range(0, rowCount):
            self.tableWidget.removeRow(0)
        for item in data:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rowCount + 1)
            self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(item[2]))
            self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(item[3]))
            self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(item[4]))
            self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(item[5]))
            self.tableWidget.setItem(rowCount, 5, QTableWidgetItem(item[6]))
            self.tableWidget.setItem(rowCount, 6, QTableWidgetItem(item[7]))
            self.tableWidget.setItem(rowCount, 7, QTableWidgetItem(item[8]))
            self.tableWidget.setItem(rowCount, 8, QTableWidgetItem(item[9]))
            self.tableWidget.setItem(rowCount, 9, QTableWidgetItem(item[10]))
            LibraryListPage.libraryBookName.append(item[1])

    def saveAllStudent(self):
        num = 0
        count = self.tableWidget.rowCount()
        for row in range(0, count):
            name = LibraryListPage.libraryBookName[num]
            userName = self.tableWidget.item(row, 0).text()
            fatherName = self.tableWidget.item(row, 1).text()
            motherName = self.tableWidget.item(row, 2).text()
            adress = self.tableWidget.item(row, 3).text()
            phone = self.tableWidget.item(row, 4).text()
            email = self.tableWidget.item(row, 5).text()
            dateBirth = self.tableWidget.item(row, 6).text()
            kindStudent = self.tableWidget.item(row, 7).text()
            money = self.tableWidget.item(row, 8).text()
            moneyGive = self.tableWidget.item(row, 9).text()
            DataBase.saveStudentInData(userName,fatherName,motherName,adress,phone,email,dateBirth,kindStudent,money,moneyGive,name)
            num += 1
        for row in range(0, count):
            self.tableWidget.removeRow(0)

class LibraryListPage(QWidget):
    libraryBookName = []
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.background()
        self.pushButton()
        self.label()
        self.lineEdit()
        self.click()
        self.table()
        self.styleApp()
        self.showAllItem()

    def background(self):
        self.back = QLabel(self)
        self.back.setGeometry(0, 0, 600, 600)
        self.back.setStyleSheet('background-color:#d6d2d2;')

    def pushButton(self):
        self.studentBtn = QPushButton('         ثبت دانش آموز        ', self)
        self.studentBtn.setIcon(QIcon('./resources/StudentBtn.png'))
        self.studentBtn.setGeometry(615, 50, 170, 35)

        self.libraryBtn = QPushButton('           کتاب خانه             ', self)
        self.libraryBtn.setIcon(QIcon('./resources/Library.png'))
        self.libraryBtn.setGeometry(615, 100, 170, 35)

        self.libraryListBtn = QPushButton('       لیست کتاب خانه       ', self)
        self.libraryListBtn.setIcon(QIcon('./resources/SearchStudentBtn.png'))
        self.libraryListBtn.setGeometry(615, 150, 170, 35)

        self.studentListBtn = QPushButton('       لیست دانش آموز       ', self)
        self.studentListBtn.setIcon(QIcon('./resources/SearchLibraryBtn.png'))
        self.studentListBtn.setGeometry(615, 200, 170, 35)

        self.searchStudentBtn = QPushButton('جستجو', self)
        self.searchStudentBtn.setGeometry(475, 10, 100, 30)

        self.deletStudentBtn = QPushButton('حذف', self)
        self.deletStudentBtn.setGeometry(475, 50, 100, 30)

        self.showAllStudentBtn = QPushButton('نمایش همه', self)
        self.showAllStudentBtn.setGeometry(225, 50, 100, 30)

        self.saveStudentBtn = QPushButton('ذخیره در پایگاه داده', self)
        self.saveStudentBtn.setGeometry(40, 50, 100, 30)

    def label(self):
        self.userlbl = QLabel(LoginPage.user, self)
        self.userlbl.move(680, 555)

        self.image = QLabel(self)
        self.image.move(620, 540)
        self.image.setPixmap(QPixmap('./resources/UserMenu.png'))

    def lineEdit(self):
        self.userNameLE = QLineEdit(self)
        self.userNameLE.setGeometry(225, 10, 210, 35)

    def table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(40, 100, 530, 470)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 131)
        self.tableWidget.setColumnWidth(3, 125)
        self.tableWidget.setHorizontalHeaderLabels(['نام', 'نام کتاب', 'تاریخ تحویل', 'مدت'])

    def styleApp(self):
        # Button
        self.studentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.studentListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.libraryListBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.searchStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.deletStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.showAllStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        self.saveStudentBtn.setStyleSheet('QPushButton{color: #E9E8E8; border-radius: 15px; background: #19A7CE; font: 57 10pt "Dubai Medium";} QPushButton:hover{background: #146C94;}')
        # leble
        self.userlbl.setStyleSheet('font: 57 10pt "Dubai Medium";')
        # LineEdit
        self.userNameLE.setStyleSheet('QLineEdit { color: #000000; border: 2px solid #19A7CE; border-radius: 15px; padding: 0px 15px; background: #AFD3E2;} QLineEdit:focus {border: 2px solid #1ecdf8;}')
       # table
        self.tableWidget.setStyleSheet('QTableWidget { color: #000000; border: 2px solid #19A7CE;}')

    def click(self):
        self.studentBtn.clicked.connect(self.studentPage)
        self.libraryBtn.clicked.connect(self.libraryPage)
        self.libraryListBtn.clicked.connect(self.libraryListPage)
        self.studentListBtn.clicked.connect(self.studentListPage)
        self.searchStudentBtn.clicked.connect(self.searchTableItem)
        self.deletStudentBtn.clicked.connect(self.removeTableItem)
        self.showAllStudentBtn.clicked.connect(self.showAllItem)
        self.saveStudentBtn.clicked.connect(self.saveAllStudent)

    def studentPage(self):
        widget.addWidget(StudentPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryPage(self):
        widget.addWidget(LibraryPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def studentListPage(self):
        widget.addWidget(StudentListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def libraryListPage(self):
        widget.addWidget(LibraryListPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def searchTableItem(self):
        LibraryListPage.libraryBookName.clear()
        rowCount = self.tableWidget.rowCount()
        userName = self.userNameLE.text()
        data = DataBase.searchBookInData(userName)
        for row in range(0, rowCount):
            self.tableWidget.removeRow(0)
        for item in data:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rowCount+1)
            self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(item[2]))
            self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(item[3]))
            self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(item[4]))
            LibraryListPage.libraryBookName.append(item[1])

    def removeTableItem(self):
        try:
            currentRow = self.tableWidget.currentRow()
            userName = self.tableWidget.item(currentRow,0).text()
            DataBase.deletBookInData(userName)
            row = self.tableWidget.currentRow()
            self.tableWidget.removeRow(row)
        except:
            pass

    def showAllItem(self):
        LibraryListPage.libraryBookName.clear()
        data = DataBase.allBookInData()
        rowCount = self.tableWidget.rowCount()
        for row in range(0, rowCount):
            self.tableWidget.removeRow(0)
        for item in data:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rowCount+1)
            self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(item[2]))
            self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(item[3]))
            self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(item[4]))
            LibraryListPage.libraryBookName.append(item[1])

    def saveAllStudent(self):
        num = 0
        count = self.tableWidget.rowCount()
        for row in range(0, count):
            name = LibraryListPage.libraryBookName[num]
            userName = self.tableWidget.item(row,0).text()
            bookName = self.tableWidget.item(row,1).text()
            date = self.tableWidget.item(row,2).text()
            time = self.tableWidget.item(row,3).text()
            DataBase.saveBookInData(userName, bookName, date, time, name)
            num += 1
        for row in range(0, count):
            self.tableWidget.removeRow(0)

def main():
    global widget
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.setObjectName('widget')
    Ui = WelcomePage()

    # Setting
    widget.setWindowTitle('مدیریت مدرسه')
    widget.setWindowIcon(QIcon('./resources/Callage.ico'))
    widget.setFixedWidth(800)
    widget.setFixedHeight(600)
    widget.resize(800,600)
    widget.addWidget(Ui)

    widget.show()
    sys.exit(app.exec_())

main()