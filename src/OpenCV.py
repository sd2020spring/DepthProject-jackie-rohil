import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshframe = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    contours,h = cv2.findContours(threshframe,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Display the resulting frame
    cv2.imshow('threshframe', threshframe)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        print(len(approx))
        if len(approx)==5:
            print("pentagon")
            cv2.drawContours(threshframe,[cnt],0,255,-1)
        elif len(approx)==3:
            print("triangle")
            cv2.drawContours(threshframe,[cnt],0,(0,255,0),-1)
        elif len(approx)==4:
            print("rectangle")
            cv2.drawContours(threshframe,[cnt],0,(0,0,255),-1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#use adaptive thresholding for better performance
#in varying lighting conditions
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
