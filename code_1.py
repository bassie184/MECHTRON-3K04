from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import serial

from serial.tools import list_ports

import time

list_ports.comports()  # Outputs list of available serial ports

ser = serial.Serial('COM5', 115200, timeout = 1)

#ser = serial.Serial('COM5', 115200)
#first window to allow user to login and add user
#created by QT Designer to intilize labels, textboxes, and buttons

class Ui_LoginWindow(object):

    def setupUi(self, LoginWindow):

        #sets up shape of window

        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(456, 171)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        #general label format
        #sets up welcome text message

        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(19, 10, 393, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Welcome.setFont(font)
        self.Welcome.setObjectName("Welcome")

        self.UserName_2 = QtWidgets.QLabel(self.centralwidget)
        self.UserName_2.setGeometry(QtCore.QRect(30, 50, 64, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.UserName_2.setFont(font)
        self.UserName_2.setObjectName("UserName_2")

        #username input box, allows user to type in it

        self.UserName = QtWidgets.QLineEdit(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(100, 50, 191, 20))
        self.UserName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UserName.setObjectName("UserName")

        self.Password_2 = QtWidgets.QLabel(self.centralwidget)
        self.Password_2.setGeometry(QtCore.QRect(30, 80, 57, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Password_2.setFont(font)
        self.Password_2.setObjectName("Password_2")

        #password input box

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(100, 80, 191, 20))
        self.Password.setObjectName("Password")

        #login button

        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(300, 50, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")

        #sets up connection of button click and actions in seperage function

        self.Login.clicked.connect(self.LoginClicked)

        #add user button & counter

        self.AddUser = QtWidgets.QPushButton(self.centralwidget)
        self.AddUser.setGeometry(QtCore.QRect(300, 80, 111, 23))
        self.AddUser.setObjectName("AddUser")

        self.UserCounter = 0

        self.AddUser.clicked.connect(self.AddUserClicked)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 25, 401, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 100, 401, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(410, 40, 20, 71))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 40, 20, 71))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi1(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    #made by QT Designer, changes texts boxes to new value

    def retranslateUi1(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Pace Maker User Interface"))
        self.Welcome.setText(_translate("LoginWindow", "Welcome to PaceMaker Pro: LOGIN MENU"))
        self.UserName_2.setText(_translate("LoginWindow", "User Name:"))
        self.Password_2.setText(_translate("LoginWindow", "Password:"))
        self.Login.setText(_translate("LoginWindow", "LOGIN"))
        self.AddUser.setText(_translate("LoginWindow", "ADD USER (Max 10.)"))

    #rewrites array with added users into the textfile

    def FileWrite(self, w):
        f = open("guru.txt", "a+")
        for i in range (len(w)):
            for j in range(len(w[i])):
                f.write (w[i][j] + " ")
            f.write ("\n")
        f.close()

    #reads from textfile and outputs file into an array so we can edit values

    def GetFile(self):
        f=open("guru.txt", "r")
        GetArrray = [["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""]]

        for i in range (len(GetArrray)):
            read = f.readline()
            GetArrray[i] = read.split (" ")

        for i in range (len(GetArrray)):
            for j in range (len(GetArrray[i])):
                GetArrray[i][j] =  GetArrray[i][j].strip("\n")

        #for i in range (len(GetArrray)):
         #   GetArrray[i].remove("")
        f.close()
        return GetArrray

    #chekcs if username and password match eachother

    def CheckPassword(self, u1, p1):
        Array = self.GetFile()

        for i in range (len(Array)):
            if (Array [i][0] == u1):
                if(Array [i][1] == p1):
                    return 1
        return 0

    #checks if username and password already exist, i.e. not unique

    def CheckNewUser(self, username):
        Array = self.GetFile()
        for i in range (len(Array)):
            if (Array[i][0] == username):
                return 1
        return 0

    #check if username or password have spaces in them

    def ContainsSpace(self, s):
        for i in range (len(s)):
            if(s[i] == " "):
                return 1
        return 0

    #code jumps to this function when 'Login' button is pressed

    def LoginClicked(self):
        #gets username and password
        username = self.UserName.text()
        password = self.Password.text()
        #since user is existing, check whether password is correct
        if self.CheckPassword(username, password):
            #change screens
            LoginWindow.hide()
            MainWindow.show()

        else:
            #password is wrong so show error message
            self.LoginPopUp()

    #code jumps to this function when 'AddUser' button is pressed

    def AddUserClicked(self):

        #uncomment next line to intilize file to contain the first row shown below
        #Array = [["Username","Password","LRL","URL","AA","APW","VA","VPW","VRP","ARP","PVARP"]]

        #change screens
        username = self.UserName.text()
        password = self.Password.text()

        #checks if username has invalid space
        if self.ContainsSpace(username) == 0:
            #checks if password has invalid space
            if self.ContainsSpace(password) == 0:
                #if user is new, adds username and password into the next row of array
                if self.CheckNewUser(username) == 0:
                    if self.UserCounter < 10:
                        #increment counter for number of users
                        self.UserCounter += 1
                        #add username and password into array
                        Array = []
                        Array.append([username, password,"","","","","","","","","","","","","","","","","","","","","",""])
                        #save array into file
                        self.FileWrite(Array)
                        #change screens
                        LoginWindow.hide()
                        MainWindow.show()
                    else:
                        #shows error when user attemptes to add an 11th user
                        self.AddUserPopUp()
                else:
                    #shows error when user name or password is not unique
                    self.NotUniquePopUp()
            else:
                #error for when password has invalid space in it
                self.PasswordSpacePopUp()
        else:
            #error for when username has invalid space in it
            self.UsernameSpacePopup()


    #error mesaages

    def LoginPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Invalid User or Password")
        msg.setText("Sorry, Invalid Information Entered.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Please Enter Valid User Info.")

        x = msg.exec_()

    def AddUserPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Full User List")
        msg.setText("Sorry, no additional users can be added.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Maximum number of users is 10.")

        x = msg.exec_()

    def NotUniquePopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Full User List")
        msg.setText("Sorry, username and password already in use.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("please use a unique username and password.")

        x = msg.exec_()

    def PasswordSpacePopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Invalid Password")
        msg.setText("Sorry, Invalid Space Character.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Please Enter User Info With No Space.")

        x = msg.exec_()

    def UsernameSpacePopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Invalid Username")
        msg.setText("Sorry, Invalid Space Character.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Please Enter User Info With No Space.")

        x = msg.exec_()


#Second window for editing variables and modes after login screen

class Ui_MainWindow(Ui_LoginWindow):

    def setupUiTwo(self, MainWindow):

        #sets up shape of window

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #general label format
        #sets up welcome text message

        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(19, 19, 393, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Welcome.setFont(font)
        self.Welcome.setObjectName("Welcome")

        #loginOutput

        self.LoginOutput = QtWidgets.QLabel(self.centralwidget)
        self.LoginOutput.setGeometry(QtCore.QRect(110, 50, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LoginOutput.setFont(font)
        self.LoginOutput.setObjectName("LoginOutput")

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 31, 491, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.Mode = QtWidgets.QLabel(self.centralwidget)
        self.Mode.setGeometry(QtCore.QRect(20, 100, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Mode.setFont(font)
        self.Mode.setObjectName("Mode")

        self.DeviceCommunicate = QtWidgets.QLabel(self.centralwidget)
        self.DeviceCommunicate.setGeometry(QtCore.QRect(20, 390, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeviceCommunicate.setFont(font)
        self.DeviceCommunicate.setObjectName("DeviceCommunicate")

        #device communication output

        self.DeviceCommunicateOutput = QtWidgets.QLabel(self.centralwidget)
        self.DeviceCommunicateOutput.setGeometry(QtCore.QRect(60, 420, 71, 21))
        self.DeviceCommunicateOutput.setObjectName("DeviceCommunicateOutput")


        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(20, 55, 591, 51))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        #mode output

        self.ModeOutput = QtWidgets.QLabel(self.centralwidget)
        self.ModeOutput.setGeometry(QtCore.QRect(110, 250, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ModeOutput.setFont(font)
        self.ModeOutput.setObjectName("ModeOutput")


        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.setGeometry(QtCore.QRect(20, 50, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.User.setFont(font)
        self.User.setObjectName("User")

        self.LRL = QtWidgets.QLabel(self.centralwidget)
        self.LRL.setGeometry(QtCore.QRect(270, 120, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LRL.setFont(font)
        self.LRL.setObjectName("LRL")

        self.ReEnter = QtWidgets.QLabel(self.centralwidget)
        self.ReEnter.setGeometry(QtCore.QRect(260, 60, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ReEnter.setFont(font)
        self.ReEnter.setObjectName("ReEnter")

        self.URL = QtWidgets.QLabel(self.centralwidget)
        self.URL.setGeometry(QtCore.QRect(270, 140, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.URL.setFont(font)
        self.URL.setObjectName("URL")

        self.AA = QtWidgets.QLabel(self.centralwidget)
        self.AA.setGeometry(QtCore.QRect(270, 170, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AA.setFont(font)
        self.AA.setObjectName("AA")

        self.APW = QtWidgets.QLabel(self.centralwidget)
        self.APW.setGeometry(QtCore.QRect(270, 190, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.APW.setFont(font)
        self.APW.setObjectName("APW")

        self.VA = QtWidgets.QLabel(self.centralwidget)
        self.VA.setGeometry(QtCore.QRect(270, 280, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VA.setFont(font)
        self.VA.setObjectName("VA")

        self.VRP = QtWidgets.QLabel(self.centralwidget)
        self.VRP.setGeometry(QtCore.QRect(270, 340, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VRP.setFont(font)
        self.VRP.setObjectName("VRP")

        self.VPW = QtWidgets.QLabel(self.centralwidget)
        self.VPW.setGeometry(QtCore.QRect(270, 300, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VPW.setFont(font)
        self.VPW.setObjectName("VPW")

        self.ARP = QtWidgets.QLabel(self.centralwidget)
        self.ARP.setGeometry(QtCore.QRect(270, 230, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ARP.setFont(font)
        self.ARP.setObjectName("ARP")


        #programmable parameters
        #input 'spinnerBox' to allow only numbers with a set range and increment

        self.LRLInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.LRLInput.setGeometry(QtCore.QRect(420, 120, 62, 22))
        self.LRLInput.setDecimals(0)
        self.LRLInput.setMinimum(30.0)
        self.LRLInput.setMaximum(175.0)
        self.LRLInput.setProperty("value", 60.0)
        self.LRLInput.setObjectName("LRLInput")
        self.URLInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.URLInput.setGeometry(QtCore.QRect(420, 140, 62, 22))
        self.URLInput.setDecimals(0)
        self.URLInput.setMinimum(50.0)
        self.URLInput.setMaximum(175.0)
        self.URLInput.setSingleStep(5.0)
        self.URLInput.setProperty("value", 120.0)
        self.URLInput.setObjectName("URLInput")
        self.AAInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.AAInput.setGeometry(QtCore.QRect(420, 170, 62, 22))
        self.AAInput.setDecimals(1)
        self.AAInput.setMinimum(0.1)
        self.AAInput.setMaximum(5.0)
        self.AAInput.setSingleStep(0.1)
        self.AAInput.setProperty("value", 3.0)
        self.AAInput.setObjectName("AAInput")
        self.APWInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.APWInput.setGeometry(QtCore.QRect(420, 190, 62, 22))
        self.APWInput.setDecimals(0)
        self.APWInput.setMinimum(1.0)
        self.APWInput.setMaximum(30.0)
        self.APWInput.setSingleStep(1.0)
        self.APWInput.setProperty("value", 30.0)
        self.APWInput.setObjectName("APWInput")
        self.VAInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.VAInput.setGeometry(QtCore.QRect(420, 280, 62, 22))
        self.VAInput.setDecimals(1)
        self.VAInput.setMinimum(0.1)
        self.VAInput.setMaximum(5.0)
        self.VAInput.setSingleStep(0.1)
        self.VAInput.setProperty("value", 3.0)
        self.VAInput.setObjectName("VAInput")
        self.VPWInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.VPWInput.setGeometry(QtCore.QRect(420, 300, 62, 22))
        self.VPWInput.setDecimals(0)
        self.VPWInput.setMinimum(1.0)
        self.VPWInput.setMaximum(30.0)
        self.VPWInput.setSingleStep(1.0)
        self.VPWInput.setProperty("value", 30.0)
        self.VPWInput.setObjectName("VPWInput")
        self.VRPInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.VRPInput.setGeometry(QtCore.QRect(420, 340, 62, 22))
        self.VRPInput.setDecimals(0)
        self.VRPInput.setMinimum(150.0)
        self.VRPInput.setMaximum(500.0)
        self.VRPInput.setSingleStep(10.0)
        self.VRPInput.setProperty("value", 320.0)
        self.VRPInput.setObjectName("VRPInput")
        self.ARPInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ARPInput.setGeometry(QtCore.QRect(420, 230, 62, 22))
        self.ARPInput.setDecimals(0)
        self.ARPInput.setMinimum(150.0)
        self.ARPInput.setMaximum(500.0)
        self.ARPInput.setSingleStep(10.0)
        self.ARPInput.setProperty("value", 250.0)
        self.ARPInput.setObjectName("ARPInput")


        #output

        self.LRLOutput = QtWidgets.QLabel(self.centralwidget)
        self.LRLOutput.setGeometry(QtCore.QRect(520, 120, 81, 16))
        self.LRLOutput.setObjectName("LRLOutput")
        self.URLOutput = QtWidgets.QLabel(self.centralwidget)
        self.URLOutput.setGeometry(QtCore.QRect(520, 140, 81, 16))
        self.URLOutput.setObjectName("URLOutput")
        self.APWOutput = QtWidgets.QLabel(self.centralwidget)
        self.APWOutput.setGeometry(QtCore.QRect(520, 190, 81, 16))
        self.APWOutput.setObjectName("APWOutput")
        self.AAOutput = QtWidgets.QLabel(self.centralwidget)
        self.AAOutput.setGeometry(QtCore.QRect(520, 170, 81, 16))
        self.AAOutput.setObjectName("AAOutput")
        self.VAOutput = QtWidgets.QLabel(self.centralwidget)
        self.VAOutput.setGeometry(QtCore.QRect(520, 280, 81, 16))
        self.VAOutput.setObjectName("VAOutput")
        self.ARPOutput = QtWidgets.QLabel(self.centralwidget)
        self.ARPOutput.setGeometry(QtCore.QRect(520, 230, 81, 16))
        self.ARPOutput.setObjectName("ARPOutput")
        self.VPWOutput = QtWidgets.QLabel(self.centralwidget)
        self.VPWOutput.setGeometry(QtCore.QRect(520, 300, 81, 16))
        self.VPWOutput.setObjectName("VPWOutput")
        self.VRPOutput = QtWidgets.QLabel(self.centralwidget)
        self.VRPOutput.setGeometry(QtCore.QRect(520, 340, 81, 16))
        self.VRPOutput.setObjectName("VRPOutput")

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(250, 80, 20, 501))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.DifferentPacemaker = QtWidgets.QLabel(self.centralwidget)
        self.DifferentPacemaker.setGeometry(QtCore.QRect(20, 450, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DifferentPacemaker.setFont(font)
        self.DifferentPacemaker.setObjectName("DifferentPacemaker")

        #different pacemaker output

        self.DifferentPacemakerOutput = QtWidgets.QLabel(self.centralwidget)
        self.DifferentPacemakerOutput.setGeometry(QtCore.QRect(60, 480, 71, 21))
        self.DifferentPacemakerOutput.setObjectName("DifferentPacemakerOutput")

        #mode input buttons

        self.NO = QtWidgets.QPushButton(self.centralwidget)
        self.NO.setGeometry(QtCore.QRect(80, 90, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.NO.setFont(font)
        self.NO.setObjectName("NO")

        self.NO.clicked.connect(self.NOClicked)

        self.AOO = QtWidgets.QPushButton(self.centralwidget)
        self.AOO.setGeometry(QtCore.QRect(20, 120, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AOO.setFont(font)
        self.AOO.setObjectName("AOO")

        self.AOO.clicked.connect(self.AOOClicked)

        self.VOO = QtWidgets.QPushButton(self.centralwidget)
        self.VOO.setGeometry(QtCore.QRect(100, 120, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.VOO.setFont(font)
        self.VOO.setObjectName("VOO")

        self.VOO.clicked.connect(self.VOOClicked)

        self.DOO = QtWidgets.QPushButton(self.centralwidget)
        self.DOO.setGeometry(QtCore.QRect(180, 120, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DOO.setFont(font)
        self.DOO.setObjectName("DOO")

        self.DOO.clicked.connect(self.DOOClicked)

        self.AAI = QtWidgets.QPushButton(self.centralwidget)
        self.AAI.setGeometry(QtCore.QRect(20, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AAI.setFont(font)
        self.AAI.setObjectName("AAI")

        self.AAI.clicked.connect(self.AAIClicked)

        self.VVI = QtWidgets.QPushButton(self.centralwidget)
        self.VVI.setGeometry(QtCore.QRect(100, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.VVI.setFont(font)
        self.VVI.setObjectName("VVI")

        self.VVI.clicked.connect(self.VVIClicked)

        self.DOOR = QtWidgets.QPushButton(self.centralwidget)
        self.DOOR.setGeometry(QtCore.QRect(180, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DOOR.setFont(font)
        self.DOOR.setObjectName("DOOR")

        self.DOOR.clicked.connect(self.DOORClicked)

        self.AOOR = QtWidgets.QPushButton(self.centralwidget)
        self.AOOR.setGeometry(QtCore.QRect(20, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AOOR.setFont(font)
        self.AOOR.setObjectName("AOOR")

        self.AOOR.clicked.connect(self.AOORClicked)

        self.VOOR = QtWidgets.QPushButton(self.centralwidget)
        self.VOOR.setGeometry(QtCore.QRect(100, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.VOOR.setFont(font)
        self.VOOR.setObjectName("VOOR")

        self.VOOR.clicked.connect(self.VOORClicked)

        self.DDDR = QtWidgets.QPushButton(self.centralwidget)
        self.DDDR.setGeometry(QtCore.QRect(180, 210, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DDDR.setFont(font)
        self.DDDR.setObjectName("DDDR")

        self.DDDR.clicked.connect(self.DDDRClicked)

        self.AAIR = QtWidgets.QPushButton(self.centralwidget)
        self.AAIR.setGeometry(QtCore.QRect(20, 210, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AAIR.setFont(font)
        self.AAIR.setObjectName("AAIR")

        self.AAIR.clicked.connect(self.AAIRClicked)

        self.VVIR = QtWidgets.QPushButton(self.centralwidget)
        self.VVIR.setGeometry(QtCore.QRect(100, 210, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.VVIR.setFont(font)
        self.VVIR.setObjectName("VVIR")

        self.VVIR.clicked.connect(self.VVIRClicked)

        #Leave button switches pages to login menu & logs off user

        self.Leave = QtWidgets.QPushButton(self.centralwidget)
        self.Leave.setGeometry(QtCore.QRect(420, 50, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Leave.setFont(font)
        self.Leave.setObjectName("Leave")

        self.Leave.clicked.connect(self.LeaveClicked)

        self.CurrentMode_2 = QtWidgets.QLabel(self.centralwidget)
        self.CurrentMode_2.setGeometry(QtCore.QRect(20, 250, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CurrentMode_2.setFont(font)
        self.CurrentMode_2.setObjectName("CurrentMode_2")

        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 570, 591, 41))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        #load parameters button

        self.Load = QtWidgets.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(420, 90, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Load.setFont(font)
        self.Load.setObjectName("Load")

        #inputs variable data into text box

        self.Load.clicked.connect(self.LoadClicked)

        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(600, 80, 20, 501))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(20, 360, 241, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(500, 40, 21, 41))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")

        self.Current = QtWidgets.QLabel(self.centralwidget)
        self.Current.setGeometry(QtCore.QRect(520, 100, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Current.setFont(font)
        self.Current.setObjectName("Current")

        #self.line_12 = QtWidgets.QFrame(self.centralwidget)
        #self.line_12.setGeometry(QtCore.QRect(403, 40, 16, 41))
        #self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        #self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.line_12.setObjectName("line_12")


        self.AS = QtWidgets.QLabel(self.centralwidget)
        self.AS.setGeometry(QtCore.QRect(270, 210, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AS.setFont(font)
        self.AS.setObjectName("AS")

        self.ASOutput = QtWidgets.QLabel(self.centralwidget)
        self.ASOutput.setGeometry(QtCore.QRect(520, 210, 81, 16))
        self.ASOutput.setObjectName("ASOutput")

        self.ASInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ASInput.setGeometry(QtCore.QRect(420, 210, 62, 22))
        self.ASInput.setDecimals(1)
        self.ASInput.setMinimum(0.0)
        self.ASInput.setMaximum(5.0)
        self.ASInput.setSingleStep(0.1)
        self.ASInput.setProperty("value", 0.0)
        self.ASInput.setObjectName("ASInput")

        self.VS = QtWidgets.QLabel(self.centralwidget)
        self.VS.setGeometry(QtCore.QRect(270, 320, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VS.setFont(font)
        self.VS.setObjectName("VS")

        self.VSOutput = QtWidgets.QLabel(self.centralwidget)
        self.VSOutput.setGeometry(QtCore.QRect(520, 320, 81, 16))
        self.VSOutput.setObjectName("VSOutput")

        self.VSInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.VSInput.setGeometry(QtCore.QRect(420, 320, 62, 22))
        self.VSInput.setDecimals(1)
        self.VSInput.setMinimum(0.0)
        self.VSInput.setMaximum(5.0)
        self.VSInput.setSingleStep(0.1)
        self.VSInput.setProperty("value", 0.0)
        self.VSInput.setObjectName("VSInput")

        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(20, 280, 241, 21))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")

        #display graph button

        self.DisplayGraph = QtWidgets.QPushButton(self.centralwidget)
        self.DisplayGraph.setGeometry(QtCore.QRect(60, 310, 161, 41))
        self.DisplayGraph.setObjectName("DisplayGraph")

        self.DisplayGraph.clicked.connect(self.DisplayGraphClicked)

        self.AThreshold = QtWidgets.QLabel(self.centralwidget)
        self.AThreshold.setGeometry(QtCore.QRect(270, 250, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AThreshold.setFont(font)
        self.AThreshold.setObjectName("AThreshold")

        self.AThresholdOutput = QtWidgets.QLabel(self.centralwidget)
        self.AThresholdOutput.setGeometry(QtCore.QRect(520, 250, 81, 16))
        self.AThresholdOutput.setObjectName("AThresholdOutput")

        self.AThresholdInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.AThresholdInput.setGeometry(QtCore.QRect(420, 250, 62, 22))
        self.AThresholdInput.setDecimals(2)
        self.AThresholdInput.setMinimum(0.5)
        self.AThresholdInput.setMaximum(3.3)
        self.AThresholdInput.setSingleStep(0.1)
        self.AThresholdInput.setProperty("value", 2.75)
        self.AThresholdInput.setObjectName("AThresholdInput")

        self.VThresholdInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.VThresholdInput.setGeometry(QtCore.QRect(420, 360, 62, 22))
        self.VThresholdInput.setDecimals(2)
        self.VThresholdInput.setMinimum(0.5)
        self.VThresholdInput.setMaximum(3.3)
        self.VThresholdInput.setSingleStep(0.1)
        self.VThresholdInput.setProperty("value", 2.75)
        self.VThresholdInput.setObjectName("VThresholdInput")

        self.VThreshold = QtWidgets.QLabel(self.centralwidget)
        self.VThreshold.setGeometry(QtCore.QRect(270, 360, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VThreshold.setFont(font)
        self.VThreshold.setObjectName("VThreshold")

        self.VThresholdOutput = QtWidgets.QLabel(self.centralwidget)
        self.VThresholdOutput.setGeometry(QtCore.QRect(520, 360, 81, 16))
        self.VThresholdOutput.setObjectName("VThresholdOutput")

        self.AVDelay = QtWidgets.QLabel(self.centralwidget)
        self.AVDelay.setGeometry(QtCore.QRect(270, 390, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AVDelay.setFont(font)
        self.AVDelay.setObjectName("AVDelay")

        self.AVDelayInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.AVDelayInput.setGeometry(QtCore.QRect(420, 390, 62, 22))
        self.AVDelayInput.setDecimals(0)
        self.AVDelayInput.setMinimum(70.0)
        self.AVDelayInput.setMaximum(300.0)
        self.AVDelayInput.setSingleStep(5.0)
        self.AVDelayInput.setProperty("value", 150.0)
        self.AVDelayInput.setObjectName("AVDelayInput")

        self.AVDelayOutput = QtWidgets.QLabel(self.centralwidget)
        self.AVDelayOutput.setGeometry(QtCore.QRect(520, 390, 81, 16))
        self.AVDelayOutput.setObjectName("AVDelayOutput")

        self.ReactionTime = QtWidgets.QLabel(self.centralwidget)
        self.ReactionTime.setGeometry(QtCore.QRect(270, 410, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ReactionTime.setFont(font)
        self.ReactionTime.setObjectName("ReactionTime")

        self.ReactionTimeInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ReactionTimeInput.setGeometry(QtCore.QRect(420, 410, 62, 22))
        self.ReactionTimeInput.setDecimals(0)
        self.ReactionTimeInput.setMinimum(1.0)
        self.ReactionTimeInput.setMaximum(30.0)
        self.ReactionTimeInput.setSingleStep(1.0)
        self.ReactionTimeInput.setProperty("value", 4.0)
        self.ReactionTimeInput.setObjectName("ReactionTimeInput")

        self.ReactionTimeOutput = QtWidgets.QLabel(self.centralwidget)
        self.ReactionTimeOutput.setGeometry(QtCore.QRect(520, 410, 81, 16))
        self.ReactionTimeOutput.setObjectName("ReactionTimeOutput")

        self.RecoveryTime = QtWidgets.QLabel(self.centralwidget)
        self.RecoveryTime.setGeometry(QtCore.QRect(270, 430, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RecoveryTime.setFont(font)
        self.RecoveryTime.setObjectName("RecoveryTime")

        self.RecoveryTimeInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.RecoveryTimeInput.setGeometry(QtCore.QRect(420, 430, 62, 22))
        self.RecoveryTimeInput.setDecimals(0)
        self.RecoveryTimeInput.setMinimum(5.0)
        self.RecoveryTimeInput.setMaximum(30.0)
        self.RecoveryTimeInput.setSingleStep(1.0)
        self.RecoveryTimeInput.setProperty("value", 10.0)
        self.RecoveryTimeInput.setObjectName("RecoveryTimeInput")

        self.RecoveryTimeOutput = QtWidgets.QLabel(self.centralwidget)
        self.RecoveryTimeOutput.setGeometry(QtCore.QRect(520, 430, 81, 16))
        self.RecoveryTimeOutput.setObjectName("RecoveryTimeOutput")

        self.ResponseFactorOutput = QtWidgets.QLabel(self.centralwidget)
        self.ResponseFactorOutput.setGeometry(QtCore.QRect(520, 450, 81, 16))
        self.ResponseFactorOutput.setObjectName("ResponseFactorOutput")

        self.ResponseFactorInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ResponseFactorInput.setGeometry(QtCore.QRect(420, 450, 62, 22))
        self.ResponseFactorInput.setDecimals(0)
        self.ResponseFactorInput.setMinimum(1.0)
        self.ResponseFactorInput.setMaximum(16.0)
        self.ResponseFactorInput.setSingleStep(1.0)
        self.ResponseFactorInput.setProperty("value", 8.0)
        self.ResponseFactorInput.setObjectName("ResponseFactorInput")

        self.ResponseFactor = QtWidgets.QLabel(self.centralwidget)
        self.ResponseFactor.setGeometry(QtCore.QRect(270, 450, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ResponseFactor.setFont(font)
        self.ResponseFactor.setObjectName("ResponseFactor")

        self.ActivityThresholdOutput = QtWidgets.QLabel(self.centralwidget)
        self.ActivityThresholdOutput.setGeometry(QtCore.QRect(520, 470, 81, 16))
        self.ActivityThresholdOutput.setObjectName("ActivityThresholdOutput")

        self.ActivityThresholdInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ActivityThresholdInput.setGeometry(QtCore.QRect(420, 470, 62, 22))
        self.ActivityThresholdInput.setDecimals(1)
        self.ActivityThresholdInput.setMinimum(1.0)
        self.ActivityThresholdInput.setMaximum(4.0)
        self.ActivityThresholdInput.setSingleStep(0.5)
        self.ActivityThresholdInput.setProperty("value", 2.0)
        self.ActivityThresholdInput.setObjectName("ActivityThresholdInput")

        self.ActivityThreshold = QtWidgets.QLabel(self.centralwidget)
        self.ActivityThreshold.setGeometry(QtCore.QRect(270, 470, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ActivityThreshold.setFont(font)
        self.ActivityThreshold.setObjectName("ActivityThreshold")

        self.MaxSensorOutput = QtWidgets.QLabel(self.centralwidget)
        self.MaxSensorOutput.setGeometry(QtCore.QRect(520, 490, 81, 16))
        self.MaxSensorOutput.setObjectName("MaxSensorOutput")

        self.MaxSensorInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.MaxSensorInput.setGeometry(QtCore.QRect(420, 490, 62, 22))
        self.MaxSensorInput.setDecimals(0)
        self.MaxSensorInput.setMinimum(50.0)
        self.MaxSensorInput.setMaximum(175.0)
        self.MaxSensorInput.setSingleStep(5.0)
        self.MaxSensorInput.setProperty("value", 120.0)
        self.MaxSensorInput.setObjectName("MaxSensorInput")

        self.MaxSensor = QtWidgets.QLabel(self.centralwidget)
        self.MaxSensor.setGeometry(QtCore.QRect(270, 490, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MaxSensor.setFont(font)
        self.MaxSensor.setObjectName("MaxSensor")

        self.PVARPExtensionInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.PVARPExtensionInput.setGeometry(QtCore.QRect(420, 550, 62, 22))
        self.PVARPExtensionInput.setDecimals(0)
        self.PVARPExtensionInput.setMinimum(150.0)
        self.PVARPExtensionInput.setMaximum(500.0)
        self.PVARPExtensionInput.setSingleStep(5.0)
        self.PVARPExtensionInput.setProperty("value", 150.0)
        self.PVARPExtensionInput.setObjectName("PVARPExtensionInput")

        self.PVARPExtension = QtWidgets.QLabel(self.centralwidget)
        self.PVARPExtension.setGeometry(QtCore.QRect(270, 550, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PVARPExtension.setFont(font)
        self.PVARPExtension.setObjectName("PVARPExtension")

        self.RateSmooth = QtWidgets.QLabel(self.centralwidget)
        self.RateSmooth.setGeometry(QtCore.QRect(270, 510, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RateSmooth.setFont(font)
        self.RateSmooth.setObjectName("RateSmooth")

        self.PVARPOutput = QtWidgets.QLabel(self.centralwidget)
        self.PVARPOutput.setGeometry(QtCore.QRect(520, 530, 81, 16))
        self.PVARPOutput.setObjectName("PVARPOutput")

        self.RateSmoothInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.RateSmoothInput.setGeometry(QtCore.QRect(420, 510, 62, 22))
        self.RateSmoothInput.setDecimals(0)
        self.RateSmoothInput.setMinimum(0.0)
        self.RateSmoothInput.setMaximum(25.0)
        self.RateSmoothInput.setSingleStep(1.0)
        self.RateSmoothInput.setProperty("value", 0.0)
        self.RateSmoothInput.setObjectName("RateSmoothInput")

        self.RateSmoothOutput = QtWidgets.QLabel(self.centralwidget)
        self.RateSmoothOutput.setGeometry(QtCore.QRect(520, 510, 81, 16))
        self.RateSmoothOutput.setObjectName("RateSmoothOutput")

        self.PVARPInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.PVARPInput.setGeometry(QtCore.QRect(420, 530, 62, 22))
        self.PVARPInput.setDecimals(0)
        self.PVARPInput.setMinimum(150.0)
        self.PVARPInput.setMaximum(500.0)
        self.PVARPInput.setSingleStep(5.0)
        self.PVARPInput.setProperty("value", 150.0)
        self.PVARPInput.setObjectName("PVARPInput")

        self.PVARP = QtWidgets.QLabel(self.centralwidget)
        self.PVARP.setGeometry(QtCore.QRect(270, 530, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PVARP.setFont(font)
        self.PVARP.setObjectName("PVARP")

        self.PVARPExtensionOutput = QtWidgets.QLabel(self.centralwidget)
        self.PVARPExtensionOutput.setGeometry(QtCore.QRect(520, 550, 81, 16))
        self.PVARPExtensionOutput.setObjectName("PVARPExtensionOutput")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiMainWindow(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #2nd stage password & username verification

        self.PasswordLoad = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordLoad.setGeometry(QtCore.QRect(270, 100, 131, 20))
        self.PasswordLoad.setObjectName("PasswordLoad")

        self.UsernameLoad = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameLoad.setGeometry(QtCore.QRect(270, 80, 131, 20))
        self.UsernameLoad.setObjectName("UsernameLoad")

        #self.LoginOutput.setText(Ui_LoginWindow.user_name)

    #made by QT Designer, changes texts boxes to new value

    def retranslateUiMainWindow(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pace Maker User Interface"))
        self.Welcome.setText(_translate("MainWindow", "Welcome to PaceMaker Pro: MAIN MENU"))
        self.LoginOutput.setText(_translate("MainWindow", ""))
        self.Mode.setText(_translate("MainWindow", "Mode:"))
        self.DeviceCommunicate.setText(_translate("MainWindow", "DCM and Device comunitating:"))
        self.DeviceCommunicateOutput.setText(_translate("MainWindow", "False"))
        self.ModeOutput.setText(_translate("MainWindow", "No Mode Selected"))
        self.User.setText(_translate("MainWindow", "CURRENT USER:"))
        self.LRL.setText(_translate("MainWindow", "Lower Rate Limit:"))
        self.ReEnter.setText(_translate("MainWindow", "Re-enter User & Pass:"))
        self.URL.setText(_translate("MainWindow", "Upper Rate Limit:"))
        self.AA.setText(_translate("MainWindow", "Atrial Amplitude:"))
        self.APW.setText(_translate("MainWindow", "Atrial Pules Width:"))
        self.VA.setText(_translate("MainWindow", "Ventricular Amplitude:"))
        self.VRP.setText(_translate("MainWindow", "VRP:"))
        self.VPW.setText(_translate("MainWindow", "Ventrical Pulse Width:"))
        self.ARP.setText(_translate("MainWindow", "ARP:"))
        self.LRLOutput.setText(_translate("MainWindow", ""))
        self.URLOutput.setText(_translate("MainWindow", ""))
        self.APWOutput.setText(_translate("MainWindow", ""))
        self.AAOutput.setText(_translate("MainWindow", ""))
        self.VAOutput.setText(_translate("MainWindow", ""))
        self.ARPOutput.setText(_translate("MainWindow", ""))
        self.VPWOutput.setText(_translate("MainWindow", ""))
        self.VRPOutput.setText(_translate("MainWindow", ""))
        self.DifferentPacemaker.setText(_translate("MainWindow", "A different Pacemaker is approached:"))
        self.DifferentPacemakerOutput.setText(_translate("MainWindow", "False"))
        self.NO.setText(_translate("MainWindow", "NO MODE"))
        self.AOO.setText(_translate("MainWindow", "AOO"))
        self.VOO.setText(_translate("MainWindow", "VOO"))
        self.DOO.setText(_translate("MainWindow", "DOO"))
        self.AAI.setText(_translate("MainWindow", "AAI"))
        self.DOOR.setText(_translate("MainWindow", "DOOR"))
        self.VVI.setText(_translate("MainWindow", "VVI"))
        self.AOOR.setText(_translate("MainWindow", "AOOR"))
        self.DDDR.setText(_translate("MainWindow", "DDDR"))
        self.VOOR.setText(_translate("MainWindow", "VOOR"))
        self.AAIR.setText(_translate("MainWindow", "AAIR"))
        self.VVIR.setText(_translate("MainWindow", "VVIR"))
        self.CurrentMode_2.setText(_translate("MainWindow", "Current Mode:"))
        self.Load.setText(_translate("MainWindow", "Load"))
        self.Current.setText(_translate("MainWindow", "Current:"))
        self.Leave.setText(_translate("MainWindow", "Leave"))
        self.AS.setText(_translate("MainWindow", "Atrial Sensitivity:"))
        self.ASOutput.setText(_translate("MainWindow", ""))
        self.VS.setText(_translate("MainWindow", "Ventrical Sensitivity:"))
        self.VSOutput.setText(_translate("MainWindow", ""))
        self.DisplayGraph.setText(_translate("MainWindow", "Display Electrogram"))
        self.AThreshold.setText(_translate("MainWindow", "Atrial Sense Threshold:"))
        self.AThresholdOutput.setText(_translate("MainWindow", ""))
        self.VThreshold.setText(_translate("MainWindow", "Vent Sense Threshold:"))
        self.VThresholdOutput.setText(_translate("MainWindow", ""))
        self.AVDelay.setText(_translate("MainWindow", "AV Delay:"))
        self.AVDelayOutput.setText(_translate("MainWindow", ""))
        self.ReactionTime.setText(_translate("MainWindow", "Reaction Time:"))
        self.ReactionTimeOutput.setText(_translate("MainWindow", ""))
        self.RecoveryTime.setText(_translate("MainWindow", "Recovery Time:"))
        self.RecoveryTimeOutput.setText(_translate("MainWindow", ""))
        self.ResponseFactorOutput.setText(_translate("MainWindow", ""))
        self.ResponseFactor.setText(_translate("MainWindow", "Response Factor:"))
        self.ActivityThresholdOutput.setText(_translate("MainWindow", ""))
        self.ActivityThreshold.setText(_translate("MainWindow", "Activity Threshold:"))
        self.MaxSensorOutput.setText(_translate("MainWindow", ""))
        self.MaxSensor.setText(_translate("MainWindow", "Max Sensor Rate (MSR):"))
        self.PVARPExtension.setText(_translate("MainWindow", "PVARP Extension:"))
        self.RateSmooth.setText(_translate("MainWindow", "Rate Smoothing:"))
        self.PVARPOutput.setText(_translate("MainWindow", ""))
        self.RateSmoothOutput.setText(_translate("MainWindow", ""))
        self.PVARP.setText(_translate("MainWindow", "PVARP:"))
        self.PVARPExtensionOutput.setText(_translate("MainWindow", ""))

    #updates ModeOutput box to say the code of each button when clicked
    def NOClicked(self):
        self.ModeOutput.setText("No Mode Selected")
        self.UpdateModeOutput()
    def AOOClicked(self):
        self.ModeOutput.setText("AOO")
        self.UpdateModeOutput()
    def VOOClicked(self):
        self.ModeOutput.setText("VOO")
        self.UpdateModeOutput()
    def DOOClicked(self):
        self.ModeOutput.setText("DOO")
        self.UpdateModeOutput()
    def AAIClicked(self):
        self.ModeOutput.setText("AAI")
        self.UpdateModeOutput()
    def VVIClicked(self):
        self.ModeOutput.setText("VVI")
        self.UpdateModeOutput()
    def DOORClicked(self):
        self.ModeOutput.setText("DOOR")
        self.UpdateModeOutput()
    def AOORClicked(self):
        self.ModeOutput.setText("AOOR")
        self.UpdateModeOutput()
    def VOORClicked(self):
        self.ModeOutput.setText("VOOR")
        self.UpdateModeOutput()
    def DDDRClicked(self):
        self.ModeOutput.setText("DDDR")
        self.UpdateModeOutput()
    def AAIRClicked(self):
        self.ModeOutput.setText("AAIR")
        self.UpdateModeOutput()
    def VVIRClicked(self):
        self.ModeOutput.setText("VVIR")
        self.UpdateModeOutput()

    #logs of and switches pages
    def LeaveClicked(self):
        MainWindow.hide()
        LoginWindow.show()

    #states graph and continues to display real time
    def DisplayGraphClicked(self):


        print("hello world")


    #reads file and saves locally in array form
    def GetFile(self):
        f=open("guru.txt", "r")
        GetArrray = [["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","","","","","",""]]

        for i in range (len(GetArrray)):
            read = f.readline()
            GetArrray[i] = read.split (" ")

        for i in range (len(GetArrray)):
            for j in range (len(GetArrray[i])):
                GetArrray[i][j] =  GetArrray[i][j].strip("\n")

        #for i in range (len(GetArrray)):
         #   GetArrray[i].remove("")
        f.close()
        return GetArrray

    #returns location of password for signed in user

    def PasswordLocation(self, Password):
        Array = self.GetFile()
        for i in range (len(Array)):
            for j in range (len(Array[i])):
            #for j in 23:
                if (Array [i][j]== Password):
                    print(i)
                    return i

    #returns password

    def GetPassword(self):
        password = self.PasswordLoad.text()
        return password

    # returns username

    def GetUsername(self):
        username = self.UsernameLoad.text()
        return username

    #checks if password and username are valid

    def CheckPassword(self, u1, p1):
        Array = self.GetFile()
        if (u1 == ""):
            return 0
        if (p1 == ""):
            return 0
        for i in range(len(Array)):
            if (Array [i][0] == u1):
                if (Array [i][1] == p1):
                    return 1
        return 0

    #returns row number of first empty row

    def CheckEmpty(self, Array):

        for i in range (len(Array)):
            if Array[i][0] == "":
                return i

    #rewrites array back into file

    def FileWrite(self, Array):
        f = open("guru.txt", "w")

        EmptyRow = self.CheckEmpty(Array)

        for i in range (EmptyRow):
            for j in range(len(Array[i])):
            #hellofor j in 23:
                f.write (Array[i][j] + " ")
            f.write ("\n")

        f.close()

    def GetMode(self):
        textmode = self.ModeOutput.text()
        if (textmode == "No Mode Selected"):
            return "0"
        elif (textmode == "AOO"):
            return "1"
        elif (textmode == "VOO"):
            return "2"
        elif (textmode == "AAI"):
            return "3"
        elif (textmode == "VVI"):
            return "4"
        elif (textmode == "DOO"):
            return "5"
        elif (textmode == "AOOR"):
            return "6"
        elif (textmode == "VOOR"):
            return "7"
        elif (textmode == "AAIR"):
            return "8"
        elif (textmode == "VVIR"):
            return "9"
        elif (textmode == "DOOR"):
            return "10"
        elif (textmode == "DDDR"):
            return "11"

    #code jumps here when user clicks load
    #checks if username and passwrd is right and then saves parameters into file
    def LoadClicked(self):

        UserPassword = self.GetPassword()
        UserUsername = self.GetUsername()

        #checks that password and username are valid
        if (self.CheckPassword(UserUsername,UserPassword) == 0):
            self.DataWrongPopUp()
            return


        self.LRLOutput.setText(self.LRLInput.text())
        self.URLOutput.setText(self.URLInput.text())
        self.AAOutput.setText(self.AAInput.text())
        self.APWOutput.setText(self.APWInput.text())
        self.ASOutput.setText(self.ASInput.text())
        self.ARPOutput.setText(self.ARPInput.text())
        self.AThresholdOutput.setText(self.AThresholdInput.text())
        self.VAOutput.setText(self.VAInput.text())
        self.VPWOutput.setText(self.VPWInput.text())
        self.VSOutput.setText(self.VSInput.text())
        self.VRPOutput.setText(self.VRPInput.text())
        self.VThresholdOutput.setText(self.VThresholdInput.text())
        self.AVDelayOutput.setText(self.AVDelayInput.text())
        self.ReactionTimeOutput.setText(self.ReactionTimeInput.text())
        self.RecoveryTimeOutput.setText(self.RecoveryTimeInput.text())
        self.ResponseFactorOutput.setText(self.ResponseFactorInput.text())
        self.ActivityThresholdOutput.setText(self.ActivityThresholdInput.text())
        self.MaxSensorOutput.setText(self.MaxSensorInput.text())
        self.RateSmoothOutput.setText(self.RateSmoothInput.text())
        self.PVARPOutput.setText(self.PVARPInput.text())
        self.PVARPExtensionOutput.setText(self.PVARPExtensionInput.text())

        lrl = self.LRLInput.text()
        url = self.URLInput.text()
        aa  =  self.AAInput.text()
        apw = self.APWInput.text()
        asense  =  self.ASInput.text()
        arp = self.ARPInput.text()
        ath = self.AThresholdInput.text()
        va  =  self.VAInput.text()
        vpw = self.VPWInput.text()
        vsense  =  self.VSInput.text()
        vrp = self.VRPInput.text()
        vth = self.VThresholdInput.text()
        avd  =  self.AVDelayInput.text()
        reaction  =  self.ReactionTimeInput.text()
        recovery  =  self.RecoveryTimeInput.text()
        response  =  self.ResponseFactorInput.text()
        activity  =  self.ActivityThresholdInput.text()
        ms  =  self.MaxSensorInput.text()
        rsmooth  =  self.RateSmoothInput.text()
        pvarp  =  self.PVARPInput.text()
        extension  =  self.PVARPExtensionInput.text()

        Array = self.GetFile()

        self.DataSavedPopUp()

        PassLocation = self.PasswordLocation(UserPassword)
        #we edit array to add the new parameters on the same line as password in array
        Array[PassLocation][2] = lrl
        Array[PassLocation][3] = url
        Array[PassLocation][4] = aa
        Array[PassLocation][5] = apw
        Array[PassLocation][6] = asense
        Array[PassLocation][7] = arp
        Array[PassLocation][8] = ath
        Array[PassLocation][9] = va
        Array[PassLocation][10] = vpw
        Array[PassLocation][11] = vsense
        Array[PassLocation][12] = vrp
        Array[PassLocation][13] = vth
        Array[PassLocation][14] = avd
        Array[PassLocation][15] = reaction
        Array[PassLocation][16] = recovery
        Array[PassLocation][17] = response
        Array[PassLocation][18] = activity
        Array[PassLocation][19] = ms
        Array[PassLocation][20] = rsmooth
        Array[PassLocation][21] = pvarp
        Array[PassLocation][22] = extension
        #Array[PassLocation][23] = "\n"

        #write everything back into file
        self.FileWrite(Array)

        #encode variables into bytes
        lrl = lrl.encode()
        url = url.encode()
        aa  =  aa.encode()
        apw = apw.encode()
        asense = asense.encode()
        arp = arp.encode()
        ath = ath.encode()
        va  =  va.encode()
        vpw = vpw.encode()
        vsense = vsense.encode()
        vrp = vrp.encode()
        vth = vth.encode()
        avd = avd.encode()
        reaction = reaction.encode()
        recovery = recovery.encode()
        response = response.encode()
        activity = activity.encode()
        ms  =  ms.encode()
        rsmooth = rsmooth.encode()
        pvarp = pvarp.encode()
        extension = extension.encode()

        #26 bytes being sent
        DataCheck = "23"
        DataCheck = DataCheck.encode()

        mode = self.GetMode()
        mode = mode.encode()
        #send serial information
        SerialArray = [mode,lrl,url,aa,va,apw,vpw,ath,vth,arp,vrp,asense,vsense,avd,reaction,recovery,response,activity,ms,rsmooth,pvarp,extension,DataCheck]
        print(SerialArray)

        ser.write(SerialArray)
        print("test 1")
        ser.write(SerialArray.encode())
        print("test 2")
        for i in SerialArray:
            ser.write(SerialArray[i])
        print("test 3")
        time.sleep(0.5)

    #error message when wrong password or username are entered
    def DataWrongPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Invalid User or Password")
        msg.setText("Sorry, Invalid Information Entered.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Please Enter Valid User Info.")
        x = msg.exec_()

    #message when password and username are right, and data saved in file
    def DataSavedPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("WELCOME")
        msg.setText("Data saved.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("file location 'guru.txt'.")
        x = msg.exec_()

    #adjusts szize of text boxs
    def UpdateModeOutput(self):
            self.ModeOutput.adjustSize()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    #login window start shown so user can login
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()

    #main window starts hiden until user logs in
    MainWindow = QtWidgets.QMainWindow()
    uiTwo = Ui_MainWindow()

    ui.setupUi(LoginWindow)
    uiTwo.setupUiTwo(MainWindow)

    LoginWindow.show()
    MainWindow.hide()

    sys.exit(app.exec_())
