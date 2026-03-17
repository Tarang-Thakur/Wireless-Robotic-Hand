import numpy as np


class FingerAngles:

    def __init__(self):
        pass

    def calculate_angle(self, a, b, c):

        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        ba = a - b
        bc = c - b

        cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))

        angle = np.degrees(np.arccos(cos_angle))

        return angle

    def get_finger_angles(self, landmarks):

        if landmarks is None:
            return None

        angles = {}

        # THUMB
        angles["thumb"] = self.calculate_angle(
            landmarks[1], landmarks[2], landmarks[4]
        )

        # INDEX
        angles["index"] = self.calculate_angle(
            landmarks[5], landmarks[6], landmarks[8]
        )

        # MIDDLE
        angles["middle"] = self.calculate_angle(
            landmarks[9], landmarks[10], landmarks[12]
        )

        # RING
        angles["ring"] = self.calculate_angle(
            landmarks[13], landmarks[14], landmarks[16]
        )

        # PINKY
        angles["pinky"] = self.calculate_angle(
            landmarks[17], landmarks[18], landmarks[20]
        )

        return angles

    def angles_to_servos(self, angles):

        if angles is None:
            return None

        servo_values = {}

        for finger in angles:

            angle = angles[finger]

            servo = int(np.interp(angle, [60, 180], [180, 0]))

            servo_values[finger] = servo

        return servo_values