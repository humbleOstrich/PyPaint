import random
import sqlite3
import sys
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QColorDialog, QFileDialog, \
    QInputDialog, QPlainTextEdit, QTableWidget, QTableWidgetItem, QLabel
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.f_dot = QtWidgets.QAction(MainWindow)
        self.f_dot.setObjectName("f_dot")
        self.f_line = QtWidgets.QAction(MainWindow)
        self.f_line.setObjectName("f_line")
        self.f_rect = QtWidgets.QAction(MainWindow)
        self.f_rect.setObjectName("f_rect")
        self.f_eraser = QtWidgets.QAction(MainWindow)
        self.f_eraser.setObjectName("f_eraser")
        self.f_circle = QtWidgets.QAction(MainWindow)
        self.f_circle.setObjectName("f_circle")
        self.f_emptyCircle = QtWidgets.QAction(MainWindow)
        self.f_emptyCircle.setObjectName("f_emptyCircle")
        self.f_color = QtWidgets.QAction(MainWindow)
        self.f_color.setObjectName("f_color")
        self.f_save = QtWidgets.QAction(MainWindow)
        self.f_save.setObjectName("f_save")
        self.f_info = QtWidgets.QAction(MainWindow)
        self.f_info.setObjectName("f_info")
        self.f_reviews = QtWidgets.QAction(MainWindow)
        self.f_reviews.setObjectName("f_reviews")
        self.f_make_review = QtWidgets.QAction(MainWindow)
        self.f_make_review.setObjectName("f_make_review")
        self.menu.addAction(self.f_dot)
        self.menu.addAction(self.f_line)
        self.menu.addAction(self.f_rect)
        self.menu.addAction(self.f_eraser)
        self.menu.addAction(self.f_circle)
        self.menu.addAction(self.f_emptyCircle)
        self.menu.addAction(self.f_color)
        self.menu_2.addAction(self.f_info)
        self.menu_2.addAction(self.f_reviews)
        self.menu_2.addAction(self.f_make_review)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.f_dot)
        self.toolBar.addAction(self.f_line)
        self.toolBar.addAction(self.f_rect)
        self.toolBar.addAction(self.f_eraser)
        self.toolBar.addAction(self.f_circle)
        self.toolBar.addAction(self.f_emptyCircle)
        self.toolBar.addAction(self.f_color)
        self.toolBar.addAction(self.f_save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Инструменты"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.f_dot.setText(_translate("MainWindow", "Точка"))
        self.f_line.setText(_translate("MainWindow", "Линия"))
        self.f_rect.setText(_translate("MainWindow", "Прямоугольник"))
        self.f_eraser.setText(_translate("MainWindow", "Ластик"))
        self.f_circle.setText(_translate("MainWindow", "Круг"))
        self.f_emptyCircle.setText(_translate("MainWindow", "Окружность"))
        self.f_color.setText(_translate("MainWindow", "Выбор цвета"))
        self.f_save.setText(_translate("MainWindow", "Сохранить изображение"))
        self.f_info.setText(_translate("MainWindow", "Информация о приложении"))
        self.f_reviews.setText(_translate("MainWindow", "Отзывы о приложении"))
        self.f_make_review.setText(_translate("MainWindow", "Оставить отзыв"))


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.new_brush = QBrush(QColor(0, 0, 0))
        self.new_pen = QPen(QColor(0, 0, 0))

    def draw(self, painter):
        painter.setBrush(self.new_brush)
        painter.setPen(self.new_pen)
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)

    def set_color(self, new_color):
        self.new_brush = QBrush(new_color)
        self.new_pen = QPen(new_color)


class Line:

    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.new_brush = QBrush(QColor(0, 0, 0))
        self.new_pen = QPen(QColor(0, 0, 0))

    def draw(self, painter):
        painter.setBrush(self.new_brush)
        painter.setPen(self.new_pen)
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)

    def set_color(self, new_color):
        self.new_brush = QBrush(new_color)
        self.new_pen = QPen(new_color)


class Circle:

    def __init__(self, cx, cy, x, y):
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y
        self.new_brush = QBrush(QColor(0, 0, 0, 0))
        self.new_pen = QPen(QColor(0, 0, 0))

    def draw(self, painter):
        painter.setBrush(self.new_brush)
        painter.setPen(self.new_pen)
        rad = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - rad, self.cy - rad, 2 * rad, 2 * rad)

    def set_color(self, new_color):
        self.new_brush = QBrush(new_color)
        self.new_pen = QPen(new_color)


class EmptyCircle:
    def __init__(self, cx, cy, x, y):
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y
        self.new_brush = QBrush(QColor(0, 0, 0, 0))
        self.new_pen = QPen(QColor(0, 0, 0))

    def draw(self, painter):
        painter.setBrush(self.new_brush)
        painter.setPen(self.new_pen)
        rad = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - rad, self.cy - rad, 2 * rad, 2 * rad)

    def set_color(self, new_color):
        self.new_pen = QPen(new_color)


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.new_brush = QBrush(QColor(0, 0, 0, 0))
        self.new_pen = QPen(QColor(0, 0, 0))

    def draw(self, painter):
        painter.setBrush(self.new_brush)
        painter.setPen(self.new_pen)
        painter.drawRect(self.x, self.y, self.width, self.height)

    def set_color(self, new_color):
        self.new_brush = QBrush(new_color)
        self.new_pen = QPen(new_color)


class Eraser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.new_brush = QBrush(QColor(240, 240, 240))
        self.new_pen = QPen(QColor(240, 240, 240))

    def draw(self, painter):
        painter.setBrush(self.new_brush)
        painter.setPen(self.new_pen)
        painter.drawEllipse(self.x - 20, self.y - 20, 40, 40)

    def set_color(self, new_color):
        self.new_brush = QBrush(new_color)
        self.new_pen = QPen(new_color)


class Canvas(QWidget):
    def __init__(self):
        super(Canvas, self).__init__()
        self.objects = []
        self.instrument = "dot"
        self.color_brush = QColor(0, 0, 0)
        self.directory = 0

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for i in self.objects:
            el = i[0]
            color = i[1]
            el.set_color(color)
            el.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        if self.instrument == "dot":
            self.objects.append((Dot(event.x(), event.y()), self.color_brush))
            self.update()

        elif self.instrument == "line":
            self.objects.append((Line(event.x(), event.y(), event.x(), event.y()), self.color_brush))
            self.update()

        elif self.instrument == "circle":
            self.objects.append((Circle(event.x(), event.y(), event.x(), event.y()), self.color_brush))
            self.update()

        elif self.instrument == 'rectangle':
            self.objects.append((Rectangle(event.x(), event.y(), 5, 5), self.color_brush))
            self.update()

        elif self.instrument == 'eraser':
            self.objects.append((Eraser(event.x(), event.y()), QColor(240, 240, 240)))
            self.update()

        elif self.instrument == "empty_circle":
            self.objects.append((EmptyCircle(event.x(), event.y(), event.x(), event.y()), self.color_brush))
            self.update()

    def mouseMoveEvent(self, event):
        if self.instrument == "dot":
            self.objects.append((Dot(event.x(), event.y()), self.color_brush))
            self.update()

        elif self.instrument == "line":
            self.objects[-1][0].ex = event.x()
            self.objects[-1][0].ey = event.y()
            self.update()

        elif self.instrument == "circle":
            self.objects[-1][0].x = event.x()
            self.objects[-1][0].y = event.y()
            self.update()

        elif self.instrument == 'rectangle':
            self.objects[-1][0].width = abs(event.x() - self.objects[-1][0].x)
            self.objects[-1][0].height = abs(event.y() - self.objects[-1][0].y)
            self.update()

        elif self.instrument == 'eraser':
            self.objects.append((Eraser(event.x(), event.y()), QColor(240, 240, 240)))
            self.update()

        elif self.instrument == "empty_circle":
            self.objects[-1][0].x = event.x()
            self.objects[-1][0].y = event.y()
            self.update()

    def setDot(self):
        self.instrument = "dot"

    def setLine(self):
        self.instrument = "line"

    def setRectangle(self):
        self.instrument = 'rectangle'

    def setEraser(self):
        self.instrument = "eraser"

    def setCircle(self):
        self.instrument = "circle"

    def setEmptyCircle(self):
        self.instrument = "empty_circle"

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_brush = color


class InformationForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Информация о приложении')
        self.setMaximumSize(500, 500)
        self.font = QFont("Colibri", 17, 3, False)
        self.font.bold()
        self.text_field = QPlainTextEdit(self)
        self.text_field.setCursorWidth(7)
        self.text_field.resize(500, 500)
        self.text_field.setEnabled(False)
        self.info_storage = open("instructions.txt", encoding="utf-8")
        self.text_field.setPlainText(str("".join(self.info_storage.readlines())))
        self.text_field.setFont(self.font)


class ReviewForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Отзывы о приложении')
        self.setMaximumSize(300, 300)
        self.tableWidget = QTableWidget(self)
        self.rect = QRect(0, 0, 300, 300)
        self.tableWidget.setGeometry(self.rect)
        self.tableWidget.move(0, 0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["имя", "отзыв"])

    def add_reviews(self, data):
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
            self.color_row(i, QColor(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        self.tableWidget.resizeColumnsToContents()

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


class PictureForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args[1])

    def initUI(self, directory):
        self.setGeometry(700, 500, 700, 500)
        self.setWindowTitle('PyPaint хочет стать лучше!')
        self.setMaximumSize(700, 500)
        self.directory = directory
        self.text_field = QPlainTextEdit(self)
        self.text_field.resize(200, 200)
        self.text_field.move(0, 0)
        self.text_field.setEnabled(False)
        self.font = QFont("Colibri", 17, 3, False)
        self.font.bold()
        self.text_field.setFont(self.font)
        self.text_field.setPlainText("До встречи! PyPaint надеется, "
                                     "что в следующий раз вы не станете скрывать свое мнение!")
        self.img = Image.open(self.directory)
        self.img = self.img.resize((500, 500))
        self.img.save(self.directory)
        self.pixmap = QPixmap(self.directory)
        self.image = QLabel(self)
        self.image.move(200, 0)
        self.image.resize(500, 500)
        self.image.setPixmap(self.pixmap)


class NotificationForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setMaximumSize(300, 300)
        self.setWindowTitle('Уведомление')
        self.text_field = QPlainTextEdit(self)
        self.text_field.resize(300, 300)
        self.text_field.setEnabled(False)
        self.font = QFont("Colibri", 17, 3, False)
        self.font.bold()

    def display_notification(self, notification):
        self.text_field.setPlainText(notification)
        self.text_field.setFont(self.font)


class MainWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCentralWidget(Canvas())
        self.initUI()
        self.f_dot.triggered.connect(self.centralWidget().setDot)
        self.f_line.triggered.connect(self.centralWidget().setLine)
        self.f_rect.triggered.connect(self.centralWidget().setRectangle)
        self.f_eraser.triggered.connect(self.centralWidget().setEraser)
        self.f_circle.triggered.connect(self.centralWidget().setCircle)
        self.f_emptyCircle.triggered.connect(self.centralWidget().setEmptyCircle)
        self.f_color.triggered.connect(self.centralWidget().choose_color)
        self.f_save.triggered.connect(self.save_file)
        self.f_info.triggered.connect(self.show_info)
        self.f_reviews.triggered.connect(self.show_reviews)
        self.f_make_review.triggered.connect(self.update_reviews)

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("PyPaint")
        self.status = False
        self.directory = ""
        self.connection = sqlite3.connect("pypaint_database.db")
        answer, ok_pressed = QInputDialog.getItem(
            self, "Добро пожаловать!", "Впервые используете PyPaint?", ("Да",
                                                                        "Нет"), 1, False)
        if answer == "Да":
            self.welcome()

    def welcome(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Как тебя зовут?")
        if self.check_name(name):
            self.write_name(name)
            self.name = name
            self.status = True
        else:
            self.notification_form = NotificationForm(self)
            self.notification_form.show()
            self.notification_form.display_notification("Похоже, такое имя уже существует. "
                                                        "Попробуйте другой вариант")
            self.welcome()

    def check_name(self, name):
        cur = self.connection.cursor()
        names = cur.execute("""SELECT name FROM Reviews""").fetchall()
        for i in names:
            for j in i:
                if j == name:
                    return False
        else:
            return True

    def show_info(self):
        self.information_form = InformationForm(self)
        self.information_form.show()

    def save_file(self):
        directory, ok_pressed = QFileDialog.getSaveFileName(self, "Сохранить изображение", "",
                                                            "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)")
        self.directory = directory

    def keyPressEvent(self, event):
        if event.matches(QtGui.QKeySequence.Save):
            if self.directory:
                screen = pyautogui.screenshot(self.directory)
                if self.status:
                    review, ok_pressed = QInputDialog.getText(self, "Обратная связь",
                                                              "Оставьте отзыв о PyPaint!")
                    if len(review) == 0:
                        self.show_picture()
                    self.write_reviews(review)
                else:
                    self.notification_form = NotificationForm(self)
                    self.notification_form.show()
                    self.notification_form.display_notification("Рисунок был успешно сохранен!")
            else:
                self.notification_form = NotificationForm(self)
                self.notification_form.show()
                self.notification_form.display_notification("Похоже, вы неверно указали место для сохранения файла!\n"
                                                            "Попробуйте еще раз!")
        if event.matches(QtGui.QKeySequence.Undo):
            if self.centralWidget().objects:
                del self.centralWidget().objects[-1]
                self.centralWidget().update()

    def update_reviews(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Введите то имя, которое использовали при регистрации")
        cur = self.connection.cursor()
        names = cur.execute("""SELECT name FROM Reviews""").fetchall()
        if not self.check_name(name):
            review, ok_pressed = QInputDialog.getText(self, "Обратная связь",
                                                      "Оставьте отзыв о PyPaint!")
            cur.execute("""UPDATE Reviews
            SET review = ? 
            WHERE name = ?""", (str(review), str(name)))
            self.connection.commit()
        else:
            self.notification_form = NotificationForm(self)
            self.notification_form.show()
            self.notification_form.display_notification("Похоже, вы ошиблись\n"
                                                        "Попробуйте еще раз!")

    def write_name(self, name):
        cur = self.connection.cursor()
        cur.execute("""INSERT INTO Reviews (name) VALUES (?)""", (str(name),))
        self.connection.commit()

    def write_reviews(self, review):
        cur = self.connection.cursor()
        cur.execute("""UPDATE Reviews
        SET review = ?
        WHERE name = ?""", (str(review), str(self.name)))
        self.connection.commit()

    def show_reviews(self):
        cur = self.connection.cursor()
        reviews = cur.execute("""SELECT name, review FROM Reviews
        WHERE review NOT LIKE ''""").fetchall()
        self.review_form = ReviewForm(self)
        self.review_form.show()
        self.review_form.add_reviews(reviews)

    def show_picture(self):
        cur = self.connection.cursor()
        pictures = cur.execute("""SELECT directory FROM Pictures""").fetchall()
        directory = pictures[random.randint(0, 3)][0]
        self.picture_form = PictureForm(self, directory)
        self.picture_form.show()

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
