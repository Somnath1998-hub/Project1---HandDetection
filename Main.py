# import all necessary packages
import cv2
import mediapipe as mp 

# import HandDetectionModule - it contains class to detect hand position
import HandDetectionModule as HDM

def main():
    # define a video capture object
    cap = cv2.VideoCapture(0)
    # initialise the HandDetection class from the HandDetectionModule
    detector = HDM.HandDetection()

    while True:
        # capture the video frame 
        rate, img = cap.read()        # img.shape = (480,640,3)

        # detect_hands method will detect the hand in image 
        img = detector.detect_hands(img)

        # find_hand_position method will detect the location of hand in image
        list_position = detector.find_hand_position(img)
        
        # if find_hand_position locates the hand in image
        if len(list_position) != 0:
            # height location of hand in image
            h_detected =  list_position[0][1]
            # width location of hand in image
            w_detected =  list_position[0][2]

            # if detected hand location is in red zone (in rectangle1) then trigger the alert
            if (h_detected >10 and h_detected < 120) and (w_detected >10 and w_detected < 120):
                # put Alert on image
                cv2.putText(img,str("Alert..!!"),(500,40), cv2.FONT_HERSHEY_PLAIN,2, (0,0,255),2)
                
             # if detected hand location is in red zone (in rectangle2) then trigger the alert
            elif (h_detected >520 and h_detected < 640) and (w_detected >350 and w_detected < 460):
                # put Alert on image
                cv2.putText(img,str("Alert..!!"),(500,40), cv2.FONT_HERSHEY_PLAIN,2, (0,0,255),2)

        # crate a rectangle1 in image as red zone
        cv2.rectangle(img, (10,10), (120,120), (0,0,255), 3)
        # crate a rectangle2 in image as red zone
        cv2.rectangle(img, (520,350), (640,460), (0,0,255), 3)  

        #display the resulting frame
        cv2.imshow("Image", img)

        # the 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # after the loop release the cap object
    cap.release()
    # distroy all the windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

