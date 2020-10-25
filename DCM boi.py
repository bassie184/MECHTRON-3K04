# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
        
    #Setting up UI
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(9, 9, 393, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Welcome.setFont(font)
        self.Welcome.setObjectName("Welcome")
        self.UserName_2 = QtWidgets.QLabel(self.centralwidget)
        self.UserName_2.setGeometry(QtCore.QRect(9, 38, 64, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.UserName_2.setFont(font)
        self.UserName_2.setObjectName("UserName_2")
        self.UserName = QtWidgets.QLineEdit(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(90, 38, 191, 20))
        self.UserName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UserName.setObjectName("UserName")
        self.Password_2 = QtWidgets.QLabel(self.centralwidget)
        self.Password_2.setGeometry(QtCore.QRect(9, 64, 57, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Password_2.setFont(font)
        self.Password_2.setObjectName("Password_2")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(90, 64, 191, 20))
        self.Password.setObjectName("Password")
        
        
        # Login Button
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(9, 90, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        self.Login.clicked.connect(self.login_clicked)
        
        #Add User Button
        self.AddUser = QtWidgets.QPushButton(self.centralwidget)
        self.AddUser.setGeometry(QtCore.QRect(90, 90, 108, 23))
        self.AddUser.setObjectName("AddUser")
        # If Add User button clicked, will go to add_user_clicked function
        self.AddUser.clicked.connect(self.add_user_clicked)
            
        #Set up dictionary
        self.users = {}
        
        self.LoginOutput = QtWidgets.QLabel(self.centralwidget)
        self.LoginOutput.setGeometry(QtCore.QRect(310, 90, 191, 21))
        self.LoginOutput.setObjectName("LoginOutput")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 25, 441, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Mode = QtWidgets.QLabel(self.centralwidget)
        self.Mode.setGeometry(QtCore.QRect(30, 140, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Mode.setFont(font)
        self.Mode.setObjectName("Mode")
        self.DeviceCommunicate = QtWidgets.QLabel(self.centralwidget)
        self.DeviceCommunicate.setGeometry(QtCore.QRect(290, 40, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeviceCommunicate.setFont(font)
        self.DeviceCommunicate.setObjectName("DeviceCommunicate")
        self.DeviceCommunicateOutput = QtWidgets.QLabel(self.centralwidget)
        self.DeviceCommunicateOutput.setGeometry(QtCore.QRect(470, 40, 71, 21))
        self.DeviceCommunicateOutput.setObjectName("DeviceCommunicateOutput")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 110, 421, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ModeOutput = QtWidgets.QLabel(self.centralwidget)
        self.ModeOutput.setGeometry(QtCore.QRect(280, 140, 81, 16))
        self.ModeOutput.setObjectName("ModeOutput")
        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.setGeometry(QtCore.QRect(206, 90, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.User.setFont(font)
        self.User.setObjectName("User")
        self.LRL = QtWidgets.QLabel(self.centralwidget)
        self.LRL.setGeometry(QtCore.QRect(30, 160, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LRL.setFont(font)
        self.LRL.setObjectName("LRL")
        self.URL = QtWidgets.QLabel(self.centralwidget)
        self.URL.setGeometry(QtCore.QRect(30, 180, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.URL.setFont(font)
        self.URL.setObjectName("URL")
        self.AA = QtWidgets.QLabel(self.centralwidget)
        self.AA.setGeometry(QtCore.QRect(30, 200, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AA.setFont(font)
        self.AA.setObjectName("AA")
        self.APW = QtWidgets.QLabel(self.centralwidget)
        self.APW.setGeometry(QtCore.QRect(30, 220, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.APW.setFont(font)
        self.APW.setObjectName("APW")
        self.VA = QtWidgets.QLabel(self.centralwidget)
        self.VA.setGeometry(QtCore.QRect(30, 240, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VA.setFont(font)
        self.VA.setObjectName("VA")
        self.VRP = QtWidgets.QLabel(self.centralwidget)
        self.VRP.setGeometry(QtCore.QRect(30, 280, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VRP.setFont(font)
        self.VRP.setObjectName("VRP")
        self.VPW = QtWidgets.QLabel(self.centralwidget)
        self.VPW.setGeometry(QtCore.QRect(30, 260, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VPW.setFont(font)
        self.VPW.setObjectName("VPW")
        self.ARP = QtWidgets.QLabel(self.centralwidget)
        self.ARP.setGeometry(QtCore.QRect(30, 300, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ARP.setFont(font)
        self.ARP.setObjectName("ARP")
        self.LRLInput = QtWidgets.QLineEdit(self.centralwidget)
        self.LRLInput.setGeometry(QtCore.QRect(160, 160, 113, 20))
        self.LRLInput.setObjectName("LRLInput")
        self.URLInput = QtWidgets.QLineEdit(self.centralwidget)
        self.URLInput.setGeometry(QtCore.QRect(160, 180, 113, 20))
        self.URLInput.setObjectName("URLInput")
        self.APWInput = QtWidgets.QLineEdit(self.centralwidget)
        self.APWInput.setGeometry(QtCore.QRect(160, 220, 113, 20))
        self.APWInput.setObjectName("APWInput")
        self.AAInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AAInput.setGeometry(QtCore.QRect(160, 200, 113, 20))
        self.AAInput.setObjectName("AAInput")
        self.ARPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ARPInput.setGeometry(QtCore.QRect(160, 300, 113, 20))
        self.ARPInput.setObjectName("ARPInput")
        self.VAInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VAInput.setGeometry(QtCore.QRect(160, 240, 113, 20))
        self.VAInput.setObjectName("VAInput")
        self.VRPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VRPInput.setGeometry(QtCore.QRect(160, 280, 113, 20))
        self.VRPInput.setObjectName("VRPInput")
        self.VPWInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VPWInput.setGeometry(QtCore.QRect(160, 260, 113, 20))
        self.VPWInput.setObjectName("VPWInput")
        self.LRLOutput = QtWidgets.QLabel(self.centralwidget)
        self.LRLOutput.setGeometry(QtCore.QRect(280, 160, 81, 16))
        self.LRLOutput.setObjectName("LRLOutput")
        self.URLOutput = QtWidgets.QLabel(self.centralwidget)
        self.URLOutput.setGeometry(QtCore.QRect(280, 180, 81, 16))
        self.URLOutput.setObjectName("URLOutput")
        self.APWOutput = QtWidgets.QLabel(self.centralwidget)
        self.APWOutput.setGeometry(QtCore.QRect(280, 220, 81, 16))
        self.APWOutput.setObjectName("APWOutput")
        self.AAOutput = QtWidgets.QLabel(self.centralwidget)
        self.AAOutput.setGeometry(QtCore.QRect(280, 200, 81, 16))
        self.AAOutput.setObjectName("AAOutput")
        self.VAOutput = QtWidgets.QLabel(self.centralwidget)
        self.VAOutput.setGeometry(QtCore.QRect(280, 240, 81, 16))
        self.VAOutput.setObjectName("VAOutput")
        self.ARPOutput = QtWidgets.QLabel(self.centralwidget)
        self.ARPOutput.setGeometry(QtCore.QRect(280, 300, 81, 16))
        self.ARPOutput.setObjectName("ARPOutput")
        self.VPWOutput = QtWidgets.QLabel(self.centralwidget)
        self.VPWOutput.setGeometry(QtCore.QRect(280, 260, 81, 16))
        self.VPWOutput.setObjectName("VPWOutput")
        self.VRPOutput = QtWidgets.QLabel(self.centralwidget)
        self.VRPOutput.setGeometry(QtCore.QRect(280, 280, 81, 16))
        self.VRPOutput.setObjectName("VRPOutput")
        self.ModeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ModeInput.setGeometry(QtCore.QRect(160, 140, 113, 20))
        self.ModeInput.setObjectName("ModeInput")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(360, 120, 20, 201))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.DifferentPacemaker = QtWidgets.QLabel(self.centralwidget)
        self.DifferentPacemaker.setGeometry(QtCore.QRect(290, 70, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DifferentPacemaker.setFont(font)
        self.DifferentPacemaker.setObjectName("DifferentPacemaker")
        self.DifferentPacemakerOutput = QtWidgets.QLabel(self.centralwidget)
        self.DifferentPacemakerOutput.setGeometry(QtCore.QRect(510, 70, 47, 21))
        self.DifferentPacemakerOutput.setObjectName("DifferentPacemakerOutput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    #Methods of Class
    
    def update(self):
        self.label.adjustSize()

    def login_clicked(self):
        user_name = self.UserName.text()
        password = self.Password.text()
        #since user is existing, check whether password is correct
        if self.users[user_name] == password:
            self.LoginOutput.setText(self.UserName.text())
            self.update()
        
    def add_user_clicked(self):
        user_name = self.UserName.text()
        password = self.Password.text()
        
        #if user is new, add to dictionary of users (if less than 10)
        
        if len(self.users) <= 9: 
            self.users[user_name] = password
            self.LoginOutput.setText(user_name)
        else:
            self.show_popup()
            
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error for Full User List")
        msg.setText("Sorry, no additional users can be added.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Maximum number of users is 10.")
        
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pace Maker User Interface"))
        self.Welcome.setText(_translate("MainWindow", "Welcome to PaceMaker Pro: MAIN MENU"))
        self.UserName_2.setText(_translate("MainWindow", "User Name:"))
        self.Password_2.setText(_translate("MainWindow", "Password:"))
        self.Login.setText(_translate("MainWindow", "LOGIN"))
        self.AddUser.setText(_translate("MainWindow", "ADD USER (Max 10.)"))
        self.LoginOutput.setText(_translate("MainWindow", "TextLabel"))
        self.Mode.setText(_translate("MainWindow", "Mode:"))
        self.DeviceCommunicate.setText(_translate("MainWindow", "DCM and Device comunitating:"))
        self.DeviceCommunicateOutput.setText(_translate("MainWindow", "TextLabel"))
        self.ModeOutput.setText(_translate("MainWindow", "TextLabel"))
        self.User.setText(_translate("MainWindow", "CURRENT USER:"))
        self.LRL.setText(_translate("MainWindow", "Lower Rate Limit:"))
        self.URL.setText(_translate("MainWindow", "Upper Rate Limit:"))
        self.AA.setText(_translate("MainWindow", "Atrial Amplitude:"))
        self.APW.setText(_translate("MainWindow", "Atrial Pules Width:"))
        self.VA.setText(_translate("MainWindow", "Ventricular Amplitude:"))
        self.VRP.setText(_translate("MainWindow", "VRP:"))
        self.VPW.setText(_translate("MainWindow", "Ventrical Pulse Width:"))
        self.ARP.setText(_translate("MainWindow", "ARP:"))
        self.LRLOutput.setText(_translate("MainWindow", "TextLabel"))
        self.URLOutput.setText(_translate("MainWindow", "TextLabel"))
        self.APWOutput.setText(_translate("MainWindow", "TextLabel"))
        self.AAOutput.setText(_translate("MainWindow", "TextLabel"))
        self.VAOutput.setText(_translate("MainWindow", "TextLabel"))
        self.ARPOutput.setText(_translate("MainWindow", "TextLabel"))
        self.VPWOutput.setText(_translate("MainWindow", "TextLabel"))
        self.VRPOutput.setText(_translate("MainWindow", "TextLabel"))
        self.DifferentPacemaker.setText(_translate("MainWindow", "A different Pacemaker is approached:"))
        self.DifferentPacemakerOutput.setText(_translate("MainWindow", "TextLabel"))
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


