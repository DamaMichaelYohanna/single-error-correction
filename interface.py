from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QHeaderView, QStackedWidget, QMainWindow
from PySide6.QtGui import QPixmap

from main import calculate_redundant_bits, calculate_parity_bits, position_redundant_bits, detect_error


class FirstPage(QMainWindow):
    def __init__(self):
        super(FirstPage, self).__init__()
        self.setWindowTitle("Single Error Correction.")
        self.setFixedSize(771, 600)
        self.stack = QStackedWidget()
        self.frame = QWidget()
        self.build_ui()

    def build_ui(self):
        label = QLabel()
        image_file = QPixmap("image.png")
        image_file.scaled(100, 100)
        label.setPixmap(image_file)
        self.text_entry = QLineEdit()
        self.text_entry.setPlaceholderText("Enter text Data to check")
        self.text_entry.setStyleSheet("padding:3px;font-size:15px;text-align:center;")
        # text_entry.setFixedWidth(500)
        button = QPushButton("Submit")
        button.setStyleSheet("padding:3px;font-size:15px;text-align:center;")
        button.clicked.connect(self.submit_data)
        # button.setFixedWidth(500)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(self.text_entry)
        layout.addWidget(button)
        layout.addStretch()
        self.frame.setLayout(layout)
        self.stack.addWidget(self.frame)

        self.setCentralWidget(self.stack)

    def submit_data(self):
        data = self.text_entry.text()
        if not data:
            pass
        else:
            redundant_bit = calculate_redundant_bits(len(data))
            array_of_redundant = position_redundant_bits(data, redundant_bit)
            parity_bit = calculate_parity_bits(array_of_redundant, redundant_bit)
            screen2 = SecondPage(self)
            self.stack.addWidget(screen2)
            self.stack.setCurrentIndex(1)
            print(parity_bit)


class SecondPage(QWidget):
    def __init__(self, first_page):
        super(SecondPage, self).__init__()
        self.setFixedSize(771, 600)
        self.first_page = first_page
        layout = QVBoxLayout()
        top = QHBoxLayout()
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back_to_home)
        text = QLabel("Program Out Put ")
        top.addWidget(back_button)
        top.addStretch()
        top.addWidget(text)
        top.addStretch()

        text.setAlignment(Qt.AlignCenter)
        text.setStyleSheet("padding:3px;font-size:15px;text-align:center;")
        heading = QHBoxLayout()
        label = QLabel("Message Sent")
        message = QLineEdit("hello world")
        message.setStyleSheet("padding:3px;font-size:15px;text-align:center;")
        error_input = QLineEdit()
        error_input.setStyleSheet("padding:3px;font-size:15px;text-align:center;")
        error_input.setPlaceholderText("Enter Error Message")
        button = QPushButton("Check Error")
        button.setStyleSheet("padding:5px;font-size:15px;text-align:center;")

        heading.addWidget(label)
        heading.addWidget(message)
        heading.addWidget(error_input)
        heading.addWidget(button)
        # ----------------------------------------------------------
        table = QTableWidget()
        table.setColumnCount(6)
        table.setRowCount(4)
        table.setHorizontalHeaderLabels(["Bit Position", "Bit Number", "Check bit",
                                         "Data bit", "Word stored", "Word fetched"])
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        layout.addLayout(top)
        layout.addLayout(heading)
        layout.addWidget(QHSeparationLine())
        layout.addWidget(table)
        # layout.addStretch()
        self.setLayout(layout)

    def back_to_home(self):
        print("i was clicked")
        self.first_page.stack.setCurrentIndex(0)


class QHSeparationLine(QtWidgets.QFrame):
    """draw a horizontal line"""

    def __init__(self):
        super(QHSeparationLine, self).__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        return


window = QApplication()
app = FirstPage()
app.show()
window.exec()
