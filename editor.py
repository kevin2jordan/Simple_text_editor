#!/usr/bin/python2
import os
import time
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from ext import *

class Main(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)

        self.filename = ""

        self.changesSaved = True

        self.initUI()

    def initToolbar(self):

        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)



        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        dateTimeAction = QtGui.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
        dateTimeAction.setStatusTip("Insert current date/time")
        dateTimeAction.setShortcut("Ctrl+D")
        dateTimeAction.triggered.connect(datetime.DateTime(self).show)



        imageAction = QtGui.QAction(QtGui.QIcon("icons/image.png"),"Insert image",self)
        imageAction.setStatusTip("Insert image")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)

        bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert bullet List",self)
        bulletAction.setStatusTip("Insert bullet list")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(dateTimeAction)
        self.toolbar.addAction(imageAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)

        self.addToolBarBreak()

    def initFormatbar(self):

        fontBox = QtGui.QFontComboBox(self)
        fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

        fontSize = QtGui.QSpinBox(self)

        fontSize.setSuffix(" pt")

        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

        fontSize.setValue(14)

        fontColor = QtGui.QAction(QtGui.QIcon("icons/font-color.png"),"Change font color",self)
        fontColor.triggered.connect(self.fontColorChanged)

        boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
        underlAction.triggered.connect(self.underline)


        alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png"),"Align left",self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"),"Align center",self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"),"Align right",self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"),"Align justify",self)
        alignJustify.triggered.connect(self.alignJustify)

        
        backColor = QtGui.QAction(QtGui.QIcon("icons/highlight.png"),"Change background color",self)
        backColor.triggered.connect(self.highlight)

        self.formatbar = self.addToolBar("Format")

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)

        self.formatbar.addSeparator()

    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        play = menubar.addMenu("PlayMusic")
        help = menubar.addMenu("CodeHelp")
        sshot = menubar.addMenu("S_shot")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        

        toolbarAction = QtGui.QAction("Toggle Toolbar",self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        formatbarAction = QtGui.QAction("Toggle Formatbar",self)
        formatbarAction.triggered.connect(self.toggleFormatbar)

        statusbarAction = QtGui.QAction("Toggle Statusbar",self)
        statusbarAction.triggered.connect(self.toggleStatusbar)

        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)

    def initUI(self):

        self.text = QtGui.QTextEdit(self)
        self.text.setTabStopWidth(33)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        self.setCentralWidget(self.text)
        self.statusbar = self.statusBar()
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)

        self.text.textChanged.connect(self.changed)

        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Personal Editor")
        self.setWindowIcon(QtGui.QIcon("icons/pyt.png"))

    def changed(self):
        self.changesSaved = False

    def closeEvent(self,event):

        if self.changesSaved:

            event.accept()

        else:
        
            popup = QtGui.QMessageBox(self)

            popup.setIcon(QtGui.QMessageBox.Warning)
            
            popup.setText("The document has been modified")
            
            popup.setInformativeText("Do you want to save your changes?")
            
            popup.setStandardButtons(QtGui.QMessageBox.Save   |
                                      QtGui.QMessageBox.Cancel |
                                      QtGui.QMessageBox.Discard)
            
            popup.setDefaultButton(QtGui.QMessageBox.Save)

            answer = popup.exec_()

            if answer == QtGui.QMessageBox.Save:
                self.save()

            elif answer == QtGui.QMessageBox.Discard:
                event.accept()

            else:
                event.ignore()

    def context(self,pos):
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        if table:

            menu = QtGui.QMenu(self)

            appendRowAction = QtGui.QAction("Append row",self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))

            appendColAction = QtGui.QAction("Append column",self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))


            removeRowAction = QtGui.QAction("Remove row",self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtGui.QAction("Remove column",self)
            removeColAction.triggered.connect(self.removeCol)


            insertRowAction = QtGui.QAction("Insert row",self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtGui.QAction("Insert column",self)
            insertColAction.triggered.connect(self.insertCol)


            mergeAction = QtGui.QAction("Merge cells",self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            if not cursor.hasSelection():
                mergeAction.setEnabled(False)


            splitAction = QtGui.QAction("Split cells",self)

            cell = table.cellAt(cursor)

            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(),cell.column(),1,1))

            else:
                splitAction.setEnabled(False)


            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)
            pos = self.mapToGlobal(pos)

            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)
            menu.move(pos)

            menu.show()

        else:

            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())

            self.text.contextMenuEvent(event)

    def removeRow(self):
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        cell = table.cellAt(cursor)
        table.removeRows(cell.row(),1)

    def removeCol(self):

        cursor = self.text.textCursor()
        table = cursor.currentTable()
        cell = table.cellAt(cursor)
        table.removeColumns(cell.column(),1)

    def insertRow(self):
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        cell = table.cellAt(cursor)
        table.insertRows(cell.row(),1)

    def insertCol(self):
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        cell = table.cellAt(cursor)
        table.insertColumns(cell.column(),1)


    def toggleToolbar(self):

        state = self.toolbar.isVisible()
        self.toolbar.setVisible(not state)

    def toggleFormatbar(self):

        state = self.formatbar.isVisible()
        self.formatbar.setVisible(not state)

    def toggleStatusbar(self):

        state = self.statusbar.isVisible()
        self.statusbar.setVisible(not state)

    def new(self):

        spawn = Main()

        spawn.show()

    def open(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def save(self):
        if not self.filename:
          self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        with open(self.filename,"wt") as file:
            file.write(self.text.toPlainText())

    def preview(self):
        preview = QtGui.QPrintPreviewDialog()
        preview.paintRequested.connect(lambda p: self.text.print_(p))
        preview.exec_()

    def printHandler(self):
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def cursorPosition(self):

        cursor = self.text.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

    def insertImage(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")

        if filename:
            image = QtGui.QImage(filename)
            if image.isNull():

                popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                          "Image load error",
                                          "Could not load image file!",
                                          QtGui.QMessageBox.Ok,
                                          self)
                popup.show()

            else:

                cursor = self.text.textCursor()

                cursor.insertImage(image,filename)

    def fontColorChanged(self):
        color = QtGui.QColorDialog.getColor()
        self.text.setTextColor(color)

    def highlight(self):
        color = QtGui.QColorDialog.getColor()
        self.text.setTextBackgroundColor(color)

    def bold(self):

        if self.text.fontWeight() == QtGui.QFont.Bold:

            self.text.setFontWeight(QtGui.QFont.Normal)

        else:

            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):

        state = self.text.fontItalic()

        self.text.setFontItalic(not state)

    def underline(self):

        state = self.text.fontUnderline()

        self.text.setFontUnderline(not state)


    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def bulletList(self):

        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

def main():
    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
