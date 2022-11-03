from random import randint
import pygame


class Gem():
    """Program responsible for gem creation, the dimensions of the gem, and their placement in the game. The program ensures the gem placement will never
    exceed the games screen."""
    
    def __init__(self, width):
        self._gem_img = "images/gem.png"
        self._gem = pygame.image.load(self._gem_img)
        self._gem_rect = self._gem.get_rect()

        self._width = width
    
    def get_gem(self):
        return self._gem

    def gen_gem_pos(self):
        max_width = self._width - self._gem_rect.width
        x = randint(0, max_width+1)
        y = 0

        return (x, y)

    def spawn_gem(self):
        self._gem_rect.x, self._gem_rect.y = self.gen_gem_pos()
        return self._gem_rect

    def get_gem_pos(self):
        return self._gem_rect.x, self._gem_rect.y
    
    def move_gem(self, x, y):
        self._gem_rect.x, self._gem_rect.y = x, y
        return self._gem_rect
    
    def get_width(self):
        return self._gem_rect.width
    
    def get_height(self):
        return self._gem_rect.height
