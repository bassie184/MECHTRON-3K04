# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

qtcreator_file  = "<mainwindow.ui>" # Enter file here.
loader = QUiLoader()
file = QtCore.QFile(qtcreator_file)
file.open(QtCore.QFile.ReadOnly)
file.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load(file, None)
    window.show()
    sys.exit(app.exec_())



from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class threek04_lab(QWidget):
    def __init__(self):
        super(threek04_lab, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = threek04_lab()
    widget.show()
    sys.exit(app.exec_())



