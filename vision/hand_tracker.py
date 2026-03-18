import cv2
from mediapipe.python.solutions import hands, drawing_utils

class HandTracker:

    def __init__(self,
                 max_hands=1,
                 detection_confidence=0.7,
                 tracking_confidence=0.6):

        self.cap = cv2.VideoCapture(0)

        self.mp_hands = hands
        self.mp_draw = drawing_utils

        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

    def get_frame(self):

        success, frame = self.cap.read()

        if not success:
            return None, None

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        landmarks = None

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]

            self.mp_draw.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            landmarks = []

            for lm in hand.landmark:
                landmarks.append((lm.x, lm.y, lm.z))

        return frame, landmarks