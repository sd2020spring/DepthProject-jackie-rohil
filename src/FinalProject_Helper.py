"""
This is the helper file for our Ball Drop Game. It contains any fundamental
helper functions that are useful throughout the rest of the project.
"""


import pygame


class Rectangle:
    """ Creates a Rectangle object based on the attributes listed below.
    This rectangle object is used throughout this project, as the basis for
    the blocks, the target, the player, and buttons in the menus.

    Attributes:
        x_pos: the x-coordinate of the top left corner of the rectangle
        y_pos: the y-coordinate of the top left corner of the rectangle
        angle: the angle between the x-axis and the long side of
                the rectangle which contains the top left corner (the rectangle
                is not necessarily horizontal)
        width: the width of the rectangle
        height: the height of the rectangle
        color: the color of the rectangle
    """
