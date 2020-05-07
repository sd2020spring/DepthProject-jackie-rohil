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
from threading import Thread
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
        self.bkgd_color = bkgd_color
        self.game_status = "start"
        #self.ball = ball
        #self.block = block

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
        self.ball = Ball()
        self.ball.draw(screen)

    def moveBall(self):
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
        #self.ball.hitbox = pygame.Rect(self.ball.x_pos, self.ball.y_pos, self.ball.width, self.ball.height)

    def drawBall(self, screen):
        self.ball.draw(screen)

    def createBlock(self, screen, x, y, angle, width, height):
        self.block = Block(x, y, angle, width, height)

    def drawBlock(self, screen):
        self.block.draw(screen)

    def collisiontext(self, screen):
        """ TODO: Move relevant code from main function to this function.
        """
        textfont = pygame.font.SysFont('Arial', 15)
        textsurface = textfont.render('You Lose!', False, (0, 0, 0))
        screen.blit(textsurface,(0,0))

    def erasecollisiontext(self, screen):
        """ TODO: Move relevant code from main function to this function.
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
        self.color = (255,0,0)
        self.hitbox = pygame.Rect(x_pos-radius,y_pos-radius,2*radius,2*radius)

    def move(self):
        """ Makes the ball move by changing the coordinates of its center point.
        """
        pass

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
        x_pos: the x-coordinate of the top left corner of the target
        y_pos: the y-coordinate of the top left corner of the target
        width: the width of the target
        height: the height of the target
        hitbox: the rectangle that defines the feature's target
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
    camera = ImageController()
    camera.create_trackbars()

    pygame.init()
    # set screen to size of OpenCV video
    screen = pygame.display.set_mode([640, 480])

    game = GameEnvironment()

    running = True

    # Fill the background with the color specified the game object
    screen.fill(game.bkgd_color)
    pygame.display.flip()
    #capture video from webcam

    #create ball object at initial position
    game.createBall(screen)

    shapes_were_created = False
    last_hitboxList = []
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(game.bkgd_color)

        #contains hitboxes for ball and block
        hitboxList = []
        collisionflag = False
        block_width = 100
        try:
            camera.create_hsv_mask()

            #says if rectangle has been detected, gives x and y pos if it has
            isRectangle, x, y = camera.detect_rectangle()
            #what should be executed if OpenCV detects a rectangle
            if (isRectangle):
                #create Block object, add hitbox to hitboxList, and draw
                game.createBlock(screen,x-block_width,y,0,block_width,block_width)
                hitboxList.append(game.block.hitbox)
                #change ball position, add hitbox to hitboxList, and draw
                game.moveBall()
                hitboxList.append(game.ball.hitbox)
            #check for collision between ball and block
            shapes_were_created = True
            if len(hitboxList) != 0:
                print("hitboxlist not zero")
                print(hitboxList)
                print(type(hitboxList[0]))
                if hitboxList[0].colliderect(hitboxList[1]):
                    game.collisiontext(screen)
                    print("collision")
                    collisionflag = True
            camera.show_frames()
        except AttributeError:
            pass

        if collisionflag == False:
            game.erasecollisiontext(screen)

        game.drawBall(screen)
        if shapes_were_created == True:
            print("shapes were created")
            game.drawBlock(screen)

        #Flip the display
        pygame.display.flip()
        screen.fill((255, 255, 255))

        key = cv2.waitKey(1)
        if key == 27:
            break

    camera.end_capture()
    #check if x button is pushed to close window
    pygame.quit()
