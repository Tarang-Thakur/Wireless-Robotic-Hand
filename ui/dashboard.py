from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Robotic Hand Vision Controller")
        self.setGeometry(100, 100, 1000, 600)

        self.build_ui()

    def build_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel("ROBOTIC HAND VISION CONTROLLER")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:22px;font-weight:bold;")

        main_layout.addWidget(title)

        content_layout = QHBoxLayout()

        # Camera feed
        self.camera_label = QLabel()
        self.camera_label.setFixedSize(640, 480)

        content_layout.addWidget(self.camera_label)

        # Servo values panel
        servo_layout = QVBoxLayout()

        self.thumb_label = QLabel("Thumb : 0")
        self.index_label = QLabel("Index : 0")
        self.middle_label = QLabel("Middle : 0")
        self.ring_label = QLabel("Ring : 0")
        self.pinky_label = QLabel("Pinky : 0")

        servo_layout.addWidget(self.thumb_label)
        servo_layout.addWidget(self.index_label)
        servo_layout.addWidget(self.middle_label)
        servo_layout.addWidget(self.ring_label)
        servo_layout.addWidget(self.pinky_label)

        content_layout.addLayout(servo_layout)

        main_layout.addLayout(content_layout)

        # Buttons
        self.status_label = QLabel("Connection : Disconnected")
        self.status_label.setStyleSheet("font-size:14px;color:red;")

        main_layout.addWidget(self.status_label)


        button_layout = QHBoxLayout()

        self.start_button = QPushButton("Start Tracking")
        self.stop_button = QPushButton("Stop Tracking")

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def update_camera(self, frame):

        height, width, channel = frame.shape

        bytes_per_line = 3 * width

        q_img = QImage(
            frame.data,
            width,
            height,
            bytes_per_line,
            QImage.Format_BGR888
        )

        self.camera_label.setPixmap(QPixmap.fromImage(q_img))

    def update_servos(self, servos):

        if servos is None:
            return

        self.thumb_label.setText(f"Thumb : {servos['thumb']}")
        self.index_label.setText(f"Index : {servos['index']}")
        self.middle_label.setText(f"Middle : {servos['middle']}")
        self.ring_label.setText(f"Ring : {servos['ring']}")
        self.pinky_label.setText(f"Pinky : {servos['pinky']}")

    def update_status(self, status):

        if status:
            self.status_label.setText("Connection : Connected")
            self.status_label.setStyleSheet("color:green;")
        else:
            self.status_label.setText("Connection : Disconnected")
            self.status_label.setStyleSheet("color:red;")