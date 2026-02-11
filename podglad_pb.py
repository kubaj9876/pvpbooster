
from PyQt5 import QtCore, QtGui, QtWidgets
import threading, win32gui, time
from test_wc import WindowCapture
import win32gui



hwid_list = []

class Ui_MainWindow(object):
        
        hwids = []
        windows_found = []
        list_widget_list = []
        current_window = 0
        delay = 1
        running = True
        
        def get_windows_name(self, hwnd, ctx ):
                window_text = win32gui.GetWindowText(hwnd)
                if win32gui.IsWindowVisible( hwnd ):
                        if "Minecraft 1" in window_text:
                                if "-" in window_text:
                                        pass
                                else:
                                        if f'{hwnd}:{window_text}' in self.windows_found:
                                                pass
                                        else:
                                                self.windows_found.append(f"{hwnd}:{window_text}")

        def detect_windows(self):
                self.windows_found = []
                win32gui.EnumWindows(self.get_windows_name, None )
                self.listWidget.clear()
                for window_name in self.windows_found:
                        self.listWidget.addItem(window_name)
        
        
        def update_screen(self):
                if len(self.listWidget.selectedItems()) > 0:                
                        hwid = self.listWidget.selectedItems()[0].text()
                        
                        wincap = WindowCapture(int(hwid))
                        while True:
                                if self.current_window == int(hwid) and self.running == True:
                                        screenshot = wincap.get_screenshot()
                                        self.label.setPixmap(QtGui.QPixmap(f"mc.png"))
                                        self.label.show()
                                        time.sleep(self.delay / 100)
                                else:
                                        break
                        
        def update_fps(self):
                if len(self.listWidget.selectedItems()) > 0:
                        self.current_window = int(self.listWidget.selectedItems()[0].text())
                        threading.Thread(target=self.update_screen).start()
                else:
                        pass #current window
        
        def update_hwid_list(self):
                self.detect_windows()
                index = 0
                self.listWidget.clear()
                for hwid in self.windows_found:
                        hwid_int = hwid.split(':')[0]
                        item = QtWidgets.QListWidgetItem()
                        self.listWidget.addItem(item)
                        item = self.listWidget.item(index)
                        item.setText(str(hwid_int))
                        index += 1
        
        def update_fps_value(self):
                self.delay = self.horizontalSlider.value()
                self.label_2.setText(f"Prędkość odświeżania: {self.horizontalSlider.value()}")
        
        def close_app(self):
                self.running = False
                self.close()
        
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(880, 580)
                MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(20, 20, 800, 500))
                self.frame.setStyleSheet("QWidget {\n"
                "    background-color: rgb(30, 30 ,30);\n"
                "    border-radius: 20px;\n"
                "}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.window_bar_frame = QtWidgets.QFrame(self.frame)
                self.window_bar_frame.setGeometry(QtCore.QRect(0, 0, 800, 35))
                self.window_bar_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(0, 0, 0);\n"
                "    border-top-left-radius: 20px;\n"
                "    border-top-right-radius: 20px;\n"
                "    border-bottom-left-radius: 0px;\n"
                "    border-bottom-right-radius: 0px;\n"
                "    border-bottom: 1px solid rgb(40, 40, 40);\n"
                "}")
                self.window_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.window_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.window_bar_frame.setObjectName("window_bar_frame")
                self.window_bar_pvp_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_pvp_label.setGeometry(QtCore.QRect(20, 7, 25, 20))
                self.window_bar_pvp_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    color: white;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.window_bar_pvp_label.setAlignment(QtCore.Qt.AlignCenter)
                self.window_bar_pvp_label.setObjectName("window_bar_pvp_label")
                self.window_bar_booster_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_booster_label.setGeometry(QtCore.QRect(45, 7, 50, 20))
                self.window_bar_booster_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    color: rgb(0, 255, 0);\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.window_bar_booster_label.setAlignment(QtCore.Qt.AlignCenter)
                self.window_bar_booster_label.setObjectName("window_bar_booster_label")
                self.window_bar_pvpbooster_przedzial_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_pvpbooster_przedzial_label.setGeometry(QtCore.QRect(110, 6, 1, 23))
                self.window_bar_pvpbooster_przedzial_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    background: rgb(30, 30, 30);\n"
                "}")
                self.window_bar_pvpbooster_przedzial_label.setText("")
                self.window_bar_pvpbooster_przedzial_label.setObjectName("window_bar_pvpbooster_przedzial_label")
                self.window_bar_minimize_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
                self.window_bar_minimize_pushbutton.clicked.connect(lambda: self.showMinimized())
                self.window_bar_minimize_pushbutton.setGeometry(QtCore.QRect(730, 8, 20, 20))
                self.window_bar_minimize_pushbutton.setStyleSheet("QPushButton {\n"
                "    border-radius: 5px;\n"
                "    background-color: none;\n"
                "    image: url(img/subtract.png);\n"
                "}")
                self.window_bar_minimize_pushbutton.setText("")
                self.window_bar_minimize_pushbutton.setObjectName("window_bar_minimize_pushbutton")
                self.window_bar_maximize_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
                self.window_bar_maximize_pushbutton.clicked.connect(lambda: self.close_app())
                self.window_bar_maximize_pushbutton.setGeometry(QtCore.QRect(760, 8, 20, 20))
                self.window_bar_maximize_pushbutton.setStyleSheet("QPushButton {\n"
                "    border-radius: 5px;\n"
                "    background-color: none;\n"
                "    image: url(img/close.png);\n"
                "}")
                self.window_bar_maximize_pushbutton.setText("")
                self.window_bar_maximize_pushbutton.setObjectName("window_bar_maximize_pushbutton")
                self.window_bar_status_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_status_label.setGeometry(QtCore.QRect(125, 7, 80, 20))
                self.window_bar_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.window_bar_status_label.setObjectName("window_bar_status_label")
                self.pages_frame = QtWidgets.QFrame(self.frame)
                self.pages_frame.setGeometry(QtCore.QRect(0, 35, 71, 465))
                self.pages_frame.setStyleSheet("QFrame {\n"
                "    border-right: 1px solid rgb(20, 20, 20);\n"
                "    background-color: rgb(45, 45, 45);\n"
                "    border-top-left-radius: 0px;\n"
                "    border-top-right-radius: 0px;\n"
                "    border-bottom-left-radius: 20px;\n"
                "    border-bottom-right-radius: 0px;\n"
                "}")
                self.pages_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.pages_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.pages_frame.setObjectName("pages_frame")
                self.listWidget = QtWidgets.QListWidget(self.pages_frame)
                self.listWidget.setGeometry(QtCore.QRect(0, 0, 71, 411))
                self.listWidget.setStyleSheet("QListWidget {\n"
                "    outline: 0;\n"
                "    color: white;\n"
                "    padding-top: 7px;\n"
                "    padding-bottom: 7px;\n"
                "    padding-left: 5px;\n"
                "    padding-right: 5px;\n"
                "}\n"
                "QListView::item {\n"
                "    border: 0px;\n"
                "    outline: 0;\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QListView::item:selected{\n"
                "    color: white;\n"
                "    background-color: rgb(0, 100, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QListView::item:hover {\n"
                "    background-color: rgb(0, 120, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QScrollBar:vertical {\n"
                "    background-color: rgb(30, 30, 30);\n"
                "    width: 10px;\n"
                "    border: 0px;\n"
                "}\n"
                "QScrollBar::handle:vertical {    \n"
                "    background-color: rgb(0, 180, 0);\n"
                "    width: 10px;\n"
                "    border-radius: 5px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::sub-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::add-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}")
                self.listWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
                self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
                self.listWidget.setObjectName("listWidget")
                #self.listWidget.setCurrentItem(item)
                self.listWidget.itemSelectionChanged.connect(self.update_fps)
                self.pushButton = QtWidgets.QPushButton(self.pages_frame)
                self.pushButton.setObjectName(u"pushButton")
                self.pushButton.setGeometry(QtCore.QRect(6, 420, 60, 25))
                self.pushButton.setStyleSheet("QPushButton{\n"
                "	color: white;\n"
                "	border-radius: 5px;\n"
                "}")
                self.pushButton.clicked.connect(lambda: self.update_hwid_list())
                self.frame_2 = QtWidgets.QFrame(self.frame)
                self.frame_2.setGeometry(QtCore.QRect(110, 70, 651, 395))
                self.frame_2.setStyleSheet("QFrame{\n"
                "    border-radius: 0px;\n"
                "}")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.label = QtWidgets.QLabel(self.frame_2)
                self.label.setGeometry(QtCore.QRect(0, 0, 651, 395))
                self.label.setText("")
                self.label.setObjectName("label")
                self.horizontalSlider = QtWidgets.QSlider(self.frame)
                self.horizontalSlider.setObjectName(u"horizontalSlider")
                self.horizontalSlider.setGeometry(QtCore.QRect(282, 461, 160, 22))
                self.horizontalSlider.setStyleSheet("QSlider {\n"
                "	background-color: rgb(30, 30 ,30);\n"
                "	margin: 0px;\n"
                "	border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "	border-radius: 5px;\n"
                "	height: 10px;\n"
                "	margin: 0px;\n"
                "	background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "	background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "	border: none;\n"
                "	height: 10px;\n"
                "	width: 10px;\n"
                "	margin: 0px;\n"
                "	border-radius: 5px;\n"
                "	background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "	background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "	background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "	border-radius: 5px;\n"
                "	height: 10px;\n"
                "	margin: 0px;\n"
                "	background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "	background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "	border: none;\n"
                "	height: 10px;\n"
                "	width: 10px;\n"
                "	margin: 0px;\n"
                "	border-radi"
                                        "us: 5px;\n"
                "	background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "	background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "	background-color: rgb(10, 150, 10);\n"
                "}")
                self.horizontalSlider.setMinimum(1)
                self.horizontalSlider.setMaximum(50)
                self.horizontalSlider.setValue(1)
                self.horizontalSlider.valueChanged.connect(lambda: self.update_fps_value())
                self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setObjectName(u"label_2")
                self.label_2.setGeometry(QtCore.QRect(100, 460, 181, 21))
                self.label_2.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                MainWindow.setCentralWidget(self.centralwidget)
                self.update_hwid_list()
                self.running = True
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.window_bar_pvp_label.setText(_translate("MainWindow", "pvp"))
                self.window_bar_booster_label.setText(_translate("MainWindow", "booster"))
                self.window_bar_status_label.setText(_translate("MainWindow", "Podgląd"))
                __sortingEnabled = self.listWidget.isSortingEnabled()
                self.listWidget.setSortingEnabled(False)
                self.listWidget.setSortingEnabled(__sortingEnabled)
                self.pushButton.setText(_translate("MainWindow", "Odśwież"))
                self.label_2.setText(_translate("MainWindow", "Prędkość odświeżania: 1"))

class MoveWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.offset = None
        self.window_bar_frame.installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.window_bar_frame:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                self.move(self.pos() - self.offset + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        return super().eventFilter(source, event)

def open_preview():
        win = MoveWindow()
        win.show()

        
