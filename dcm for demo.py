from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QMainWindow
import sys



#first window to allow user to login and add user

class Ui_LoginWindow(object):
    
    def setupUi(self, LoginWindow):
        
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(456, 171)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        
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
        
        #username input
        
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
        
        #password input
        
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
        
        #self.user_name = "username"

    def retranslateUi1(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Pace Maker User Interface"))
        self.Welcome.setText(_translate("LoginWindow", "Welcome to PaceMaker Pro: LOGIN MENU"))
        self.UserName_2.setText(_translate("LoginWindow", "User Name:"))
        self.Password_2.setText(_translate("LoginWindow", "Password:"))
        self.Login.setText(_translate("LoginWindow", "LOGIN"))
        self.AddUser.setText(_translate("LoginWindow", "ADD USER (Max 10.)"))
    
    def fileWrite(self, w):
        f = open("guru.txt", "a+")
        for i in range (len(w)):
            for j in range(len(w[i])):
                f.write (w[i][j] + " ")
            f.write ("\n")
        f.close()
    
    def getFile(self):
        f=open("guru.txt", "r")
        getArray = [["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""]]

        for i in range (len(getArray)):
            read = f.readline()
            getArray[i] = read.split (" ")
    
        for i in range (len(getArray)):
            for j in range (len(getArray[i])):
                getArray[i][j] =  getArray[i][j].strip("\n")
    
        #for i in range (len(getArray)):
         #   getArray[i].remove("")
        f.close()  
        return getArray
    
    def checkPassword(self, u1,p1):
        cpArray = self.getFile()
        
        for i in range (len(cpArray)):
            for j in range (len(cpArray[i])):
                if (cpArray [i][j]== u1):
                    if(cpArray [i][j+1]==p1):
                        return 1
        return 0
    
    def LoginClicked(self):
        
        
        username = self.UserName.text()
        password = self.Password.text()
        #since user is existing, check whether password is correct
        if self.checkPassword(username, password):
            
            LoginWindow.hide()        
            MainWindow.show()
            
        else:
            self.LoginPopUp()
            
    
    def AddUserClicked(self):
        self.UserCounter += 1
        
        #array = [["Username","Password","LRL","URL","AA","APW","VA","VPW","VRP","ARP","PVART"]]
        
        username = self.UserName.text()
        password = self.Password.text()
        
        
        #if user is new, add to dictionary of users (if less than 10)
        if self.UserCounter <= 10:
            array = []
            array.append([username, password,"","","","","","","","",""])
            self.fileWrite(array)
            
            LoginWindow.hide()        
            MainWindow.show()
        
        else:
            self.AddUserPopUp()
    
    
    
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





#Second window for editing variables and modes after login

class Ui_MainWindow(Ui_LoginWindow):
    
    def setupUiTwo(self, MainWindow):
        
        
        #main window
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #welcome text
        
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
        self.line_5.setGeometry(QtCore.QRect(20, 31, 391, 20))
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
        self.DeviceCommunicate.setGeometry(QtCore.QRect(20, 320, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeviceCommunicate.setFont(font)
        self.DeviceCommunicate.setObjectName("DeviceCommunicate")
        
        #device communication output
        
        self.DeviceCommunicateOutput = QtWidgets.QLabel(self.centralwidget)
        self.DeviceCommunicateOutput.setGeometry(QtCore.QRect(200, 320, 71, 21))
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
        
        self.re_enter = QtWidgets.QLabel(self.centralwidget)
        self.re_enter.setGeometry(QtCore.QRect(250, 60, 200, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.re_enter.setFont(font)
        self.re_enter.setObjectName("re_enter")
        
        self.URL = QtWidgets.QLabel(self.centralwidget)
        self.URL.setGeometry(QtCore.QRect(270, 140, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.URL.setFont(font)
        self.URL.setObjectName("URL")
        
        self.AA = QtWidgets.QLabel(self.centralwidget)
        self.AA.setGeometry(QtCore.QRect(270, 160, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AA.setFont(font)
        self.AA.setObjectName("AA")
        
        self.APW = QtWidgets.QLabel(self.centralwidget)
        self.APW.setGeometry(QtCore.QRect(270, 180, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.APW.setFont(font)
        self.APW.setObjectName("APW")
        
        self.VA = QtWidgets.QLabel(self.centralwidget)
        self.VA.setGeometry(QtCore.QRect(270, 200, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VA.setFont(font)
        self.VA.setObjectName("VA")
        
        self.VRP = QtWidgets.QLabel(self.centralwidget)
        self.VRP.setGeometry(QtCore.QRect(270, 240, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VRP.setFont(font)
        self.VRP.setObjectName("VRP")
        
        self.VPW = QtWidgets.QLabel(self.centralwidget)
        self.VPW.setGeometry(QtCore.QRect(270, 220, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VPW.setFont(font)
        self.VPW.setObjectName("VPW")
        
        self.ARP = QtWidgets.QLabel(self.centralwidget)
        self.ARP.setGeometry(QtCore.QRect(270, 260, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ARP.setFont(font)
        self.ARP.setObjectName("ARP")
        
        self.PVART = QtWidgets.QLabel(self.centralwidget)
        self.PVART.setGeometry(QtCore.QRect(270, 280, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PVART.setFont(font)
        self.PVART.setObjectName("PVART")
        
        #programmable parameters
        
        #input
        
        self.LRLInput = QtWidgets.QLineEdit(self.centralwidget)
        self.LRLInput.setGeometry(QtCore.QRect(400, 120, 113, 20))
        self.LRLInput.setObjectName("LRLInput")
        self.URLInput = QtWidgets.QLineEdit(self.centralwidget)
        self.URLInput.setGeometry(QtCore.QRect(400, 140, 113, 20))
        self.URLInput.setObjectName("URLInput")
        self.APWInput = QtWidgets.QLineEdit(self.centralwidget)
        self.APWInput.setGeometry(QtCore.QRect(400, 180, 113, 20))
        self.APWInput.setObjectName("APWInput")
        self.AAInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AAInput.setGeometry(QtCore.QRect(400, 160, 113, 20))
        self.AAInput.setObjectName("AAInput")
        self.ARPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ARPInput.setGeometry(QtCore.QRect(400, 260, 113, 20))
        self.ARPInput.setObjectName("ARPInput")
        self.VAInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VAInput.setGeometry(QtCore.QRect(400, 200, 113, 20))
        self.VAInput.setObjectName("VAInput")
        self.VRPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VRPInput.setGeometry(QtCore.QRect(400, 240, 113, 20))
        self.VRPInput.setObjectName("VRPInput")
        self.VPWInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VPWInput.setGeometry(QtCore.QRect(400, 220, 113, 20))
        self.VPWInput.setObjectName("VPWInput")
        self.PVARTInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PVARTInput.setGeometry(QtCore.QRect(400, 280, 113, 20))
        self.PVARTInput.setObjectName("PVARTInput")
        
        #output
        
        self.LRLOutput = QtWidgets.QLabel(self.centralwidget)
        self.LRLOutput.setGeometry(QtCore.QRect(520, 120, 81, 16))
        self.LRLOutput.setObjectName("LRLOutput")
        self.URLOutput = QtWidgets.QLabel(self.centralwidget)
        self.URLOutput.setGeometry(QtCore.QRect(520, 140, 81, 16))
        self.URLOutput.setObjectName("URLOutput")
        self.APWOutput = QtWidgets.QLabel(self.centralwidget)
        self.APWOutput.setGeometry(QtCore.QRect(520, 180, 81, 16))
        self.APWOutput.setObjectName("APWOutput")
        self.AAOutput = QtWidgets.QLabel(self.centralwidget)
        self.AAOutput.setGeometry(QtCore.QRect(520, 160, 81, 16))
        self.AAOutput.setObjectName("AAOutput")
        self.VAOutput = QtWidgets.QLabel(self.centralwidget)
        self.VAOutput.setGeometry(QtCore.QRect(520, 200, 81, 16))
        self.VAOutput.setObjectName("VAOutput")
        self.ARPOutput = QtWidgets.QLabel(self.centralwidget)
        self.ARPOutput.setGeometry(QtCore.QRect(520, 260, 81, 16))
        self.ARPOutput.setObjectName("ARPOutput")
        self.VPWOutput = QtWidgets.QLabel(self.centralwidget)
        self.VPWOutput.setGeometry(QtCore.QRect(520, 220, 81, 16))
        self.VPWOutput.setObjectName("VPWOutput")
        self.VRPOutput = QtWidgets.QLabel(self.centralwidget)
        self.VRPOutput.setGeometry(QtCore.QRect(520, 240, 81, 16))
        self.VRPOutput.setObjectName("VRPOutput")
        self.PVARTOutput = QtWidgets.QLabel(self.centralwidget)
        self.PVARTOutput.setGeometry(QtCore.QRect(520, 280, 81, 16))
        self.PVARTOutput.setObjectName("PVARTOutput")
        
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(250, 80, 20, 231))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        
        self.DifferentPacemaker = QtWidgets.QLabel(self.centralwidget)
        self.DifferentPacemaker.setGeometry(QtCore.QRect(20, 350, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DifferentPacemaker.setFont(font)
        self.DifferentPacemaker.setObjectName("DifferentPacemaker")
        
        #different pacemaker output
        
        self.DifferentPacemakerOutput = QtWidgets.QLabel(self.centralwidget)
        self.DifferentPacemakerOutput.setGeometry(QtCore.QRect(240, 350, 71, 21))
        self.DifferentPacemakerOutput.setObjectName("DifferentPacemakerOutput")
        
        #mode input buttons
        
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
        self.DOOR.setGeometry(QtCore.QRect(180, 150, 75, 23))
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
        self.DDDR.setGeometry(QtCore.QRect(180, 180, 75, 23))
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
        
        self.VVIA = QtWidgets.QPushButton(self.centralwidget)
        self.VVIA.setGeometry(QtCore.QRect(100, 210, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.VVIA.setFont(font)
        self.VVIA.setObjectName("VVIA")
        
        self.VVIA.clicked.connect(self.VVIAClicked)
        
        #leave button switches pages to login menu & logs off user
        
        self.leave = QtWidgets.QPushButton(self.centralwidget)
        self.leave.setGeometry(QtCore.QRect(450, 50, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leave.setFont(font)
        self.leave.setObjectName("Leave")
        
        self.leave.clicked.connect(self.leaveClicked)
        
        
        self.CurrentMode_2 = QtWidgets.QLabel(self.centralwidget)
        self.CurrentMode_2.setGeometry(QtCore.QRect(20, 250, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CurrentMode_2.setFont(font)
        self.CurrentMode_2.setObjectName("CurrentMode_2")
        
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 290, 591, 41))
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
        self.line_9.setGeometry(QtCore.QRect(600, 80, 20, 231))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(20, 370, 321, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(330, 310, 21, 71))
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
        
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(403, 40, 16, 41))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUiMainWindow(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #2nd stage password verification
        
        self.PasswordLoad = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordLoad.setGeometry(QtCore.QRect(270, 100, 131, 20))
        self.PasswordLoad.setObjectName("PasswordLoad")
        
        self.UsernameLoad = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameLoad.setGeometry(QtCore.QRect(270, 80, 131, 20))
        self.UsernameLoad.setObjectName("UsernameLoad")
        
        #self.LoginOutput.setText(Ui_LoginWindow.user_name)
        
        
        
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
        self.re_enter.setText(_translate("MainWindow", "Re-enter User & Pass:"))
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
        self.VVIA.setText(_translate("MainWindow", "VVIA"))
        self.CurrentMode_2.setText(_translate("MainWindow", "Current Mode:"))
        self.Load.setText(_translate("MainWindow", "Load"))
        self.Current.setText(_translate("MainWindow", "Current:"))
        self.PVART.setText(_translate("MainWindow", "PVART:"))
        self.PVARTOutput.setText(_translate("MainWindow", ""))
        self.leave.setText(_translate("MainWindow", "leave"))
        
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
        
    def VVIAClicked(self):
        self.ModeOutput.setText("VVIA")
        self.UpdateModeOutput()
    
    def leaveClicked(self):
        MainWindow.hide()
        LoginWindow.show()
    
    def getFile(self):
        f=open("guru.txt", "r")
        getArray = [["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""],
                    ["","","","","","","","","","",""]]

        for i in range (len(getArray)):
            read = f.readline()
            getArray[i] = read.split (" ")
    
        for i in range (len(getArray)):
            for j in range (len(getArray[i])):
                getArray[i][j] =  getArray[i][j].strip("\n")
    
        for i in range (len(getArray)):
            getArray[i].remove("")
        f.close()  
        return getArray
    
    def passwordLocation(self, plPass):
        plArray = self.getFile()    
        for i in range (len(plArray)):
            for j in range (len(plArray[i])):
                if (plArray [i][j]== plPass):
                    return i
    
    def getPassword(self):
        password = self.PasswordLoad.text()
        return password

    def getUsername(self):
        username = self.UsernameLoad.text()
        return username
    
    def checkPassword(self,u1,p1):
        cpArray = self.getFile()
        
        for i in range (len(cpArray)):
            for j in range (len(cpArray[i])):
                if (cpArray [i][j]== u1):
                    if(cpArray [i][j+1]==p1):
                        return 1
        return 0
    
    def fileWrite(self, w):
        f = open("guru.txt", "w")
        for i in range (len(w)):
            for j in range(len(w[i])):
                f.write (w[i][j] + " ")
            f.write ("\n")
        f.close()
        
    def LoadClicked(self):
        self.LRLOutput.setText(self.LRLInput.text())
        self.URLOutput.setText(self.URLInput.text())
        self.AAOutput.setText(self.AAInput.text())
        self.APWOutput.setText(self.APWInput.text())
        self.VAOutput.setText(self.VAInput.text())
        self.VPWOutput.setText(self.VPWInput.text())
        self.VRPOutput.setText(self.VRPInput.text())
        self.ARPOutput.setText(self.ARPInput.text())
        self.PVARTOutput.setText(self.PVARTInput.text())
        
        lrl = self.LRLInput.text()
        url = self.URLInput.text()
        aa  =  self.AAInput.text()
        apw = self.APWInput.text()
        va  =  self.VAInput.text()
        vpw = self.VPWInput.text()
        vrp = self.VRPInput.text()
        arp = self.ARPInput.text()
        pvart = self.PVARTInput.text()
        
        array = self.getFile()
        check = 0
        while(check ==0):
            userPassword = self.getPassword()
            userUserName = self.getUsername()
            check = self.checkPassword(userUserName,userPassword)
            
        
        passLoca = self.passwordLocation(userPassword)
        
        array[passLoca][2] = lrl
        array[passLoca][3] = url
        array[passLoca][4] = aa
        array[passLoca][5] = apw
        array[passLoca][6] = va
        array[passLoca][7] = vpw
        array[passLoca][8] = vrp
        array[passLoca][9] = arp
        array[passLoca][10] = pvart
        
        self.fileWrite(array)
        
        
    
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

