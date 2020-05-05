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
    def __init__(self, is_placed, x_pos, y_pos, angle, width, height, color):
        """ Assigns provided parameters to a new ImageController object. The
        attributes of this object will be checked within GameEnvironment to
        control the movement of the player.
        """
        pass


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
