"""
Ball Drop Game
@authors:
Jackie Zeng
Rohil Agarwal

This is the main file for our Ball Drop Game.
There are two other files that this file depends on (view and controller).

This is a game that combines CV and AR into the gameplay.
The human player can add obstacles to the game environment by placing
them in front of a separate game display screen, OpenCV will detect the
obstacles, and these obstacles would be generated through pygame as a component
that other features in the game could interact with.
This idea is based off of Puppet.io, a project we were impressed by at
MakeHarvard 2020.

See https://sd2020spring.github.io/DepthProject-jackie-rohil/ for more extensive
information about this project.
"""


import pygame
import time
from pygame.locals import *
import sys
import numpy as np
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
import numpy as np
from FinalProject_Controller import *
from FinalProject_View import *
from FinalProject_Helper import *


class GameEnvironment:
    """ Represents the full game.
    Initializes new objects for the penguin and obstacles and draws them.
    Draws the environment within which the game is played (ex: background color)

    Attributes:
        bkgd_color: color code for the background (some sort of blue)
        game_status: a string representing the state of the game, 3 options
            - start: will display start menu
            - play: will run and display the game
            - end: will display end menu
    """
    def __init__(self, bkgd_color=(0,200,255), game_status="start"):
        """ Starts the game at the start menu.
        """
        pass

    def gameplay(self):
        """ CONTROLS THE FLOW OF THE GAME.

        CREATE MULTIPLE SUBFUNCTIONS (LIKE COLLISION CHECK) THAT THIS FUNCTION
        CALLS

        When game_status="start"
            - create StartMenu object
            - create MouseController object
            - call functions to draw start menu and play start music
            - when start button is clicked, change game_status to "play"
        When game_status="play"
            - create KeyboardController object
            - create ImageController object and create blocks within the game
                based on the human-placed blocks
            - create Player object and call drawPlayer
            - if space bar is pressed, release ball
            - play music that corresponds to specific actions
            - check for collisions between player and blocks based on hitboxes
                - if collision with blocks occurs, play collision music and
                    change movement based on the new constraint
                - if collision with target occurs, play win music and change
                    game_status to "end"
        When game_status="end"
            - create EndMenu object
            - call functions to draw end menu and play end music
            - when retry button is clicked, change game_status to "play"
            - when home button is clicked, change game_status to "start"
        """
        pass


class Ball:
    """ Represents the player as a ball.
    The penguin remains stationary while the environment and obstacles
    move toward it, hence no change position function.

    Attributes:
        x_pos: the x-coordinate of the center of the ball
        y_pos: the y-coordinate of the center of the ball
        radius: the radius of the ball
        hitbox: the rectangle that defines the ball hitbox
    """
    def __init__(self, x_pos=100, y_pos=100, radius=50):
        """ Creates a Ball object. The values in the parameters
        should not be overwritten, since the ball will always start in the same
        position and have the same size every time the game is played.
        """
        #expected methods assigning parameters to attributes
        #self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pass

    def move(self):
        """ Makes the ball move by changing the coordinates of its center point.
        """
        pass

    def drawPlayer(self):
        """ Draws the ball based on its attributes.
        """
        pass


class Feature:
    """ The superclass that represents a generic feature. Block and target
    are the child classes of this class.

    Attributes:
        x_pos: the x-coordinate of the top left corner of the feature
        y_pos: the y-coordinate of the top left corner of the feature
        angle: the angle between the x-axis and the long side of the feature which
                contains the top left corner (the feature is not necessarily
                horizontal)
        width: the width of the feature
        height: the height of the feature
        color: the color of the feature
        hitbox: the rectangle that defines the feature's hitbox
    """
    def __init__(self, x_pos, y_pos, angle, width, height, color):
        """ Creates a Feature object.
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.width = width
        self.height = height
        self.color = (0,255,0)
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def draw(self, screen):
        """ Draws the Feature.
        """
        pygame.draw.rect(screen, self.color, self.hitbox)

class Block(Feature):
    """ Represents the blocks that direct the ball

    Unique Attributes:
        color=(0,255,0)
            - all blocks have the same color (green)

    Inherited from Obstacle:
        x_pos: the x-coordinate of the top left corner of the block
        y_pos: the y-coordinate of the top left corner of the block
        angle: the angle between the x-axis and the long side of the block which
                contains the top left corner (the block is not necessarily
                horizontal)
        width: the width of the block
        height: the height of the block
        hitbox: the rectangle that defines the feature's block
    """
    def __init__(self, x_pos, y_pos, angle, width, height):
        """Creates a new Block object with the given attributes.
        """
        super().__init__(x_pos, y_pos, angle, width, height, color=(0,255,0))


    def draw(self,screen):
        """ Draws the Block based on its attributes.
        """
        super().draw(screen)


class Target(Feature):
    """ Represents the blocks that direct the ball

    Unique Attributes:
        color = (0,0,255)
            - the target is always blue
        angle = 0
            - the target is always horizontal

    Inherited from Obstacle:
        x_pos: the x-coordinate of the top left corner of the block
        y_pos: the y-coordinate of the top left corner of the block
        width: the width of the block
        height: the height of the block
        hitbox: the rectangle that defines the feature's block
    """
    def __init__(self, x_pos, y_pos, width, height):
        """Creates a new Target object with the given attributes.
        """
        super().__init__(x_pos, y_pos, 0, width, height, (0,255,0))

    def draw(self):
        """ Draws the Target based on its attributes.
        """
        super().draw()


if __name__ == "__main__":
    pygame.init()
    # set screen to size of OpenCV video
    screen = pygame.display.set_mode([640, 480])
    camera = ImageController()
    running = True

    # Fill the background with white
    screen.fill((255, 255, 255))
    pygame.display.flip()
    #capture video from webcam
    cap = cv2.VideoCapture(0)
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        isRectangle, x, y = camera.detect_rectangle(cap)
        print (x,y)
        if (isRectangle):
            platform = Block(x,y,0,20,20)
            platform.draw(screen)
            # pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)

        #Flip the display
        pygame.display.flip()
        screen.fill((255, 255, 255))

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    GameEnvironment()
    #check if x button is pushed to close window
    pygame.quit()
