# import all necessary packages
import cv2
import mediapipe as mp 


class HandDetection():
    """
    This class is designed to detect hands in an image and provide their respective locations.
    """
    def __init__(self, image_mode = False, max_num_hands = 2, model_complexity = 1,
     min_detection_confi = 0.5, min_tracking_confi = 0.5):
        """
        Class variables
        image_mode : hand detection and landmark localization. if flase only detect at first instance and then locate else detect at every instance
        max_num_hands : Maximum number of hands to detect
        model_complexity : Complexity of the hand landmark model(0 or1), Landmark accuracy as well as inference latency generally go up with the model complexity
        min_detection_confi : Minimum confidence value ([0.0, 1.0]) from the hand detection model 
        min_tracking_confi: Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model
    
        """
        self.image_mode = image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confi = min_detection_confi
        self.min_tracking_confi = min_tracking_confi

        # initialise hands object 
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.image_mode,
                                        self.max_num_hands,
                                        self.model_complexity,
                                        self.min_detection_confi,
                                        self.min_tracking_confi)
        # draw method initialisation to draw connections
        self.mp_draw = mp.solutions.drawing_utils
        self.results = 0

    def detect_hands(self, img, draw_hand = True):
        """
        Input : img, draw_hand
        Output : img

        this method will take img as input and draw hand (True or False) as input and return a image with detected hand in image 
        
        """
        # convert image to RGB as mediapipe works on RGB
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # process image to detect hand
        self.results = self.hands.process(img_RGB)

        # detect the hands in image
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                # if draw_hand == True the draw the hand in image
                if draw_hand:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)

        return img


    def find_hand_position(self, img, hand_no = 0, draw_hand = True):
        """
        Input : img, hand_no, draw_hand
        Output : list of locations of hand

        this method will take image with detected hand as input and return the list of loaction
        hand_no : no of hands to detect in image
        draw_hand : if true draw the hand
        """
        # initialise the list for hand location
        list_position = []
        # from results of detected hands
        if self.results.multi_hand_landmarks:
            # my_hand is the selected hand out of detection
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                # get image shape
                h, w, c = img.shape
                # landmarks are the ratios 
                # convert landmark into pixel
                cx, cy = int(lm.x*w), int(lm.y*h)

                # id =8 is tip of the index finger
                if id == 8:
                    # append the location of index finger tip
                    list_position.append([id, cx, cy])
                    # If draw_hand = True then draw the index finger tip
                    if draw_hand:
                        cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)

        return list_position







