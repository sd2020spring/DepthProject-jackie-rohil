"""
This is the controller file for our Ball Drop Game. It provides the
functions that read user input (in our case, from the webcam feed) to control
the gameplay mechanics.
"""


import pygame
from threading import Thread
import time
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
        #start capturing video from webcam
        self.cap = cv2.VideoCapture(0)
        #sets amount of frames stored in the internal buffer memory. Since the
        #buffer is only storing 2 frames, we are always getting live feed.
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # FPS = 1/X
        # X = desired FPS. Our webcam has a FPS of 30
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        #stops this thread if the other program stops running
        self.thread.daemon = True
        self.thread.start()

        #sets font
        self.font = cv2.FONT_HERSHEY_COMPLEX

    def update(self):
        '''
        auto updates frame every FPS
        '''
        while True:
            if self.cap.isOpened():
                (self.status, self.frame) = self.cap.read()
            time.sleep(self.FPS)

    def show_frame(self):
        cv2.imshow('Frame', self.frame)
        cv2.waitKey(self.FPS_MS)

    def show_mask(self):
        cv2.imshow("Mask", self.mask)
        cv2.waitKey(self.FPS_MS)

    def create_trackbars(self):
        '''
        Creates trackbars to calibrate the background. Sets lower and upper HSV
        ranges so we can create a mask later of a certain color. OpenCV HSV ranges: Hue(0-180), Saturation(0-255), Value(0-255). Values are currently set to green because I used a green post it note for testing
        '''
        cv2.namedWindow("Trackbars")
        # #initialize values for trackbars
        cv2.createTrackbar("L-H", "Trackbars", 0, 180, lambda x:x)
        cv2.createTrackbar("L-S", "Trackbars", 61, 255, lambda x:x)
        cv2.createTrackbar("L-V", "Trackbars", 125, 255, lambda x:x)
        cv2.createTrackbar("U-H", "Trackbars", 81, 180, lambda x:x)
        cv2.createTrackbar("U-S", "Trackbars", 251, 255, lambda x:x)
        cv2.createTrackbar("U-V", "Trackbars", 240, 255, lambda x:x)

    def create_hsv_mask(self):
        '''
        creates mask with HSV values
        '''

        #convert frame into HSV color space
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

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
        self.mask = cv2.erode(mask, kernel)

    def detect_rectangle(self):
        isRectangle = False

        if int(cv2.__version__[0]) > 3:
            # Opencv 4.x.x
            # looking for contours in mask. Outputs points in the image.
            contours, _ = cv2.findContours(self.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        else:
            # Opencv 3.x.x
            _, contours, _ = cv2.findContours(self.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            #Aproximate sides. True refers to closed polygon
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            #get xy positions to place the text
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            # only detect objects that are bigger to remove noise
            if area > 400:
                # draws points found in contours
                cv2.drawContours(self.frame, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 4:
                    cv2.putText(self.frame, "Rectangle", (x, y), self.font, 1, (0, 0, 0))
                    isRectangle = True
                    pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)

        if(isRectangle == True):
            return (isRectangle, x, y)

    def end_capture(self):

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

if __name__ == "__main__":

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

        camera.create_hsv_mask()
        camera.detect_rectangle()
        camera.show_frame()
        camera.show_mask()

        # display pygame graphics
        pygame.display.flip()
        screen.fill((255, 255, 255))

        #press escape key to end
        key = cv2.waitKey(1)
        if key == 27:
            camera.end_capture()
