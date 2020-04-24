"""
Ball Drop Game
@authors:
Jackie Zeng
Rohil Agarwal
Game objective: TODO
"""


import pygame
import sys
import numpy as np
import cv2


class GameEnvironment:
    """ Represents the full game.
    Initializes new objects for the penguin and obstacles and draws them.
    Draws the environment within which the game is played (ex: background color)

    Attributes:
        y_pos: y coordinate for the ice/ground as a continuous line
        bkgd_color: color code for the background (some sort of blue)
        level: an int representing the current difficulty level of the game
        game_status: a string representing the state of the game, 3 options
            - start: will display start menu
            - play: will run and display the game
            - end: will display end menu
    """
    def __init__(self, y_pos=200, bkgd_color=(0,200,255), level=1, game_status="start"):
        """ Starts the game at the start menu and level 1.
        """
        pass

    def gameplay(self):
        """ CONTROLS THE FLOW OF THE GAME.

        When game_status="start"
            - create StartMenu object
            - create MouseController object
            - call functions to draw start menu and play start music
            - when start button is clicked, change game_status to "play"
        When game_status="play"
            - draw the ground as a wide rectangle with a small height
            - create KeyboardController object
            - create Penguin object and call draw_normal_penguin
            - if up arrow is pressed, call Penguin's jump() function
            - if down arrow is pressed, call Penguin's duck() and draw_ducking_penguin() functions
            - if down arrow is unpressed, call Penguin's unduck() and draw_normal_penguin() functions
            - create new obstacles, draw them, and move them toward the player
                - speed and number should be based on the difficulty level
            - play music that corresponds to specific actions
            - increase the level by 1 after a set time interval (ex: 15 seconds)
            - track the player's score, which is a multiple of the time they have survived for
            - check for collisions between player and obstacle based on hitboxes
                - if collision occurs, change game_status to "end"
        When game_status="end"
            - create EndMenu object
            - call functions to draw end menu and play end music
            - when retry button is clicked, change game_status to "play"
            - when home button is clicked, change game_status to "start"
        """
        pass


class Penguin:
    """ Represents the player as a penguin.
    The penguin remains stationary while the environment and obstacles
    move toward it, hence no change position function.

    Attributes:
        x_pos: the x-coordinate of the top left corner of the character's hitbox
        y_pos: the y-coordinate of the top left corner of the character's hitbox
        width: the width of the character's hitbox
        height: the height of the character's hitbox
        hitbox: the rectangle that defines the character's hitbox

    Note: preset parameter numbers are arbitrary, they are just to show
    that for these attributes, parameters provided are unwated/unnecessary
    """
    def __init__(self, x_pos=100, y_pos=100, width=100, height=300):
        """ Creates a penguin object. The values in the parameters
        should not be overwritten, since the penguin will remain in the same
        position and have the same width and height in any instance that
        the game is played.
        """
        #expected methods assigning parameters to attributes
        #self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pass

    def jump(self):
        """ Makes the penguin jump by increasing its y_position by a little bit
        each millisecond and then decreasing it back to its original value after
        reaching a preset apogee (maximum y_value).
        """
        pass

    def duck(self):
        """ Makes the penguin duck by instantly decreasing its height.
        A separate draw method will be used to draw the ducking penguin.
        """
        pass

    def unduck(self):
        """ Makes the penguin go back to its normal height after the down arrow
        is unpressed by the user.
        """
        pass

    def draw_normal_penguin(self):
        """ Draws the penguin in its normal, upright position.
        This is how the penguin will look when running or jumping.
        """
        pass

    def draw_ducking_penguin(self):
        """ Draws the penguin in its ducking position.
        """
        pass


class Obstacle:
    """ The superclass that represents a generic obstacle. Snowball and IceCrack
    are the child classes of this class.

    Attributes:
        x_pos: x-coordinate of center of obstacle (for snowball) or top left
        corner (for IceCrack)
        y_pos: y-coordinate of center of obstacle (for snowball) or top left
        corner (for IceCrack)
        width: width of the rectangle bounding the obstacle
        height: height of the rectangle bounding the obstacle
        hitbox: the rectangle that bounds the obstacle and defines the \
        character's hitbox
    """
    def __init__(self, x_pos, y_pos, width, height):
        """ Creates an Obstacle object.
        """
        #expected methods assigning parameters to attributes
        #self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pass

    def changePosition(self):
        """ Moves the Obstacle closer to the Penguin. The manner in which this
        is done depends on the Obstacle type (Snowball vs. IceCrack).
        """
        pass

    def draw(self):
        """ Draws the Obstacle.
        """
        pass


class IceCrack(Obstacle):
    """ Represents the ground obstacle, which are cracks in the ice.

    Unique Attributes:
        length: length of the crack in the ice, in pixels
        height: the height of the crack in the ice, should always be
        the same (the height of the ground never changes, so it doesn't make
        sense for the height of the crack to change)

    Inherited from Obstacle:
        x_pos: x-coordinate of the top left corner of the crack
        y_pos: y-coordinate of the top left corner of the crack

    Note: The crack will be drawn in the same color as the background so that
    it looks like there is no ice or other object there.
    """
    def __init__(self, length, x_pos, y_pos, height=10):
        """Since the GroundObstacle is a crack in the ice and we are going to stop
        drawing something, the GameEnvironment class calls this function, which
        passes the length (in pixels or time) that GameEnvironment needs to pause
        drawing the ground for.
        """
        pass

    def changePosition(self):
        """ Moves the IceCrack toward the penguin at a constant speed.
        """
        pass

    def draw(self):
        """ Draws the IceCrack as a Rectangle based on x_pos, y_pos, length,
        height, and a hard-coded color. The IceCrack will be drawn so that it
        colors over the ground.
        """
        pass


class Snowball(Obstacle):
    """ Represents the air obstacle, which is a moving snowball.

    Unique Attributes:
        diameter: diameter of the snowball in pixels

    Inherited from Obstacle:
        x_pos: x-coordinate of the center of the snowball
        y_pos: y-coordinate of the center of the snowball
    """
    def __init__(self, diameter, x_pos, y_pos):
        """ Creates a Snowball object, which is an obstacle. This snowball is
        defined by the circle centered at x_pos and y_pos, with a diameter
        specified with the diameter attribute.
        """
        pass

    def changePosition(self):
        """ Moves the snowball in a parabola by decreasing its x_pos (so that it
        moves closer to the penguin) by a little bit each millisecond while
        increasing y_pos by a little bit each millisecond until the snowball
        reaches a preset apogee (maximum y-value), after which the y_pos is
        reduced by a little bit each millisecond.
        """
        pass

    def draw(self):
        """ Draws the snowball based on x_pos, y_pos, diameter, and a hard-coded
        color.
        """
        pass


if __name__ == "__main__":
    pygame.init()
    GameEnvironment()
    #check if x button is pushed to close window
    pygame.quit()
