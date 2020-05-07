"""
This is the controller file for our Ball Drop Game. It provides the
functions that read user input (in our case, from the webcam feed) to control
the gameplay mechanics.
"""


import pygame
from threading import Thread
import time
import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
#sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
import numpy as np


class ImageController:
    """ Checks for user input from placing the blocks on the wall projection and
    creates a new block based on the properties of this block.
    """

    def __init__(self):
        """ Initializes OpenCV set up
        """
        # Start capturing video from webcam
        self.cap = cv2.VideoCapture(0)
        # Sets amount of frames stored in the internal buffer memory. Since the
        # buffer is only storing 2 frames, we are always getting live feed.
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # FPS = 1/X
        # X = desired FPS. Our webcam has a FPS of 30
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        # Stops this thread if the other program stops running
        self.thread.daemon = True
        self.thread.start()

        # Sets font
        self.font = cv2.FONT_HERSHEY_COMPLEX

    def update(self):
        """ This function is threaded. It updates self.frame automatically every
        FPS
        """
        while True:
            if self.cap.isOpened():
                (self.status, self.frame) = self.cap.read()
            time.sleep(self.FPS)

    def show_frames(self):
        """ Displays mask and webcam feed and waits the desired FPS to sync up video
        """
        cv2.imshow('Frame', self.frame)
        cv2.imshow("Mask", self.mask)
        cv2.waitKey(self.FPS_MS)

    def create_trackbars(self):
        """ Creates trackbars to calibrate the background. Sets lower and upper HSV
        ranges so we can create a mask later of a certain color.
        OpenCV HSV ranges: Hue(0-180), Saturation(0-255), Value(0-255).
        Values are currently set to green. This needs to be calibrated before the
        program can function properly.
        """
        cv2.namedWindow("Trackbars")
        # Initialize values for trackbars
        cv2.createTrackbar("L-H", "Trackbars", 12, 180, lambda x:x)
        cv2.createTrackbar("L-S", "Trackbars", 61, 255, lambda x:x)
        cv2.createTrackbar("L-V", "Trackbars", 125, 255, lambda x:x)
        cv2.createTrackbar("U-H", "Trackbars", 81, 180, lambda x:x)
        cv2.createTrackbar("U-S", "Trackbars", 251, 255, lambda x:x)
        cv2.createTrackbar("U-V", "Trackbars", 240, 255, lambda x:x)

    def create_hsv_mask(self):
        """ Creates mask with HSV values from the trackbar. Adjusts in real time.
        """
        # Convert frame into HSV color space
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        # Retrieves real time trackbar values.
        l_h = cv2.getTrackbarPos("L-H", "Trackbars")
        l_s = cv2.getTrackbarPos("L-S", "Trackbars")
        l_v = cv2.getTrackbarPos("L-V", "Trackbars")
        u_h = cv2.getTrackbarPos("U-H", "Trackbars")
        u_s = cv2.getTrackbarPos("U-S", "Trackbars")
        u_v = cv2.getTrackbarPos("U-V", "Trackbars")

        lower_color = np.array([l_h, l_s, l_v])
        upper_color = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, lower_color, upper_color)
        # Small square to erode image by.
        kernel = np.ones((5, 5), np.uint8)
        # Erode makes the object we are masking smaller. Cleans up data by taking
        # away random small dots
        self.mask = cv2.erode(mask, kernel)

    def detect_rectangle(self):
        """ Uses contours generated from the mask to detect whether a
        rectangle exists in the frame.

        Returns:
            isRectangle: boolean representing whether there is a rectangle in frame
            x: x position of the top right corner of the rectangle detected
            y: y position of the top right corner of the rectangle detected
        """
        # There is no rectangle at the beginning
        isRectangle = False

        # Checking OpenCV version because the findContours function is different.
        if int(cv2.__version__[0]) > 3:
            # Opencv 4.x.x
            # Looking for contours in mask. Outputs points in the image.
            contours, _ = cv2.findContours(self.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        else:
            # Opencv 3.x.x
            _, contours, _ = cv2.findContours(self.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            # Aproximate sides. True refers to closed polygon
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            # Get xy positions to place the text
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            # Only detect objects that are bigger to remove noise
            if area > 400:
                # Draws points found in contours
                cv2.drawContours(self.frame, [approx], 0, (0, 0, 0), 5)

                # If it detects 4 outlines, then a rectangle exists
                if len(approx) == 4:
                    # Displays text on frame confirming there is a rectangle
                    cv2.putText(self.frame, "Rectangle", (x, y), self.font, 1, (0, 0, 0))
                    isRectangle = True

        if(isRectangle == True):
            return (isRectangle, x, y)
        else:
            return (False, 0, 0)

    def end_capture(self):
        """
        Ends current video capture
        """
        self.cap.release()
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
        is_pressed: boolean indicating whether the left mouse button is pressed
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

if __name__ == "__main__":

    #testing code before moving into main model file
    camera = ImageController()
    camera.create_trackbars()

    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    running = True

    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        try:
            camera.create_hsv_mask()
            camera.detect_rectangle()
            camera.show_frames()
        except AttributeError:
            pass

        # display pygame graphics
        pygame.display.flip()
        screen.fill((255, 255, 255))

        #press escape key to end
        key = cv2.waitKey(1)
        if key == 27:
            camera.end_capture()
