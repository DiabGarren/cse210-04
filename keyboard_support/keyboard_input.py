import keyboard

class Keyboard():
    
    def __init__(self):
        self._left = 'a' 
        self._right = 'd'

        self._up = 'w'
        self._down = 's'

        self._restart_y = 'y'
        self._restart_n = 'n'
    
    def move_x(self):
        if keyboard.is_pressed(self._left):
            return -10
        elif keyboard.is_pressed(self._right):
            return 10
        else:
            return 0

    def move_y(self):
        if keyboard.is_pressed(self._up):
            return -10
        elif keyboard.is_pressed(self._down):
            return 10
        else:
            return 0
    
    def restart(self):
        if keyboard.is_pressed(self._restart_y):
            return True
        elif keyboard.is_pressed(self._restart_n): 
            return False