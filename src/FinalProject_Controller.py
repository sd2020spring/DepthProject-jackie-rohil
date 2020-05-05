"""
This is the controller file for our Ball Drop Game. It provides the
functions that read user input (in our case, from the webcam feed) to control
the gameplay mechanics.
"""


import pygame
from pygame.locals import *
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
import numpy as np


class ImageController:
    """ Checks for user input from placing the blocks on the wall projection and
    creates a new block based on the properties of this block.
    """
    def __init__(self):
        '''
        Initializes OpenCV set up
        '''
        #sets font
        font = cv2.FONT_HERSHEY_COMPLEX
    def get_feed(self):
        '''
        returns the video feed after converting it to HSV
        '''
        #capture video from webcam
        cap = cv2.VideoCapture(0)
        #get dimensions of video capture so we can make a pygame window of the
        #same size
        width  = int(cap.get(3))
        height = int(cap.get(4))

    def create_trackbars(self):
        '''
        Creates trackbars to calibrate the background. Sets lower and upper HSV
        ranges so we can create a mask later of a certain color. OpenCV HSV ranges: Hue(0-180), Saturation(0-255), Value(0-255). Values are currently set to green because I used a green post it note for testing
        '''
        cv2.namedWindow("Trackbars")
        #initialize values for trackbars
        cv2.createTrackbar("L-H", "Trackbars", 27, 180, nothing)
        cv2.createTrackbar("L-S", "Trackbars", 10, 255, nothing)
        cv2.createTrackbar("L-V", "Trackbars", 134, 255, nothing)
        cv2.createTrackbar("U-H", "Trackbars", 91, 180, nothing)
        cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
        cv2.createTrackbar("U-V", "Trackbars", 167, 255, nothing)

    def create_mask():
        '''
        creates mask with HSV values
        '''
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

    def run_camera():
        '''
        main program to run OpenCV code
        '''
        get_feed()
        create_trackbars()
        while True:
            _, frame = cap.read()
            #convert into HSV color space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            create_mask()
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
                        # Rect(left, top, width, height)
                        platform = pygame.Rect(0, 0, 40, 10)
                        platform.centerx = x
                        platform.centery = y
                        pygame.draw.rect(screen, (0,0,255), platform)

            cv2.imshow("Frame", frame)
            cv2.imshow("Mask", mask)

            #Update the full display surface to the screen
            pygame.display.flip()
            screen.fill((255, 255, 255))

            #press escape key to end
            key = cv2.waitKey(1)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
class KeyboardController:
    """ Checks for user input from clicking keys on the keyboard in order to
    move the ball.

    Attributes:
        is_pressed: boolean indicating whether a key is pressed
        key: the event key, shows which key is pressed (up arrow, down
        arrow, side arrows)
    """
    def __init__(self, is_pressed, key):
        """ Assigns provided parameters to a new KeyboardController object. The
        attributes of this object will be checked within FinalProject_Model to
        control the movement of the ball.
        """
        pass


class MouseController:
    """ Checks for user input from clicking the mouse in order to click on
    buttons.

    Attributes:
        is_pressed: boolean indicating whether the left mouuse button is pressed
        x_pos: the x-coordinate of the location on the screen where the mouse
                was clicked
        y_pos: the y-coordinate of the location on the screen where the mouse
                was clicked
    """
    def __init__(self, is_pressed, x_pos, y_pos):
        """ Assigns provided parameters to a new MouseController object. The
        attributes of this object will be checked within FinalProject_Model to
        allow the users to navigate the menu pages.
        """
        pass
