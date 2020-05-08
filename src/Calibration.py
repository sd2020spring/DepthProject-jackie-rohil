import pygame
import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
# sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
import numpy as np

# OpenCV Setup

#capture video from webcam
cap = cv2.VideoCapture(0)
#get dimensions of video capture so we can make a pygame window of the same
#size. Convert to int bc pygame display expects integers
width  = int(cap.get(3))
height = int(cap.get(4))
print(width, height)

# OpenCV HSV ranges: Hue(0-180), Saturation(0-255), Value(0-255)
cv2.namedWindow("Trackbars")
#initialize values for trackbars
cv2.createTrackbar("L-H", "Trackbars", 0, 180, lambda x:x)
cv2.createTrackbar("L-S", "Trackbars", 25, 255, lambda x:x)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, lambda x:x)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, lambda x:x)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, lambda x:x)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, lambda x:x)

font = cv2.FONT_HERSHEY_COMPLEX

#initialize pygame
pygame.init()
screen = pygame.display.set_mode([width, height])
running = True
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while True:
        _, frame = cap.read()
        #convert into HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("L-H", "Trackbars")
        l_s = cv2.getTrackbarPos("L-S", "Trackbars")
        l_v = cv2.getTrackbarPos("L-V", "Trackbars")
        u_h = cv2.getTrackbarPos("U-H", "Trackbars")
        u_s = cv2.getTrackbarPos("U-S", "Trackbars")
        u_v = cv2.getTrackbarPos("U-V", "Trackbars")

        lower_color = np.array([l_h, l_s, l_v])
        upper_color = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, lower_color, upper_color)
        #small square
        kernel = np.ones((5, 5), np.uint8)
        #erode makes the object we are masking smaller. Cleans up data by taking
        #away random small dots
        mask = cv2.erode(mask, kernel)

        # Contours detection
        if int(cv2.__version__[0]) > 3:
            # Opencv 4.x.x
            # looking for contours in mask. Outputs points in the image.
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        else:
            # Opencv 3.x.x
            _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            #Aproximate sides. True refers to closed polygon
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            #get xy positions to place the
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            # only detect objects that are bigger to remove noise
            if area > 400:
                # draws points found in contours
                # (fram, ___, ___, color of contour, thickness of contour line)
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 4:
                    cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                    #draw a circle on the pygame screen
                    pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)

        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        #Flip the display
        pygame.display.flip()
        screen.fill((255, 255, 255))

        key = cv2.waitKey(1)
        #press escape key to end
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
