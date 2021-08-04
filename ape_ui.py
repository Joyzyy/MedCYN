from PyQt5.QtCore import (
    QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt
)
from PyQt5.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
)
from PyQt5.QtWidgets import *

import sqlite3, pandas

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

class UIAtestat(object):
    def CreazaInterfata(self, wnd):
        if wnd.objectName():
            wnd.setObjectName(u"FereastraPrincipala")
        wnd.resize(880, 600)
        wnd.setMinimumSize(QSize(880, 600))

        self.centralWidget = QWidget(wnd)
        self.centralWidget.setObjectName(u"centralWidget")

        self.aspectUmbra = QVBoxLayout(self.centralWidget)
        self.aspectUmbra.setSpacing(0)
        self.aspectUmbra.setContentsMargins(10, 10, 10, 10)
        self.aspectUmbra.setObjectName(u"aspectUmbra")

        self.cadruUmbra = QFrame(self.centralWidget)
        self.cadruUmbra.setStyleSheet(u"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n")
        self.cadruUmbra.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(41, 41, 48), stop:0.521368 rgb(32, 39, 48));\n"
"border-radius: 10px;")
        self.cadruUmbra.setFrameShape(QFrame.NoFrame)
        self.cadruUmbra.setFrameShadow(QFrame.Raised)

        self.aspectVertical = QVBoxLayout(self.cadruUmbra)
        self.aspectVertical.setSpacing(0)
        self.aspectVertical.setContentsMargins(0, 0, 0, 0)
        self.aspectVertical.setObjectName(u"aspectVertical")

        self.baraTitlu = QFrame(self.cadruUmbra)
        self.baraTitlu.setMaximumSize(QSize(16777215, 50))
        self.baraTitlu.setFrameShape(QFrame.NoFrame)
        self.baraTitlu.setFrameShadow(QFrame.Raised)
        self.baraTitlu.setStyleSheet(u"background-color: none;")

        self.aspectOrizontal = QHBoxLayout(self.baraTitlu)
        self.aspectOrizontal.setSpacing(0)
        self.aspectOrizontal.setContentsMargins(0, 0, 0, 0)
        self.aspectOrizontal.setObjectName(u"aspectOrizontal")

        self.cadruTitlului = QFrame(self.baraTitlu)
        self.cadruTitlului.setMinimumSize(QSize(0, 50))
        fontRobotoLight = QFont()
        fontRobotoLight.setFamily(u"Roboto Condensed Light")
        fontRobotoLight.setPointSize(14)
        self.cadruTitlului.setFont(fontRobotoLight)
        self.cadruTitlului.setFrameShape(QFrame.StyledPanel)
        self.cadruTitlului.setFrameShadow(QFrame.Raised)

        self.aspectVertical_2 = QVBoxLayout(self.cadruTitlului)
        self.aspectVertical_2.setSpacing(0)
        self.aspectVertical_2.setContentsMargins(15, 0, 0, 0)
        self.aspectVertical_2.setObjectName(u"aspectVertical_2")

        self.etichetaTitlu = QLabel(self.cadruTitlului)
        fontRoboto = QFont()
        fontRoboto.setFamily(u"Roboto")
        fontRoboto.setPointSize(14)
        self.etichetaTitlu.setFont(fontRoboto)
        self.etichetaTitlu.setStyleSheet(u"color: rgb(62, 182, 80);")
        self.etichetaTitlu.setObjectName(u"etichetaTitlu")
        
        self.aspectVertical_2.addWidget(self.etichetaTitlu)
        self.aspectOrizontal.addWidget(self.cadruTitlului)

        self.cadruButoane = QFrame(self.baraTitlu)
        self.cadruButoane.setMaximumSize(QSize(100, 16777215))
        self.cadruButoane.setFrameShape(QFrame.StyledPanel)
        self.cadruButoane.setFrameShadow(QFrame.Raised)

        self.aspectOrizontal_2 = QHBoxLayout(self.cadruButoane)
        self.aspectOrizontal_2.setObjectName(u"aspectOrizontal_2")

        self.butonMareste = QPushButton(self.cadruButoane)
        self.butonMareste.setMinimumSize(QSize(18, 17))
        self.butonMareste.setMaximumSize(QSize(19, 17))
        self.butonMareste.setStyleSheet(u"QPushButton {\n"
"   border-radius: 4px; \n"
"   background-image: url(cil-media-stop.png);\n"
"   background-position: bottom; \n"
"   background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(50, 50, 50);\n"
"   color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"   background-color: rgb(35, 35, 35);\n"
"   color: rgb(200, 200, 200);\n"
"}")


        self.butonMinimizeaza = QPushButton(self.cadruButoane)
        self.butonMinimizeaza.setMinimumSize(QSize(18, 17))
        self.butonMinimizeaza.setMaximumSize(QSize(19, 17))
        self.butonMinimizeaza.setStyleSheet(u"QPushButton {\n"
"   border-radius: 4px; \n"
"   background-image: url(cil-window-minimize.png);\n"
"   background-position: center; \n"
"   background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(50, 50, 50);\n"
"   color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"   background-color: rgb(35, 35, 35);\n"
"   color: rgb(200, 200, 200);\n"
"}")
        

        self.butonInchide = QPushButton(self.cadruButoane)
        self.butonInchide.setMinimumSize(QSize(18, 17))
        self.butonInchide.setMaximumSize(QSize(19, 17))
        self.butonInchide.setStyleSheet(u"QPushButton {\n"
"   border-radius: 4px; \n"
"   background-image: url(cil-x.png);\n"
"   background-position: center; \n"
"   background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(50, 50, 50);\n"
"   color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"   background-color: rgb(35, 35, 35);\n"
"   color: rgb(200, 200, 200);\n"
"}")
        
        self.aspectOrizontal_2.addWidget(self.butonMinimizeaza)
        self.aspectOrizontal_2.addWidget(self.butonMareste)
        self.aspectOrizontal_2.addWidget(self.butonInchide)

        self.aspectOrizontal.addWidget(self.cadruButoane)
        self.aspectVertical.addWidget(self.baraTitlu)

        ## cadru
        self.baraContinut = QFrame(self.cadruUmbra)
        self.baraContinut.setStyleSheet(u"background-color: none;")
        self.baraContinut.setFrameShape(QFrame.StyledPanel)
        self.baraContinut.setFrameShadow(QFrame.Raised)

        self.aspectVertical_4 = QVBoxLayout(self.baraContinut)

        self.paginiWidget = QStackedWidget(self.baraContinut)
        self.paginiWidget.setStyleSheet(u"background-color: none;")


        ### creaza un tabel
        def CreazaTabel(pNumeTabel):
            pNumeTabel.setRowCount(15)
            pNumeTabel.setColumnCount(11)
            pNumeTabel.setSelectionMode(QAbstractItemView.NoSelection)
            pNumeTabel.setCornerButtonEnabled(False)
            pNumeTabel.setShowGrid(True)
            pNumeTabel.setGridStyle(Qt.SolidLine)
            pNumeTabel.horizontalHeader().setVisible(True)
            pNumeTabel.horizontalHeader().setCascadingSectionResizes(True)
            pNumeTabel.horizontalHeader().setStretchLastSection(True)
            pNumeTabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            pNumeTabel.verticalHeader().setVisible(True)
            pNumeTabel.verticalHeader().setCascadingSectionResizes(False)
            pNumeTabel.verticalHeader().setHighlightSections(False)
            pNumeTabel.verticalHeader().setStretchLastSection(True)
            pNumeTabel.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
""
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget QTableCornerButton::section\n"
"{\n"
"   background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
            x = 0

        def search_func(self):
            aux = Fereastra_Search()
            aux.exec_()

        def ml_med_func(self):
            aux = ML_Medicamente()
            aux.exec_()

        def ml_asis_med_func(self):
            aux = ML_Medic_Asistente()
            aux.exec_()

        #### prima pagina
        self.pAcasa = QWidget()
        
        self.aspectVertical_6 = QVBoxLayout(self.pAcasa)

        self.frameMain = QFrame(self.pAcasa)

        self.aspectVertical_5 = QVBoxLayout(self.frameMain)

        itemSpatiere_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.aspectVertical_5.addItem(itemSpatiere_1)

        self.bine_ai_venit_txt = QLabel(self.frameMain)
        self.bine_ai_venit_txt.setText("Bine ai venit!")
        font = QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.bine_ai_venit_txt.setFont(font)
        self.bine_ai_venit_txt.setTextFormat(Qt.RichText)
        self.bine_ai_venit_txt.setAlignment(Qt.AlignCenter)
        self.bine_ai_venit_txt.setWordWrap(False)
        self.bine_ai_venit_txt.setObjectName("bine_ai_venit_txt")
        
        self.aspectVertical_5.addWidget(self.bine_ai_venit_txt)

        self.copyright = QLabel(self.frameMain)
        self.copyright.setText("MedCYN (c) Zavoianu Gabriel 2021")
        font = QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(24)
        self.copyright.setFont(font)
        self.copyright.setStyleSheet("color: rgb(255, 0, 0);")
        self.copyright.setScaledContents(False)
        self.copyright.setAlignment(Qt.AlignCenter)
        self.copyright.setObjectName("copyright")

        self.aspectVertical_5.addWidget(self.copyright)

        itemSpatiere_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.aspectVertical_5.addItem(itemSpatiere_2)
        self.aspectVertical_6.addWidget(self.frameMain)

        self.paginiWidget.addWidget(self.pAcasa)

        ###### end prima pagina

        ###### a doua pagina (medici)
        self.pMedici = QWidget()
        self.aspectVertical_8 = QVBoxLayout(self.pMedici)
        
        self.frameButoaneSearch = QHBoxLayout()
        g_SpatiuLiber_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frameButoaneSearch.addItem(g_SpatiuLiber_2)

        self.statisticiMedici = QPushButton(self.pMedici)
        ibutonStatisticiMedici = QIcon()
        ibutonStatisticiMedici.addPixmap(QPixmap("P:\\Poriect atestat/cil-chart.png"), QIcon.Normal, QIcon.On)
        self.statisticiMedici.setIcon(ibutonStatisticiMedici)
        self.statisticiMedici.setIconSize(QSize(24, 24))

        self.frameButoaneSearch.addWidget(self.statisticiMedici)

        self.butonSearchMedici = QPushButton(self.pMedici)
        ibutonSearchMedici = QIcon()
        ibutonSearchMedici.addPixmap(QPixmap("C:/Users/Playboi Carti/Desktop/Licenta/Aplicatie/img/cauta.png"), QIcon.Normal, QIcon.On)
        self.butonSearchMedici.setIcon(ibutonSearchMedici)
        self.butonSearchMedici.setIconSize(QSize(24, 24))

        self.frameButoaneSearch.addWidget(self.butonSearchMedici)
        self.aspectVertical_8.addLayout(self.frameButoaneSearch)

        def func_statisticiMedici(self):
            ml_asis_med_func(self)

        def func_butonSearchMedici(self):
            search_func(self)

        self.statisticiMedici.clicked.connect(lambda: func_statisticiMedici(self))
        self.butonSearchMedici.clicked.connect(lambda: func_butonSearchMedici(self))

        self.aspectVertical_7 = QVBoxLayout()
        
        self.tabelMedici = QTableWidget(self.pMedici)
        CreazaTabel(self.tabelMedici)

        self.tabelMedici.setColumnCount(5)
        self.tabelMedici.setRowCount(0)

        self.baza_de_date = sqlite3.connect('sql/medcyn.db')
        self.binfo = self.baza_de_date.cursor()

        self.binfo.execute("SELECT `Nume`, `Sectie`, `Disponibil`, `Program lucru`, `Motiv` FROM `medici`")
        for r_n, r_d in enumerate(self.binfo):
            self.tabelMedici.insertRow(r_n)
            for c_n, data in enumerate(r_d):
                self.tabelMedici.setItem(r_n, c_n, QTableWidgetItem(str(data)))
                self.tabelMedici.setSortingEnabled(True)

        self.binfo.close()
        self.baza_de_date.close()

        self.tabelMedici.setHorizontalHeaderLabels(
            (
                "Nume",
                "Sectie",
                "Disponibil",
                "Program de lucru",
                "Motiv"
            )
        )

        self.aspectVertical_7.addWidget(self.tabelMedici)
        self.aspectVertical_8.addLayout(self.aspectVertical_7)

        ####### end medici
        
        ####### start asistente
        self.pAsistente = QWidget()
        self.aspectVertical_9 = QVBoxLayout(self.pAsistente)

        self.frameButoaneSearch_2 = QHBoxLayout()
        g_SpatiuLiber_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frameButoaneSearch_2.addItem(g_SpatiuLiber_3)

        self.statisticiAsistente = QPushButton(self.pAsistente)
        ibutonStatisticiAsistente = QIcon()
        ibutonStatisticiAsistente.addPixmap(QPixmap("P:\\Poriect atestat/cil-chart.png"), QIcon.Normal, QIcon.On)
        self.statisticiAsistente.setIcon(ibutonStatisticiAsistente)
        self.statisticiAsistente.setIconSize(QSize(24, 24))        

        self.frameButoaneSearch_2.addWidget(self.statisticiAsistente)

        self.butonSearchAsistente = QPushButton(self.pAsistente)
        ibutonSearchAsistente = QIcon()
        ibutonSearchAsistente.addPixmap(QPixmap("C:/Users/Playboi Carti/Desktop/Licenta/Aplicatie/img/cauta.png"), QIcon.Normal, QIcon.On)
        self.butonSearchAsistente.setIcon(ibutonSearchAsistente)
        self.butonSearchAsistente.setIconSize(QSize(24, 24))

        self.frameButoaneSearch_2.addWidget(self.butonSearchAsistente)
        self.aspectVertical_9.addLayout(self.frameButoaneSearch_2)

        def func_statisticiAsistente(self):
            ml_asis_med_func(self)

        def func_butonSearchAsistente(self):
            search_func(self)

        self.statisticiAsistente.clicked.connect(lambda: func_statisticiAsistente(self))
        self.butonSearchAsistente.clicked.connect(lambda: func_butonSearchAsistente(self))

        self.aspectVertical_9_2 = QVBoxLayout()

        self.tableAsistente = QTableWidget(self.pAsistente)
        CreazaTabel(self.tableAsistente)

        self.tableAsistente.setColumnCount(5)
        self.tableAsistente.setRowCount(0)

        self.baza_de_date = sqlite3.connect('sql/medcyn.db')
        self.binfo = self.baza_de_date.cursor()

        self.binfo.execute("SELECT `Nume`, `Sectie`, `Disponibil`, `Program lucru`, `Motiv` FROM `asistente`")
        for r_n, r_d in enumerate(self.binfo):
            self.tableAsistente.insertRow(r_n)
            for c_n, data in enumerate(r_d):
                self.tableAsistente.setItem(r_n, c_n, QTableWidgetItem(str(data)))
                self.tableAsistente.setSortingEnabled(True)

        self.binfo.close()
        self.baza_de_date.close()

        self.tableAsistente.setHorizontalHeaderLabels(
            (
                "Nume",
                "Sectie",
                "Disponibil",
                "Program de lucru",
                "Motiv"
            )
        )

        self.aspectVertical_9_2.addWidget(self.tableAsistente)
        self.aspectVertical_9.addLayout(self.aspectVertical_9_2)

        ### end asistente

        ### start pacienti
        self.pPacienti = QWidget()
        self.aspectVertical_10 = QVBoxLayout(self.pPacienti)

        self.frameButoaneSearch_3 = QHBoxLayout()
        g_SpatiuLiber_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frameButoaneSearch_3.addItem(g_SpatiuLiber_4)

        self.butonSearchPacienti = QPushButton(self.pPacienti)
        ibutonSearchPacienti = QIcon()
        ibutonSearchPacienti.addPixmap(QPixmap("C:/Users/Playboi Carti/Desktop/Licenta/Aplicatie/img/cauta.png"), QIcon.Normal, QIcon.On)
        self.butonSearchPacienti.setIcon(ibutonSearchPacienti)
        self.butonSearchPacienti.setIconSize(QSize(24, 24))

        self.frameButoaneSearch_3.addWidget(self.butonSearchPacienti)
        self.aspectVertical_10.addLayout(self.frameButoaneSearch_3)

        def func_butonSearchPacienti(self):
            search_func(self)

        self.butonSearchPacienti.clicked.connect(lambda: func_butonSearchPacienti(self))

        self.aspectVertical_10_2 = QVBoxLayout()

        self.tabelPacienti = QTableWidget(self.pPacienti)
        CreazaTabel(self.tabelPacienti)

        self.tabelPacienti.setColumnCount(9)
        self.tabelPacienti.setRowCount(0)

        self.baza_de_date = sqlite3.connect('sql/medcyn.db')
        self.binfo = self.baza_de_date.cursor()

        self.binfo.execute("SELECT `Nume`, `Varsta`, `Sectie`, `Bloc`, `Etaj`, `Camera`, `Afectiune`, `Medicament administrat`, `Evolutie` FROM `pacienti`")
        for r_n, r_d in enumerate(self.binfo):
            self.tabelPacienti.insertRow(r_n)
            for c_n, data in enumerate(r_d):
                self.tabelPacienti.setItem(r_n, c_n, QTableWidgetItem(str(data)))
                self.tabelPacienti.setSortingEnabled(True)

        self.binfo.close()
        self.baza_de_date.close()

        self.tabelPacienti.setHorizontalHeaderLabels(
            (
                "Nume",
                "Varsta",
                "Sectie",
                "Bloc",
                "Etaj",
                "Camera",
                "Afectiune",
                "Medicament administrat",
                "Evolutie",
            )
        )

        self.aspectVertical_10_2.addWidget(self.tabelPacienti)
        self.aspectVertical_10.addLayout(self.aspectVertical_10_2)
        ### end pacienti

        ### start medicamente
        self.pMedicamente = QWidget()
        self.aspectVertical_11 = QVBoxLayout(self.pMedicamente)

        self.frameButoaneSearch_4 = QHBoxLayout()
        g_SpatiuLiber_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frameButoaneSearch_4.addItem(g_SpatiuLiber_5)

        self.statisticiMedicamente = QPushButton(self.pMedicamente)
        ibutonStatisticiMedicamente = QIcon()
        ibutonStatisticiMedicamente.addPixmap(QPixmap("P:\\Poriect atestat/cil-chart.png"), QIcon.Normal, QIcon.On)
        self.statisticiMedicamente.setIcon(ibutonStatisticiMedicamente)
        self.statisticiMedicamente.setIconSize(QSize(24, 24))        

        self.frameButoaneSearch_4.addWidget(self.statisticiMedicamente)

        self.butonSearchMedicamente = QPushButton(self.pMedicamente)
        ibutonSearchMedicamente = QIcon()
        ibutonSearchMedicamente.addPixmap(QPixmap("C:/Users/Playboi Carti/Desktop/Licenta/Aplicatie/img/cauta.png"), QIcon.Normal, QIcon.On)
        self.butonSearchMedicamente.setIcon(ibutonSearchMedicamente)
        self.butonSearchMedicamente.setIconSize(QSize(24, 24))

        self.frameButoaneSearch_4.addWidget(self.butonSearchMedicamente)
        self.aspectVertical_11.addLayout(self.frameButoaneSearch_4)

        def func_statisticiMedicamente(self):
            ml_med_func(self)

        def func_butonSearchMedicamente(self):
            search_func(self)

        self.statisticiMedicamente.clicked.connect(lambda: func_statisticiMedicamente(self))
        self.butonSearchMedicamente.clicked.connect(lambda: func_butonSearchMedicamente(self))

        self.aspectVertical_11_2 = QVBoxLayout()

        self.tabelMedicamente = QTableWidget(self.pMedicamente)
        CreazaTabel(self.tabelMedicamente)

        self.tabelMedicamente.setColumnCount(3)
        self.tabelMedicamente.setRowCount(0)

        self.baza_de_date = sqlite3.connect('sql/medcyn.db')
        self.binfo = self.baza_de_date.cursor()

        self.binfo.execute("SELECT `Sectie`, `Nume`, `Cantitate` FROM `medicamente`")
        for r_n, r_d in enumerate(self.binfo):
            self.tabelMedicamente.insertRow(r_n)
            for c_n, data in enumerate(r_d):
                self.tabelMedicamente.setItem(r_n, c_n, QTableWidgetItem(str(data)))
                self.tabelMedicamente.setSortingEnabled(True)

        self.binfo.close()
        self.baza_de_date.close()

        self.tabelMedicamente.setHorizontalHeaderLabels(
            (
                "Sectie",
                "Nume",
                "Cantitate"
            )
        )

        self.aspectVertical_11_2.addWidget(self.tabelMedicamente)
        self.aspectVertical_11.addLayout(self.aspectVertical_11_2)
        ### end medicamente

        self.paginiWidget.addWidget(self.pAcasa)
        self.paginiWidget.addWidget(self.pMedici)
        self.paginiWidget.addWidget(self.pAsistente)
        self.paginiWidget.addWidget(self.pPacienti)
        self.paginiWidget.addWidget(self.pMedicamente)
        self.aspectVertical_4.addWidget(self.paginiWidget)
        self.aspectVertical.addWidget(self.baraContinut)

        ##############################################################################
        ## start butoane

        self.frameButoane = QFrame(self.cadruUmbra)
        self.frameButoane.setStyleSheet("background-color: transparent;")
        self.meniu = QHBoxLayout(self.frameButoane)
        self.bAcasa = QPushButton(self.frameButoane)
        ibutonAcasa = QIcon()
        ibutonAcasa.addPixmap(QPixmap("cil-home.png"), QIcon.Normal, QIcon.Off)
        self.bAcasa.setIcon(ibutonAcasa)
        self.bAcasa.setIconSize(QSize(24, 24))
        self.bAcasa.setCheckable(False)
        self.bAcasa.setDefault(False)
        self.bAcasa.setFlat(False)
            
        self.meniu.addWidget(self.bAcasa)

        self.bMedici = QPushButton(self.frameButoane)
        ibutonMedici = QIcon()
        ibutonMedici.addPixmap(QPixmap("cil-user.png"), QIcon.Normal, QIcon.Off)
        self.bMedici.setIcon(ibutonMedici)
        self.bMedici.setIconSize(QSize(24, 24))
        self.bMedici.setCheckable(False)
        self.bMedici.setDefault(False)
        self.bMedici.setFlat(False)

        self.meniu.addWidget(self.bMedici)

        self.bAsistente = QPushButton(self.frameButoane)
        ibutonAsistente = QIcon()
        ibutonAsistente.addPixmap(QPixmap("cil-user-female.png"), QIcon.Normal, QIcon.Off)
        self.bAsistente.setIcon(ibutonAsistente)
        self.bAsistente.setIconSize(QSize(24, 24))
        self.bAsistente.setCheckable(False)
        self.bAsistente.setDefault(False)
        self.bAsistente.setFlat(False)

        self.meniu.addWidget(self.bAsistente)

        self.bPacienti = QPushButton(self.frameButoane)
        ibutonPacienti = QIcon()
        ibutonPacienti.addPixmap(QPixmap("cil-newspaper.png"), QIcon.Normal, QIcon.Off)
        self.bPacienti.setIcon(ibutonPacienti)
        self.bPacienti.setIconSize(QSize(24, 24))
        self.bPacienti.setCheckable(False)
        self.bPacienti.setDefault(False)
        self.bPacienti.setFlat(False)

        self.meniu.addWidget(self.bPacienti)

        self.bMedicamente = QPushButton(self.frameButoane)
        ibutonMedicamente = QIcon()
        ibutonMedicamente.addPixmap(QPixmap("cil-plus.png"), QIcon.Normal, QIcon.Off)
        self.bMedicamente.setIcon(ibutonMedicamente)
        self.bMedicamente.setIconSize(QSize(24, 24))
        self.bMedicamente.setCheckable(False)
        self.bMedicamente.setDefault(False)
        self.bMedicamente.setFlat(False)        

        self.meniu.addWidget(self.bMedicamente)

        ## functionalitate butoane

        def defAcasa(self):
            print("acasa")
            self.paginiWidget.setCurrentIndex(0)

        def defMedici(self):
            print("medici")
            self.paginiWidget.setCurrentIndex(1)

        def defAsistente(self):
            print("asistente")
            self.paginiWidget.setCurrentIndex(2)

        def defMedicamente(self):
            print("medicamente")
            self.paginiWidget.setCurrentIndex(4)
        
        def defPacienti(self):
            print("pacienti")
            self.paginiWidget.setCurrentIndex(3)

        self.bAcasa.clicked.connect(lambda: defAcasa(self))
        self.bMedici.clicked.connect(lambda: defMedici(self))
        self.bAsistente.clicked.connect(lambda: defAsistente(self))
        self.bPacienti.clicked.connect(lambda: defPacienti(self))
        self.bMedicamente.clicked.connect(lambda: defMedicamente(self))

        ## end functionalitate butoane

        ## end butoane

        ## cadru
        self.aspectVertical_4.addWidget(self.paginiWidget)
        self.aspectVertical.addWidget(self.baraContinut)

        self.baraCredite = QFrame(self.cadruUmbra)
        self.baraCredite.setMaximumSize(QSize(16777215, 30))
        self.baraCredite.setStyleSheet(u"background-color: rgb(40, 54, 61);")
        self.baraCredite.setFrameShape(QFrame.NoFrame)
        self.baraCredite.setFrameShadow(QFrame.Raised)

        self.aspectOrizontal_3 = QHBoxLayout(self.baraCredite)
        self.aspectOrizontal_3.setSpacing(0)
        self.aspectOrizontal_3.setContentsMargins(0, 0, 0, 0)

        self.cadruEtichetaCredite = QFrame(self.baraCredite)
        self.cadruEtichetaCredite.setFrameShape(QFrame.StyledPanel)
        self.cadruEtichetaCredite.setFrameShadow(QFrame.Raised)

        self.aspectVertical_3 = QVBoxLayout(self.cadruEtichetaCredite)
        self.aspectVertical_3.setSpacing(0)
        self.aspectVertical_3.setContentsMargins(15, 0, 0, 0)
        
        self.etichetaCredite = QLabel(self.cadruEtichetaCredite)
        fontRoboto.setPointSize(10)
        self.etichetaCredite.setFont(fontRoboto)
        self.etichetaCredite.setStyleSheet(u"color: rgb(62, 182, 80);")

        self.aspectVertical_3.addWidget(self.etichetaCredite)
        self.aspectOrizontal_3.addWidget(self.cadruEtichetaCredite)

        self.prindereCadru = QFrame(self.baraCredite)
        self.prindereCadru.setMinimumSize(QSize(30, 30))
        self.prindereCadru.setMaximumSize(QSize(30, 30))
        self.prindereCadru.setStyleSheet(u"padding: 5px;")
        self.prindereCadru.setFrameShape(QFrame.StyledPanel)
        self.prindereCadru.setFrameShadow(QFrame.Raised)

        self.aspectOrizontal_3.addWidget(self.prindereCadru)

        self.aspectVertical.addWidget(self.frameButoane)
        self.aspectVertical.addWidget(self.baraCredite)
        self.aspectUmbra.addWidget(self.cadruUmbra)

        wnd.setCentralWidget(self.centralWidget)

        self.conecteazaObiecteDupaNume(wnd)

        self.paginiWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(wnd)

    def conecteazaObiecteDupaNume(self, wnd):
        wnd.setWindowTitle(QCoreApplication.translate("Atestat", u"Atestat", None))
        self.etichetaTitlu.setText(QCoreApplication.translate("Atestat", u"MedCYN", None))
        
        self.butonMareste.setToolTip(QCoreApplication.translate("Atestat", u"Mareste", None))
        self.butonMareste.setText("")
        self.butonMinimizeaza.setToolTip(QCoreApplication.translate("Atestat", u"Minimizeaza", None))
        self.butonMinimizeaza.setText("")
        self.butonInchide.setToolTip(QCoreApplication.translate("Atestat", u"Inchide", None))
        self.butonInchide.setText("")
        self.etichetaCredite.setText(QCoreApplication.translate("Atestat", u"Proiect Atestat - Zavoianu Gabriel", None))

class Fereastra_Search(QDialog):
    def __init__(self):
        super(Fereastra_Search, self).__init__()

        self.setWindowTitle("Search")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.medic_pacient_combo = QComboBox()
        optiuni = ["Selecteaza...", "Medic", "Pacient"]

        for i in range(len(optiuni)):
            self.medic_pacient_combo.addItem(optiuni[i])

        self.cauta_btn = QPushButton()
        self.cauta_btn.setText("Search")
        self.cauta_btn.clicked.connect(self.search_func)

        self.nume_input = QLineEdit()
        self.nume_input.setPlaceholderText("Introduceti numele")

        layout = QVBoxLayout()
        layout.addWidget(self.medic_pacient_combo)
        layout.addWidget(self.nume_input)
        layout.addWidget(self.cauta_btn)

        self.setLayout(layout)
    
    def optiune_schimbata(self):
        self.nume_input.clear()

        optiune_curenta = self.medic_pacient_combo.currentText()
        if optiune_curenta == "Pacient":
            self.baza_de_date = sqlite3.connect('sql/medcyn.db')
            self.binfo = self.baza_de_date.cursor()

            self.binfo.execute("SELECT `Nume` FROM `pacienti`")

            basic_list = []
            for (n, ) in self.binfo:
                basic_list.append(n)
            
            self.binfo.close()
            self.baza_de_date.close()

            self.auto_complete = QCompleter(basic_list)
            self.auto_complete.setCaseSensitivity(Qt.CaseInsensitive)

            self.nume_input.setCompleter(self.auto_complete)
        
        elif optiune_curenta == "Medic":
            self.baza_de_date = sqlite3.connect('sql/medcyn.db')
            self.binfo = self.baza_de_date.cursor()

            self.binfo.execute("SELECT `Nume` FROM `medici`")

            basic_list_2 = []
            for (n, ) in self.binfo:
                basic_list_2.append(n)

            self.binfo.close()
            self.baza_de_date.close()

            self.auto_complete = QCompleter(basic_list_2)
            self.auto_complete.setCaseSensitivity(Qt.CaseInsensitive)

            self.nume_input.setCompleter(self.auto_complete)
    
    def search_func(self):
        nume_introdus = self.nume_input.text()
        optiune_curenta = self.medic_pacient_combo.currentText()

        gasit, rezultat = False, None

        if optiune_curenta == "Pacient":
            self.baza_de_date = sqlite3.connect('sql/medcyn.db')
            self.binfo = self.baza_de_date.cursor()

            self.binfo.execute("SELECT `Nume`, `Varsta`, `Sectie`, `Bloc`, `Etaj`, `Camera`, `Afectiune`, `Perioada internare (zile)`, `Evolutie` FROM `pacienti` WHERE `Nume`=?", (str(nume_introdus), ))

            for (n, v, s, b, e, c, a, p, ev) in self.binfo:
                rezultat = "Nume: " + str(n) + '\n' + "Varsta: " + str(v) + '\n' + "Sectie: " + str(s) + '\n' + "Bloc: " + str(b) + '\n' + "Etaj: " + str(e) + '\n' + "Camera: " + str(c) + '\n' + "Afectiune: " + str(a) + '\n' + "Perioada internare (zile): " + str(p) + '\n' + "Evolutie: " + str(ev) + '\n'
                gasit = True

            self.binfo.close()
            self.baza_de_date.close()

            if (gasit == True):
                QMessageBox.information(QMessageBox(), "Pacient gasit!", rezultat)
            else:
                QMessageBox.warning(QMessageBox(), "Pacientul nu a fost gasit!", "Pacientul nu a fost gasit in baza de date (nume incorect?)")
        elif optiune_curenta == "Medic":
            self.baza_de_date = sqlite3.connect('sql/medcyn.db')
            self.binfo = self.baza_de_date.cursor()

            self.binfo.execute("SELECT `Nume`, `Sectie`, `Disponibil`, `Program lucru`, `Motiv` FROM `medici` WHERE `Nume`=?", (str(nume_introdus), ))

            for (n, s, d, p, m) in self.binfo:
                rezultat = "Nume: " + str(n) + '\n' + "Sectie: " + str(s) + '\n' + "Program de lucru: " + str(p) + '\n' + "Disponibil: " + str(d) + '\n' + "Motiv: " + str(m) + '\n'
                gasit = True

            self.binfo.close()
            self.baza_de_date.close()

            if (gasit == True):
                QMessageBox.information(QMessageBox(), "Medic gasit!", rezultat)
            else:
                QMessageBox.warning(QMessageBox(), "Medicul nu a fost gasit!", "Medicul nu a fost gasit in baza de date (nume incorect)?")

class ML_Medicamente(QDialog):
    def __init__(self):
        super(ML_Medicamente, self).__init__()

        self.setWindowTitle("Monitorizare MEDS")
        self.resize(500, 350)
        self.setMinimumSize(QSize(500, 350))


        self.sectie_combo = QComboBox()
        sectii = [
            "Cardiologie",
            "BoliInfectioase",
            "Pediatrie",
            "Chirurgie",
            "Psihiatrie"
        ]

        for i in range(len(sectii)):
            self.sectie_combo.addItem(sectii[i])
        
        self.ok_btn = QPushButton()
        self.ok_btn.setText("ok")

        self.ok_btn.clicked.connect(self.machine_learning)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sectie_combo)
        self.layout.addWidget(self.ok_btn)

        self.setLayout(self.layout)
    
    def machine_learning(self):
        current = self.sectie_combo.currentText()

        df = pandas.read_csv('csv/MedicamenteSCronica.csv')
        df['Sectie'] = df['Sectie'].apply(self.transform)

        x = df.drop(columns='target')
        y = df['target']

        model = DecisionTreeClassifier()
        model.fit(x, y)

        self.baza_de_date = sqlite3.connect('sql/medcyn.db')
        self.binfo = self.baza_de_date.cursor()

        self.binfo.execute("SELECT `Nume` FROM `medicamente` WHERE `Sectie`=?", (current, ))

        nume_medicament = []
        for (nume, ) in self.binfo:
            nume_medicament.append(nume)

        for i in range(len(nume_medicament)):
            self.binfo.execute("SELECT `Nume` FROM `pacienti` WHERE `Medicament administrat`=?", (nume_medicament[i], ))
            
            medicament_administrat_pacient = []
            for (medicament_administrat, ) in self.binfo:
                medicament_administrat_pacient.append(medicament_administrat)
            
            self.binfo.execute("SELECT `Cantitate` FROM `medicamente` WHERE `Nume`=?", (nume_medicament[i], ))
            cantitate_medicamente = []
            for (cantitate, ) in self.binfo:
                cantitate_medicamente.append(cantitate)
            
            numar_de_medicamente = cantitate_medicamente[0]
            numar_de_pacienti = len(medicament_administrat_pacient)
            
            predictie = model.predict([[self.transform(current), numar_de_pacienti, numar_de_medicamente]])

            rez = 0
            if predictie == 1:
                print(f"Nu e nevoie de medicamente pentru {current}")
                self.lb = QLabel()
                self.lb.setText(f"Pe sectia {current}: trebuie sa cumperi {rez} de tip {nume_medicament[i]}")
                self.layout.addWidget(self.lb)
            else:
                for a in range(numar_de_medicamente + 1, 500):
                    predictie_noua = model.predict([[self.transform(current), numar_de_pacienti, a]])
                    rez += 1
                    if predictie_noua == 1:
                        print(f"Pe sectia {current}: trebuie sa cumperi {rez} de tip {nume_medicament[i]}!")
                        
                        self.lb = QLabel()
                        self.lb.setText(f"Pe sectia {current}: trebuie sa cumperi {rez} de tip {nume_medicament[i]}!")
                        self.layout.addWidget(self.lb)

                        break

        self.binfo.close()
        self.baza_de_date.close()
    
    def transform(self, data):
        if data == 'Cardiologie':
            return 200
        if data == 'BoliInfectioase':
            return 250
        if data == 'Psihiatrie':
            return 400
        if data == 'Pediatrie':
            return 50
        if data == 'Chirurgie':
            return 300

class ML_Medic_Asistente(QDialog):
    def __init__(self):
        super(ML_Medic_Asistente, self).__init__()

        self.setWindowTitle("Monitorizare medici si asistente")

        self.resize(500, 150)
        self.setMinimumSize(QSize(500, 150))

        self.sectie_combo = QComboBox()
        sectii = [
            "Cardiologie",
            "BoliInfectioase",
            "Pediatrie",
            "Chirurgie",
            "Psihiatrie"
        ]
        for i in range(len(sectii)):
            self.sectie_combo.addItem(sectii[i])

        self.ok_btn = QPushButton()
        self.ok_btn.setText("ok")

        self.ok_btn.clicked.connect(self.machine_learning)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sectie_combo)
        self.layout.addWidget(self.ok_btn)

        self.setLayout(self.layout)

    def machine_learning(self):
        current = self.sectie_combo.currentText()

        df = pandas.read_csv('csv/medasis.csv')
        df['Sectie'] = df['Sectie'].apply(self.transform)

        x = df.drop(columns=['target'])
        y = df['target']

        model = DecisionTreeClassifier()
        model.fit(x, y)

        self.baza_de_date = sqlite3.connect('sql/medcyn.db')
        self.binfo = self.baza_de_date.cursor()

        self.binfo.execute("SELECT `Nume` FROM `pacienti` WHERE `Sectie`=?", (current, ))
        nume_pacient = []
        for (np, ) in self.binfo:
            nume_pacient.append(np)
        
        self.binfo.execute("SELECT `Nume` FROM `medici` WHERE `Sectie`=?", (current, ))
        nume_medic = []
        for (nm, ) in self.binfo:
            nume_medic.append(nm)
        
        self.binfo.execute("SELECT `Nume` FROM `asistente` WHERE `Sectie`=?", (current,))
        nume_asistent = []
        for (na, )in self.binfo:
            nume_asistent.append(na)
        
        self.binfo.close()
        self.baza_de_date.close()

        nume_sectie = current
        k_pacienti = len(nume_pacient)
        k_doctori = len(nume_medic)
        k_asistente = len(nume_asistent)

        print(f"{nume_sectie}:{k_pacienti}:{k_doctori}:{k_asistente}")

        predictie = model.predict([[
            self.transform(nume_sectie),
            k_pacienti,
            k_doctori,
            k_asistente
        ]])

        aux = 0
        if predictie == 1:
            self.lb = QLabel()
            self.lb.setText(
                "Numarul de doctori si de asistente aflati in spital raportat la numarul de pacienti este suficient."
            )
            self.layout.addWidget(self.lb)
        else:
            if model.predict([[self.transform(nume_sectie), k_pacienti, 25, k_asistente]]) == 1:
                aux = 1
            else:
                if model.predict([[self.transform(nume_sectie), k_pacienti, k_doctori, 40]]) == 1:
                    aux = 2
                else:
                    if model.precit([[self.transform(nume_sectie), k_pacienti, 25, 40]]) == 1:
                        aux = 3
        
        rez1, rez2, rez3, rez4 = 0, 0, 0, 0

        if aux == 1:
            for a in range(k_doctori + 1, 26):
                new_pred1 = model.predict([[self.transform(nume_sectie), k_pacienti, a, k_asistente]])
                rez1 += 1
                if new_pred1 == 1:
                    self.pred1 = QLabel()
                    self.pred1.setText("Pe sectia " + str(nume_sectie) + " personalul raportat la numarul de pacienti nu este indeajuns." + '\n' + "Numar aditional recomandat: " + '\n' +
                                       str(rez1) + " medici" + '\n' + " 0 asistente")
                    self.layout.addWidget(self.pred1)

                    break
        elif aux == 2:
            for a in range(k_asistente + 1, 41):
                new_pred2 = model.predict([[self.transform(nume_sectie), k_pacienti, k_doctori, a]])
                rez2 += 1
                if new_pred2 == 1:
                    self.pred2 = QLabel()
                    self.pred2.setText("Pe sectia " + str(nume_sectie) + " personalul raportat la numarul de pacienti nu este indeajuns." + '\n' + "Numar aditional recomandat: " + '\n' +
                                       "0 medici " + '\n' + str(rez2) + " asistente")

                    self.layout.addWidget(self.pred2)

                    break
        elif aux == 3:
            for a in range(k_doctori + 1, 26):
                new_pred3 = model.predict([[self.transform(nume_sectie), k_pacienti, a, 40]])
                rez3 += 1
                if new_pred3 == 1:
                    break
            for a in range(k_asistente + 1, 41):
                new_pred4 = model.predict([[self.transform(nume_sectie), k_pacienti, 25, a]])
                rez4 += 1
                if new_pred4 == 1:
                    self.pred3 = QLabel()
                    self.pred3.setText("Pe sectia " + str(nume_sectie) + " personalul raportat la numarul de pacienti nu este indeajuns." + '\n' + "Numar aditional recomandat: " + '\n' +
                                       str(rez3) + " medici" + '\n'  + str(rez4) + " asistente")
                    self.layout.addWidget(self.pred3)

                    break
    
    def transform(self, data):
        if data == 'Cardiologie':
            return 200
        if data == 'BoliInfectioase':
            return 250
        if data == 'Psihiatrie':
            return 400
        if data == 'Pediatrie':
            return 50
        if data == 'Chirurgie':
            return 300