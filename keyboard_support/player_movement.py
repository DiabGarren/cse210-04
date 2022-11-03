from keyboard_support.keyboard_input import Keyboard

class player_movement(Keyboard):
    """Inherits the attributes and functions from class Keyboard to control player movement. Set an x, y location to manipulate players location."""
    
    def __init__(self):
        super(player_movement, self).__init__()
    
    def move_player(self, x, y):
        x += self.move_x()
        y += self.move_y()
        return x, y
