import sys
import PyQt5.QtCore
import PyQt5.QtWidgets
class txtToXml(PyQt5.QtWidgets.QDialog):
    def __init__(self):
        PyQt5.QtWidgets.QDialog.__init__(self)
        layout = PyQt5.QtWidgets.QGridLayout(self)
        self.display = PyQt5.QtWidgets.QLineEdit()
        self.display.setReadOnly(True)
        self.display.setPlaceholderText("Please enter the location of file to be converted")
        self.textBox = PyQt5.QtWidgets.QPlainTextEdit()
        self.textBox.setReadOnly(True)
        self.textBox.setPlaceholderText("Preview of File")
        self.convert = PyQt5.QtWidgets.QPushButton("Convert")
        self.browse = PyQt5.QtWidgets.QPushButton("Browse")
        self.buttonClose = PyQt5.QtWidgets.QPushButton("Close")
        self.author = PyQt5.QtWidgets.QLabel("<h2>Designed by Karthik C R S</h2>")
        layout.addWidget(self.display,0,0,1,4)
        layout.addWidget(self.browse,0,5)
        layout.addWidget(self.textBox,2,0,10,4)
        layout.addWidget(self.convert,2,5,4,1)
        layout.addWidget(self.buttonClose,9,5,4,1)
        layout.addWidget(self.author,12,1,10,2)
        self.setLayout(layout)
        self.setWindowTitle("Text to Xml By Karthik C R S")
        self.buttonClose.clicked.connect(self.close)
        self.browse.clicked.connect(self.browse_file)
        self.convert.clicked.connect(self.processFile)
    def browse_file(self):
           try:
               self.convert.setFocus()
               self.open_file = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, directory=self.display.text(),
                                                                            filter="*.*")
               self.tempFileDir=PyQt5.QtCore.QDir.toNativeSeparators(self.open_file[0])
               self.display.setText(PyQt5.QtCore.QDir.toNativeSeparators(self.open_file[0]))
               self.viewFile()
               return
           except Exception:
                PyQt5.QtWidgets.QMessageBox.warning(self, "Warning", Exception)
                return
    def viewFile(self):
        self.text = open(self.open_file[0]).read()
        self.textBox.setPlainText(self.text)
    def processFile(self):
        targetFileName = self.tempFileDir[:-3]
        targetFileName = targetFileName + "xml"
        outputFile = open(targetFileName,"w+")
        self.targetData = self.text.replace("><",">\n<")
        outputFile.write(self.targetData)
        self.textBox.setPlainText(self.targetData)
app = PyQt5.QtWidgets.QApplication(sys.argv)
dialog = txtToXml()
dialog.show()
app.exec_()