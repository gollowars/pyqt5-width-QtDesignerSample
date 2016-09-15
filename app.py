import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from sample2 import Ui_MainWindow

class MyQueueObj(QObject):
  mySampleSignal = pyqtSignal() 

class MyWindow(QMainWindow,Ui_MainWindow):
  def __init__(self,parent=None,name=None,fl=0):
    QMainWindow.__init__(self,parent)
    self.setupUi(self)

    self.progressBar.setMaximum(99)
    self.addEvent()


  def addEvent(self):
    self.pushButton.clicked.connect(self.buttonClicked)
    
    self.c = MyQueueObj()
    self.c.mySampleSignal.connect(self.mySignalEventHandler)

    self.horizontalSlider.valueChanged.connect(self.sliderValueChangeHandler)

  def buttonClicked(self):
    print('button is clicked!!')
    
    self.c.mySampleSignal.emit()

  def sliderValueChangeHandler(self,value):
    self.lcdNumber.display(value)
    print(self.lcdNumber.value())
    self.progressBar.setValue(int(value))



  def mySignalEventHandler(self):
    print('mySignalEventHandler')


if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MyWindow()
  w.show()
  sys.exit(app.exec_())