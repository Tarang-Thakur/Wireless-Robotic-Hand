import sys
import cv2

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from vision.hand_tracker import HandTracker
from processing.finger_angles import FingerAngles
from communication.mqtt_client import TCPClient
from ui.dashboard import Dashboard


class App:

    def __init__(self):

        self.tracker = HandTracker()
        self.processor = FingerAngles()
        self.tcp = TCPClient()

        self.dashboard = Dashboard()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.dashboard.start_button.clicked.connect(self.start)
        self.dashboard.stop_button.clicked.connect(self.stop)

    def start(self):

        self.tcp.connect()

        self.dashboard.update_status(self.tcp.connected)

        self.timer.start(30)

    def stop(self):

        self.timer.stop()

    def update(self):

        frame, landmarks = self.tracker.get_frame()

        if frame is None:
            return

        angles = self.processor.get_finger_angles(landmarks)
        servos = self.processor.angles_to_servos(angles)

        if servos is not None:

            if self.tcp.connected:
                self.tcp.send_servos(servos)

            self.dashboard.update_servos(servos)

        self.dashboard.update_status(self.tcp.connected)

        self.dashboard.update_camera(frame)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    program = App()

    program.dashboard.show()

    sys.exit(app.exec())