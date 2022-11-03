from random import randint
import pygame


class Rock():
    """Program responsible for rock creation, the dimensions of the rock, and their placement in the game. The program ensures the rock placement will never
    exceed the games screen."""
    
    def __init__(self, width):
        self._rock_img = "images/rock.png"
        
        self._rock = pygame.image.load(self._rock_img)
        self._rock_rect = self._rock.get_rect()

        self._screen_width = width
    
    def get_rock(self):
        return self._rock

    def gen_rock_pos(self):
        max_width = self._screen_width - self._rock_rect.width
        x = randint(0, max_width+1)
        y = 0

        return (x, y)

    def spawn_rock(self):
        self._rock_rect.x, self._rock_rect.y = self.gen_rock_pos()
        return self._rock_rect

    def get_rock_pos(self):
        return self._rock_rect.x, self._rock_rect.y
    
    def move_rock(self, x, y):
        self._rock_rect.x, self._rock_rect.y = x, y
        return self._rock_rect

    def get_width(self):
        return self._rock_rect.width

    def get_height(self):
        return self._rock_rect.height
