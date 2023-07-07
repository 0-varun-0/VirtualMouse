import cv2
import time
import numpy
import mediapipe
import HandRecognitionModule as Hrm

#############
wCam ,hCam = 640 ,480
#############

detector = Hrm.handDetector(maxHands=1)
pTime =0
cap = cv2.VideoCapture(0)
cap.set(3 , wCam)
cap.set(4 , hCam)

while True:
    #1 .To Find Handlandmarks
    success , img =cap.read()
    img = detector.findHands(img)
    lmList , bbox = detector.findPosition(img)
    #2. Get the tip of the index and middle fingers

    #3. Check which fingers are up

    #4.Only index = moving mode

    #5. convert coordinates

    #6. Smoothen the values

    #7. Move mouse

    #8. Check if we are in clicking mode i.e both index and moddle fingers are up

    #9. find disyance between these fingers and click if disatnce is short

    #10. Frame rate and display
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img , str(int(fps)) , (10,50) , cv2.FONT_HERSHEY_PLAIN , 3 ,(255 ,0,0) ,3 )

    cv2.imshow("Image",img)
    cv2.waitKey(1)

