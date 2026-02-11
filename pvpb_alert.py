from PyQt5 import QtCore, QtGui, QtWidgets
import time

alert = 'test'
alert_type = 'info'

class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent, bg1, bg2, c1, c2, c3, c4):
        #bg1 = background-color
        #bg2 = background-color:hover
        
        self.background_1 = bg1
        self.background_2 = bg2
        self.color_1 = c1
        self.color_2 = c2
        self.color_3 = c3
        self.color_4 = c4
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor(self.background_2),
            endValue=QtGui.QColor(self.background_1),
            valueChanged=self._on_value_changed,
            duration=100,
        )
        self._update_stylesheet(QtGui.QColor(self.background_1), QtGui.QColor(self.background_2), QtGui.QColor(self.color_1))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QtGui.QColor(self.color_1)
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor(self.color_2)
        )
        foreground2 = (
            QtGui.QColor(self.color_3)
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor(self.color_4)
        )
        self._update_stylesheet(color, foreground, foreground2)

    def _update_stylesheet(self, background, foreground, foreground2):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            border-radius: 10px;
            color: %s;
            text-align: center;
            text-decoration: none;
            border: 1px solid %s;
            outline: 0;
        }
        """
            % (background.name(), foreground2.name(), foreground.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)
        time.sleep(0.01)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)
        time.sleep(0.01)

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 230)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 350, 150))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(30, 30 ,30);\n"
"    border-radius: 20px;\n"
"}")
        self.widget.setObjectName("widget")
        self.window_bar_frame = QtWidgets.QFrame(self.widget)
        self.window_bar_frame.setGeometry(QtCore.QRect(0, 0, 350, 26))
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
        self.window_bar_pvp_label.setGeometry(QtCore.QRect(20, 3, 25, 20))
        self.window_bar_pvp_label.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: white;\n"
"    font: 10pt \"Bahnschrift SemiBold\";\n"
"}")
        self.window_bar_pvp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.window_bar_pvp_label.setObjectName("window_bar_pvp_label")
        self.window_bar_booster_label = QtWidgets.QLabel(self.window_bar_frame)
        self.window_bar_booster_label.setGeometry(QtCore.QRect(41, 3, 50, 20))
        self.window_bar_booster_label.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(0, 255, 0);\n"
"    font: 10pt \"Bahnschrift SemiBold\";\n"
"}")
        self.window_bar_booster_label.setAlignment(QtCore.Qt.AlignCenter)
        self.window_bar_booster_label.setObjectName("window_bar_booster_label")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(10, 35, 90, 90))
        if alert_type == 'info':
            self.frame_2.setStyleSheet("QFrame{\n"
            "    background-color: none;\n"
            "    image: url(img/info_green.png);\n"
            "}")
        elif alert_type == 'error':
            self.frame_2.setStyleSheet("QFrame{\n"
            "    background-color: none;\n"
            "    image: url(img/error_green.png);\n"
            "}")
        elif alert_type == 'done':
            self.frame_2.setStyleSheet("QFrame{\n"
            "    background-color: none;\n"
            "    image: url(img/done_green.png);\n"
            "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 45, 200, 60))
        self.label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font: 11pt \"Bahnschrift SemiBold\";\n"
"}")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = PushButton(self.widget, "#3c3c3c", "#00ff00", "#1e1e1e", "#464646", 'white', 'black')
        self.pushButton.setGeometry(QtCore.QRect(260, 110, 60, 25))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 300 5 \"Arial\";\n"
"    color: white;\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(30, 30, 30);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton.clicked.connect(lambda: self.close())
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.window_bar_pvp_label.setText(_translate("MainWindow", "pvp"))
        self.window_bar_booster_label.setText(_translate("MainWindow", "booster"))
        self.label.setText(_translate("MainWindow", f"{alert}"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

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

def open_alert():
    win = MoveWindow()
    win.show()
