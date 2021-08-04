import sys, platform

######################################## PyQt5 includes ########################################
from PyQt5.QtCore import (
    QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
)
from PyQt5.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
)
from PyQt5.QtWidgets import *
######################################## PyQt5 includes ########################################

######################################## Helper includes #######################################
from ape_ui import UIAtestat
from ape_func import *
######################################## Helper includes #######################################

class Atestat(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.interfataGrafica = UIAtestat()
        self.interfataGrafica.CreazaInterfata(self)

        def moveWindow(event):
            if FunctiiUI.returnStatus() == 1:
                FunctiiUI.maximize_restore(self)
            
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
            
        self.interfataGrafica.baraTitlu.mouseMoveEvent = moveWindow

        FunctiiUI.definitii(self)

        self.show()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()                                                  

if __name__ == "__main__":
    aplicatieAtestat = QApplication(sys.argv)
    fereastraPrincipala = Atestat()
    sys.exit(aplicatieAtestat.exec_())