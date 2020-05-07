"""
DISCLAIMER: This game captures video using your computer webcam. This video feed
is near-live capture, and it is not saved locally or to the web. By playing this
game, you consent to having video taken, which can involve yourself or other
people.

MVP: CV Ball Avoidance Game
Original Idea: AR/CV Ball Drop Game


@authors:
Jackie Zeng
Rohil Agarwal


MVP:
PLEASE NOTE: We already drafted our class structure for our original idea, and
we hope to complete our original idea in the future. We have intentionally
included non-functional classes and functions to allow for future implementation
and show our thinking.

We were unable to complete our original idea in the time frame allotted,
so we pivoted to our MVP idea, which is a simple game that uses CV to detect a
real-life rectangle, creates a virtual rectangle based on these properties, and
has a vitual circle chase it. You lose if the circle is able to catch up to and
collide with the rectangle, so you have to move your real-life rectangle
quickly and with dexterity in order to not lose.


Original Idea:
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
from threading import Thread
from pygame.locals import *
import sys
import numpy as np
""" If you have ROS on your operating system, uncomment the following two
sys.path lines
"""
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # In order to import cv2 under python3
import cv2
#sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # Append back in order to import rospy
import numpy as np
from FinalProject_Controller import *
from FinalProject_View import *

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
    def __init__(self, bkgd_color=(109,104,117), game_status="start"):
        """ Starts the game at the start menu.
        """
        self.bkgd_color = bkgd_color
        self.game_status = "start"

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
            - create Player object and call its draw function
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

    def createBall(self, screen):
        """ Creates default ball object in default position.
        """
        self.ball = Ball()
        self.ball.draw(screen)

    def moveBall(self):
        """ Moves ball toward the square and recreates hitbox after moving.
        """
        dx = 5
        dy = 5
        if self.block.x_center > self.ball.x_pos:
            self.ball.x_pos += dx
        elif self.block.x_center < self.ball.x_pos:
            self.ball.x_pos -= dx
        if self.block.y_center > self.ball.y_pos:
            self.ball.y_pos += dy
        elif self.block.y_center < self.ball.y_pos:
            self.ball.y_pos -= dy
        self.ball.hitbox = pygame.Rect(self.ball.x_pos-self.ball.radius, self.ball.y_pos-self.ball.radius, self.ball.radius*2, self.ball.radius*2)

    def drawBall(self, screen):
        self.ball.draw(screen)

    def createBlock(self, screen, x, y, angle, width, height):
        """ Creates Block with parameters passed from main method.
        """
        self.block = Block(x, y, angle, width, height)

    def drawBlock(self, screen):
        self.block.draw(screen)

    def collisiontext(self, screen):
        """ Displays 'YOU LOSE' when collision occurs.
        """
        textfont = pygame.font.SysFont('Arial', 50)
        textsurface = textfont.render('YOU LOSE!', False, (0, 0, 0))
        screen.blit(textsurface,(10,10))

    def erasecollisiontext(self, screen):
        """ Removes 'YOU LOSE' when ball and block are no longer collided.
        """
        textfont = pygame.font.SysFont('Arial', 15)
        textsurface = textfont.render('', False, (0, 0, 0))
        screen.blit(textsurface,(0,0))


class Ball:
    """ Represents the player as a ball.
    The penguin remains stationary while the environment and obstacles
    move toward it, hence no change position function.

    Unique Attributes:
        color=(255,0,0)
            - the ball is always red

    Attributes:
        x_pos: the x-coordinate of the center of the ball
        y_pos: the y-coordinate of the center of the ball
        radius: the radius of the ball
        hitbox: the rectangle that defines the ball hitbox
    """
    def __init__(self, x_pos=320, y_pos=240, radius=50):
        """ Creates a Ball object. The values in the parameters
        should not be overwritten, since the ball will always start in the same
        position and have the same size every time the game is played.
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = (255, 180, 162)
        self.hitbox = pygame.Rect(self.x_pos-self.radius,self.y_pos-self.radius,2*self.radius,2*self.radius)

    def draw(self, screen):
        """ Draws the ball based on its attributes.
        """
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)


class Feature:
    """ The superclass that represents a generic rectangular feature. Block and target
    are the child classes of this class.

    Attributes:
        x_pos: the x-coordinate of the top left corner of the feature
        y_pos: the y-coordinate of the top left corner of the feature
        angle: the angle between the x-axis and the long side of the feature which
                contains the top left corner (the feature is not necessarily
                horizontal)
        width: the width of the feature
        height: the height of the feature
        x_center: the x_coordinate of the center of the block
        y_center: the y_coordinate of the center of the block
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
        self.x_center = self.x_pos + self.width/2
        self.y_center = self.y_pos + self.height/2
        self.color = color
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
        x_center: the x_coordinate of the center of the block
        y_center: the y_coordinate of the center of the block
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
        super().__init__(x_pos, y_pos, angle, width, height, color=(181, 131, 141))

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
        x_pos: the x-coordinate of the top left corner of the target
        y_pos: the y-coordinate of the top left corner of the target
        width: the width of the target
        height: the height of the target
        hitbox: the rectangle that defines the feature's target
    """
    def __init__(self, x_pos, y_pos, width, height):
        """Creates a new Target object with the given attributes.
        """
        super().__init__(x_pos, y_pos, 0, width, height, (109,104,117))

    def draw(self):
        """ Draws the Target based on its attributes.
        """
        super().draw()


if __name__ == "__main__":

    # Creates ImageController object, which reads webcam data
    camera = ImageController()
    # Creates trackbars for calibration
    camera.create_trackbars()

    # Initialize game engine
    pygame.init()

    # Scale window up by a factor of 2
    scale = 2
    # Set screen to scale times the size of OpenCV video
    screen = pygame.display.set_mode([640*scale, 480*scale])

    # Creates new GameEnvironment object, which contains instances of game
    # features and methods that act on them
    game = GameEnvironment()

    # Flag for running while loop below
    running = True

    # Fill the background with the color specified the game object
    screen.fill(game.bkgd_color)
    # Display pygame window
    pygame.display.flip()

    # Create ball object at initial position
    game.createBall(screen)

    # Flag so that draw does not occur if try block fails on first attempt
    shapes_were_created = False

    while running:

        # Check if the user clicks the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(game.bkgd_color)

        # Contains hitboxes for ball and block
        hitboxList = []
        collisionflag = False
        block_width = 100
        # If AttributeError is thrown (because frame or mask was not captured
        # during this particular loop), pass through, continue with the while
        # loop, and repeat
        try:
            camera.create_hsv_mask()
            # Says if rectangle has been detected, gives x and y pos if it has
            isRectangle, x, y = camera.detect_rectangle()
            # What should be executed if OpenCV detects a rectangle
            if (isRectangle):
                # Create Block object, add hitbox to hitboxList, and draw
                game.createBlock(screen,(x-block_width)*scale,y*scale,0,block_width,block_width)
                hitboxList.append(game.block.hitbox)
                # Change ball position, add hitbox to hitboxList, and draw
                game.moveBall()
                hitboxList.append(game.ball.hitbox)
            # Check for collision between ball and block
            shapes_were_created = True
            # If hitboxList has been populated, check for collision, if collision
            # then display collision text and set flag to true
            if len(hitboxList) != 0:
                if hitboxList[0].colliderect(hitboxList[1]):
                    game.collisiontext(screen)
                    collisionflag = True
            # Shows windows for Mask and Frame/webcam feed
            camera.show_frames()
        except AttributeError:
            pass

        # If collision has not occurred, erase collisiontext
        if collisionflag == False:
            game.erasecollisiontext(screen)

        # Draw shapes
        game.drawBall(screen)
        if shapes_were_created == True:
            game.drawBlock(screen)

        # Displays the drawings to the screen
        pygame.display.flip()
        # Clear canvas
        screen.fill((255, 255, 255))

        # Ends capture and breaks out of while loop if escape is pressed
        key = cv2.waitKey(1)
        if key == 27:
            camera.end_capture()
            break

    # Check if x button is hit to end video capture
    camera.end_capture()
    # Check if x button is pushed to close window
    pygame.quit()
