#! /usr/bin/env python3
import sys
import os
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog



class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle('Persnal Editor')
        self.setWindowIcon(QIcon('pyt.png'))

        extractAction = QAction('&Exit ', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        openEditor = QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QAction('&Save File', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)


        self.statusBar()

        mainMenu = self.menuBar()
	
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        fileMenu = mainMenu.addMenu('&Options')
        fileMenu.addAction(extractAction)

        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
	


        self.home()

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    def file_open(self):
      
        name,_ = QFileDialog.getOpenFileName(self, 'Open File')
   
        file = open(name, 'r')
      
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(self,'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


    def home(self):

        self.show()

   

    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass


if __name__ == "__main__":  

    def start():
        app = QApplication(sys.argv)
        rahul = window()
        sys.exit(app.exec_())

start()
