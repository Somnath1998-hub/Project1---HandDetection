import time
import cv2
import mediapipe as mp 

import HandDetectionModule as HDM

def main():
    pTime =0
    cTime = 0

    cap = cv2.VideoCapture(0)

    detector = HDM.HandDetection()


    while True:
        rate, img = cap.read()
        # print(img.shape)
        img = detector.detect_hands(img)

        list_position = detector.find_hand_position(img)

        print(list_position)
        if len(list_position) != 0:
            h_detected =  list_position[0][1]
            w_detected =  list_position[0][2]
            if (h_detected >10 and h_detected < 120) and (w_detected >10 and w_detected < 120):
                cv2.putText(img,str("Alert..!!"),(500,40), cv2.FONT_HERSHEY_PLAIN,2, (0,0,255),2)
            elif (h_detected >520 and h_detected < 640) and (w_detected >350 and w_detected < 460):
                cv2.putText(img,str("Alert..!!"),(500,40), cv2.FONT_HERSHEY_PLAIN,2, (0,0,255),2)



        cTime = time.time()
        fps = 1 /(cTime-pTime)
        pTime = cTime
        
        # cv2.putText(img,str(int(fps)),(560,40), cv2.FONT_HERSHEY_PLAIN,2, (255,0,255),2)
        cv2.rectangle(img, (10,10), (120,120), (0,0,255), 3)
        cv2.rectangle(img, (520,350), (640,460), (0,0,255), 3)

        
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

