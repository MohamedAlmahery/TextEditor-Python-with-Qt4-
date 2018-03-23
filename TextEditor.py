from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Main (QMainWindow):

        def __init__(self,parent=None):
            QMainWindow.__init__(self,parent)
            self.InitUi()
            self.filename = ""

        ##Our MenuBar
        def Menubar(self):
                menubar = self.menuBar()
                file = menubar.addMenu("File")
                edit = menubar.addMenu('Edit')
                photo = menubar.addMenu("Image's")
                view = menubar.addMenu('View')

                file.addAction(self.newAction)
                file.addAction(self.openAction)
                file.addAction(self.saveAction)
                file.addAction(self.saveasAction)

                edit.addAction(self.cutAction)
                edit.addAction(self.copyAction)
                edit.addAction(self.pasteAction)
                edit.addAction(self.deleteAction)
                edit.addAction(self.selectAllAction)

                photo.addAction(self.airplaneAction)
                photo.addAction(self.carAction)
                photo.addAction(self.bicycleAction)
                photo.addAction(self.cruiseAction)
                photo.addAction(self.parasailingAction)
                photo.addAction(self.schoolbusAction)
                photo.addAction(self.scooterAction)
                photo.addAction(self.startupAction)

                view.addAction(self.helpAction)
                view.addAction(self.aboutAction)



                
        ##Our Toolbar
        def Toolbar(self):

                self.newAction = QAction(QIcon('icons/new.png') , 'New' , self)
                self.newAction.triggered.connect(self.new)
                self.newAction.setShortcut("ctrl+N")
                self.openAction = QAction(QIcon('icons/open.png'), 'Open', self)
                self.openAction.triggered.connect(self.open)
                self.openAction.setShortcut('ctrl+o')
                self.saveAction = QAction(QIcon('icons/save.png'), 'Save', self)
                self.saveAction.triggered.connect(self.save)
                self.saveAction.setShortcut('ctrl+s')
                self.saveasAction = QAction("Save TO Know HTML code" , self)
                self.saveasAction.triggered.connect(self.saveas)
                
                self.cutAction = QAction(QIcon('icons/cut.png'), 'Cut', self)
                self.cutAction.triggered.connect(self.cut)
                self.cutAction.setShortcut('ctrl+x')
                self.copyAction = QAction(QIcon('icons/copy.png'), 'Copy', self)
                self.copyAction.triggered.connect(self.copy)
                self.copyAction.setShortcut('ctrl+c')
                self.pasteAction = QAction(QIcon('icons/paste.png'), 'Paste', self)
                self.pasteAction.triggered.connect(self.paste)
                self.pasteAction.setShortcut('ctrl+v')
                self.deleteAction = QAction(QIcon('icons/delete.png'), 'Clear', self)
                self.deleteAction.triggered.connect(self.delete)
                self.deleteAction.setShortcut('ctrl+d')
                self.selectAllAction = QAction(QIcon('icons/sellectall.png'), 'Sellect All', self)
                self.selectAllAction.triggered.connect(self.selectAll)
                self.selectAllAction.setShortcut('ctrl+A')

                self.airplaneAction = QAction(QIcon("image's/airplane.png"),"Airplane",self)
                self.airplaneAction.triggered.connect(self.airplane)
                self.carAction = QAction(QIcon("image's/car.png"),"Car",self)
                self.carAction.triggered.connect(self.car)
                self.bicycleAction = QAction(QIcon("image's/bicycle.png"),"bicycle",self)
                self.bicycleAction.triggered.connect(self.bicycle)
                self.cruiseAction = QAction(QIcon("image's/cruise.png"),"cruise",self)
                self.cruiseAction.triggered.connect(self.cruise)
                self.parasailingAction = QAction(QIcon("image's/parasailing.png"),"parasailing",self)
                self.parasailingAction.triggered.connect(self.parasailing)
                self.schoolbusAction = QAction(QIcon("image's/school-bus.png"),"school-bus",self)
                self.schoolbusAction.triggered.connect(self.schoolbus)
                self.scooterAction = QAction(QIcon("image's/scooter.png"),"scooter",self)
                self.scooterAction.triggered.connect(self.scooter)
                self.startupAction = QAction(QIcon("image's/startup.png"),"startup",self)
                self.startupAction.triggered.connect(self.startup)
                self.truckAction = QAction(QIcon("image's/truck.png"),"truck",self)
                self.truckAction.triggered.connect(self.truck)


                self.helpAction = QAction(QIcon('icons/help.png'), 'Help', self)
                self.helpAction.triggered.connect(self.help)
                self.aboutAction = QAction(QIcon('icons/about.png'), 'About', self)
                self.aboutAction.triggered.connect(self.about)

        ##Our Formatbar
        def Formatbar(self):


                fontbox = QFontComboBox(self)
                fontbox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

                fontsize = QSpinBox(self)
                fontsize.setSuffix("pt")
                fontsize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))
                fontsize.setValue(50)
                if self.text.clear():
                        fontsize.setValue(50)


                fontcolors = QAction(QIcon("icons/font-color.png") , "Change Font color" , self)
                fontcolors.triggered.connect(self.font_color_changes)


                bold = QAction(QIcon("icons/bold") , "Change Font To Bold" , self)
                bold.triggered.connect(self.bold)

                italic = QAction(QIcon("icons/italic.png") , "Change Font To Italic" , self)
                italic.triggered.connect(self.italic)

                underline = QAction(QIcon("icons/underline.png") , "Put A Line Under Words" , self)
                underline.triggered.connect(self.underline)

                strike = QAction(QIcon("icons/strike.png") , "Put A Line On Your Words" , self)
                strike.triggered.connect(self.strike)

                align_left = QAction(QIcon("icons/align-left.png") ,"Align Words To Left" , self)
                align_left.triggered.connect(self.align_left)

                align_right = QAction(QIcon("icons/align-right.png") , "Align Words To Right" , self)
                align_right.triggered.connect(self.align_right)

                align_center = QAction(QIcon("icons/align-center.png") , "Align Words To center" , self)
                align_center.triggered.connect(self.align_center)

                justify = QAction(QIcon("icons/align-justify.png") , "Justify Your Words" , self)
                justify.triggered.connect(self.justify)

                undo = QAction(QIcon("icons/undo.png"),"Undo Your word" , self)
                undo.triggered.connect(self.undo)

                redo = QAction(QIcon("icons/redo.png"),"Redo Your word" , self)
                redo.triggered.connect(self.redo)

                delete = QAction(QIcon("icons/delete.png"),"Delete Your text" , self)
                delete.triggered.connect(self.delete)

                self.Formatbar = self.addToolBar("Format")
                self.Formatbar.addWidget(fontbox)
                self.Formatbar.addWidget(fontsize)
                self.Formatbar.addSeparator()


                self.Formatbar.addAction(fontcolors)
                self.Formatbar.addAction(bold)
                self.Formatbar.addAction(italic)
                self.Formatbar.addAction(underline)
                self.Formatbar.addAction(strike)
                self.Formatbar.addSeparator()

                self.Formatbar.addAction(align_left)
                self.Formatbar.addAction(align_right)
                self.Formatbar.addAction(justify)
                self.Formatbar.addAction(align_center)
                self.Formatbar.addSeparator()

                self.Formatbar.addAction(undo)
                self.Formatbar.addAction(redo)
                self.Formatbar.addAction(delete)

        def SFormatbar (self):
                self.SFormatbar = self.addToolBar("Tools")

                newtool = QAction(QIcon("icons/new.png"), "New", self)
                newtool.triggered.connect(self.new)

                opentool = QAction(QIcon("icons/open.png"), "Open", self)
                opentool.triggered.connect(self.open)

                savetool = QAction(QIcon("icons/save.png"), "Save", self)
                savetool.triggered.connect(self.save)

                self.SFormatbar.addAction(savetool)
                self.SFormatbar.addAction(newtool)
                self.SFormatbar.addAction(opentool)

        def PFormatbar (self):
                self.PFormatbar = self.addToolBar("Image's")

                airplanetool = QAction(QIcon("image's/airplane.png"),"Airplane",self)
                airplanetool.triggered.connect(self.airplane)

                cartool = QAction(QIcon("image's/car.png"),"Car",self)
                cartool.triggered.connect(self.car)

                bicycletool = QAction(QIcon("image's/bicycle.png"),"bicycle",self)
                bicycletool.triggered.connect(self.bicycle)

                cruisetool = QAction(QIcon("image's/cruise.png"),"cruise",self)
                cruisetool.triggered.connect(self.cruise)

                parasailingtool = QAction(QIcon("image's/parasailing.png"),"parasailing",self)
                parasailingtool.triggered.connect(self.parasailing)

                schoolbustool = QAction(QIcon("image's/school-bus.png"),"school-bus",self)
                schoolbustool.triggered.connect(self.schoolbus)

                scootertool = QAction(QIcon("image's/scooter.png"),"scooter",self)
                scootertool.triggered.connect(self.scooter)
                
                startuptool = QAction(QIcon("image's/startup.png"),"startup",self)
                startuptool.triggered.connect(self.startup)

                trucktool = QAction(QIcon("image's/truck.png"),"truck",self)
                trucktool.triggered.connect(self.truck)

                self.PFormatbar.addAction(airplanetool)
                self.PFormatbar.addAction(cartool)
                self.PFormatbar.addAction(bicycletool)
                self.PFormatbar.addAction(cruisetool)
                self.PFormatbar.addAction(parasailingtool)
                self.PFormatbar.addAction(schoolbustool)
                self.PFormatbar.addAction(scootertool)
                self.PFormatbar.addAction(startuptool)

        def new(self):
                f = open('darkorange.stylesheet', 'r')
                style = f.read()
                f.close()
                main_window = Main()
                main_window.setStyleSheet(style)
                main_window.show()
                
        
        def open(self):
                self.filename = QFileDialog.getOpenFileName(self , "Open File" , '.' , "(*.txt)")

                if self.filename:
                        with open(self.filename , "rt") as file :
                                self.text.setText(file.read())
        def save(self):
                if not self.filename:
                        self.filename = QFileDialog.getSaveFileName(self , "Save File" , '.' , "(*.txt)")

                if not self.filename.endswith(".txt") :
                        self.filename += ".txt"

                with open(self.filename, "wt") as file:
                        file.write(self.text.toPlainText())

        def saveas(self):
                if not self.filename:
                        self.filename = QFileDialog.getSaveFileName(self , "Save File" , '.' , "(*.txt)")

                if not self.filename.endswith(".txt"):
                        self.filename += ".txt"

                with open(self.filename, "wt") as file:
                        file.write(self.text.toHtml())

        def cut(self):
                self.text.cut()
        def copy(self):
                self.text.copy()
        def paste(self):
                self.text.paste()
        def delete(self):
                self.text.clear()
        def selectAll(self):
                self.text.selectAll()

        def help(self):
                self.text.setText('To Help : https://www.facebook.com/Almahery123')
        def about(self):
                self.text.setText('Programmer : Mohamed Ashraf ')
        def font_color_changes(self):
                colors = QColorDialog.getColor()
                self.text.setTextColor(colors)
        def highlight(self):
                color = QColorDialog.getColor()
                self.text.setTextBackgroundColor(color)
        def bold(self):
                if self.text.fontWeight() == QFont.Bold:
                        self.text.setFontWeight(QFont.Normal)
                else:
                        self.text.setFontWeight(QFont.Bold)
        def italic(self):
                state = self.text.fontItalic()
                self.text.setFontItalic(not state)

        def underline(self):
                state = self.text.fontUnderline()
                self.text.setFontUnderline(not state)
                
        def strike(self):
                words = self.text.currentCharFormat()
                words.setFontStrikeOut(not words.fontStrikeOut())
                self.text.setCurrentCharFormat(words)
        def align_left(self):
                self.text.setAlignment(Qt.AlignLeft)
        def align_right(self):
                self.text.setAlignment(Qt.AlignRight)
        def align_center(self):
                self.text.setAlignment(Qt.AlignCenter)
        def justify(self):
                self.text.setAlignment(Qt.AlignJustify)

        def undo(self):
                self.text.undo()
        def redo(self):
                self.text.redo()
                
        ##Our image's
        def airplane(self):
                url = ("image's/airplane.png")
                self.text.setHtml('<img src="%s" />' % url)
        def car (self):
                url = ("image's/car.png")
                self.text.setHtml('<img src="%s" />' % url)
        def bicycle (self):
                url = ("image's/bicycle.png")
                self.text.setHtml('<img src="%s" />' % url)
        def cruise(self):
                url = ("image's/cruise.png")
                self.text.setHtml('<img src="%s" />' % url)
        def parasailing (self):
                 url = ("image's/parasailing.png")
                 self.text.setHtml('<img src="%s" />' % url)
        def schoolbus(self):
                url = ("image's/school-bus.png")
                self.text.setHtml('<img src="%s" />' % url)
        def scooter(self):
                url = ("image's/scooter.png")
                self.text.setHtml('<img src="%s" />' % url)
        def startup(self):
                url = ("image's/startup.png")
                self.text.setHtml('<img src="%s" />' % url)
        def truck(self):
                url = ("image's/truck.png")
                self.text.setHtml('<img src=%s">'% url)
        
                
        def InitUi(self):
                ##Start With The Gui
                self.text = QTextEdit(self)
                self.setCentralWidget(self.text)
                self.setGeometry(100 , 100 , 900 , 600)
                self.SFormatbar()
                self.Formatbar()
                self.Toolbar()
                self.Menubar()
                self.PFormatbar()
                self.statusBar().showMessage('Text Editor')
                self.setWindowTitle('Text Editor')
                self.setWindowIcon(QIcon('text.png'))
                self.setToolTip('The main program')

                
def main():
    f = open('darkorange.stylesheet' , 'r')
    style = f.read()
    f.close()
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.setStyleSheet(style)
    main_window.show()
    app.exec_()
                
if __name__ == "__main__":
        main()
