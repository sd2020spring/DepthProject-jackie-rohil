#FinalProject (Controller)

class KeyboardController:
    """ Checks for user input from clicking keys on the keyboard in order to
    move the penguin.

    Attributes:
        is_pressed: boolean indicating whether a key is pressed
        key: the event key, shows which key is pressed (up arrow, down
        arrow)
        freq: the number of times the key was pressed in quick succession (if
        up arrow was clicked twice quickly, a bigger jump occurs)
    """
    def __init__(self, is_pressed, key, freq):
        """ Assigns provided parameters to a new KeyboardController object. The
        attributes of this object will be checked within GameEnvironment to
        control the movement of the player.
        """
        pass


class MouseController:
    """ Checks for user input from clicking the mouse in order to click on
    buttons.

    Attributes:
        is_pressed: boolean indicating whether the left mouuse button is pressed
    """
    def __init__(self, is_pressed):
        """ Assigns provided parameters to a new MouseController object. The
        attributes of this object will be checked within GameEnvironment navigate
        on the menu pages.
        """
        pass
