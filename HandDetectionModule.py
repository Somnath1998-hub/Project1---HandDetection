import time
import cv2
import mediapipe as mp 


class HandDetection():
    def __init__(self, image_mode = False, max_num_hands = 2, model_complexity = 1,
     min_detection_confi = 0.5, min_tracking_confi = 0.5):

        self.image_mode = image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confi = min_detection_confi
        self.min_tracking_confi = min_tracking_confi

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.image_mode,
                                        self.max_num_hands,
                                        self.model_complexity,
                                        self.min_detection_confi,
                                        self.min_tracking_confi)

        self.mp_draw = mp.solutions.drawing_utils
        self.results = 0

    def detect_hands(self, img, draw_hand = True):
        
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
        self.results = self.hands.process(img_RGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw_hand:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)

        return img


    def find_hand_position(self, img, hand_no = 0, draw_hand = True):

        list_position = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 8:
                    list_position.append([id, cx, cy])
                    if draw_hand:
                        cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)

        return list_position







