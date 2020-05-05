"""
This is the view file for our Ball Drop Game. It controls the sensory aspects
of the game (e.g. music, menu/button visuals)
"""


import pygame


class SoundEffect:
    """ Represents the sound effects made in the game.
    Files should be in audio file formats such as mp3 and wav

    Attributes:
        start_file: file for music played when on the start menu
        music_file: file for game music played throughout the gameplay
        end_file: file for music played when on the end menu
        win_file: file for music played when the ball lands on the target
        collision_file: file for sound effect played when a collision occurs
    """
    def __init__(self, start_file, music_file, end_file, win_file, collision_file):
        """ Initialize a SoundEffects object.

        This function will save the files you provide it with locally if they
        have not already been saved.
        """
        pass

    def play_start_music(self):
        """ Use pygame.mixer.music.load and pygame.mixer.music.play or other
        functions to play music when on the start menu.
        """
        pass

    def play_game_music(self):
        """ Use pygame.mixer.music.load and pygame.mixer.music.play or other
        functions to play music throughout the gameplay.
        """
        pass

    def play_end_music(self):
        """
        Use pygame.mixer.music.load and pygame.mixer.music.play or other
        functions to play music when on the end menu.
        """
        pass

    def play_win_music(self):
        """
        Use pygame.mixer.music.load and pygame.mixer.music.play or other
        functions to play a sound effect when the player jumps.
        """
        pass

    def play_collision_sound(self):
        """
        Use pygame.mixer.music.load and pygame.mixer.music.play or other
        functions to play a sound effect when the player collides with an
        obstacle.
        """
        pass


class Button:
    """ Creates a Button overlaid with text to be used in a menu.

    Attributes:
        font_style: the style of the text
        font_size: the size of the text
        font_color: the color code for the text
        x_pos: the x-coordinate of the top left corner of the rectangle bounding
        the button
        y_pos: the y-coordinate of the top left corner of the rectangle bounding
        the button
        width: the width of the rectangle bounding the button
        height: the height of the rectangle bounding the button
        text: the button text
        button_color: the color code for the button
        rect: the rectange bounding the button

    """
    def __init__(self, font_style, font_size, font_color, x_pos, y_pos, width, height, text, button_color):
        """ Create Button object with given attributes
        """
        #expected methods assigning parameters to attributes
        #self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pass

    def draw(self):
        """ Draw Button based on the attributes of the instance of the object
        """
        pass


class Menu:
    """ Creates a Menu that contains text (instructions to the user) and one or
    more button(s).

    Attributes:
        font_style: the style of the text
        font_size: the size of the text
        font_color: the color code for the text
        x_pos: the x-coordinate of the top left corner of the rectangle bounding
        the textbox
        y_pos: the y-coordinate of the top left corner of the rectangle bounding
        the textbox
        width: the width of the rectangle bounding the textbox
        height: the height of the rectangle bounding the textbox
        text: the menu text
        button: a Button object
        rect: the rectangle bounding the textbox

    """
    def __init__(self, font_style, font_size, font_color, x_pos, y_pos, width, height, text, button):
        """ Create Menu object with given attributes
        """
        #expected methods assigning parameters to attributes
        #self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pass

    def draw(self):
        """ Draw Button based on the attributes of the instance of the object
        """
        pass


class StartMenu(Menu):
    """ Represents directions for the game, important disclosures, and a start
    button to trigger the beginning of the game. There is no __init__ method so
    it will be called from the superclass.

    All attributes are inherited from the Menu class.
    """

    def text_properties(self):
        """ Alters some of the attributes of the object's text with hard-coded
        entries specific to the start menu
        """
        pass

    def button_properties(self):
        """ Alters some of the attributes of the button with hard-coded
        entries specific to the start menu. One possible button is to "start"
        the game.
        """
        pass


class EndMenu(Menu):
    """ Represents the menu after the player has finished the game.

    All attributes are inherited from the Menu class.
    """

    def text_properties(self):
        """ Alters some of the attributes of the object's text of self with
        entries specific to the end menu
        """
        pass

    def button_properties(self):
        """ Alters some of the attributes of the button with hard-coded
        entries specific to the end menu. Possible buttons are to "restart" or
        "close" the game.
        """
        pass
