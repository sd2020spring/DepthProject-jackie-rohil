"""
This is the controller file for our Ball Drop Game. It provides the
functions that read user input (in our case, from the webcam feed) to control
the gameplay mechanics.
"""


import pygame


class ImageController:
    """ Checks for user input from placing the blocks on the wall projection and
    creates a new block based on the properties of this block.

    Attributes:
        is_placed: boolean indicating whether a block has been placed
        x_pos: the x-coordinate of the top left corner of the block
        y_pos: the y-coordinate of the top left corner of the block
        angle: the angle between the x-axis and the long side of the block which
                contains the top left corner (the block is not necessarily
                horizontal)
        width: the width of the block
        height: the height of the block
        color: the color of the block
        hitbox: the rectangle that defines the block's hitbox
    """
    def __init__(self):
        '''
        Initializes OpenCV set up
        '''
        #capture video from webcam
        cap = cv2.VideoCapture(0)
        #get dimensions of video capture so we can make a pygame window of the
        #same size
        width  = int(cap.get(3))
        height = int(cap.get(4))
        #sets font
        font = cv2.FONT_HERSHEY_COMPLEX
    def get_feed(self):
        '''
        returns the video feed after converting it to HSV
        '''
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
