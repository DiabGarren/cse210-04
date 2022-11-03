import pygame

class Player():

    def __init__(self, width, height):
        self._player_img = "images/player.png"
        self._player = pygame.image.load(self._player_img)
        self._player_rect = self._player.get_rect()

        self._player_x = width//2
        self._player_y = height

    def get_player(self):
        return self._player
    
    def spawn_player_pos(self):
        self._player_y -= self._player_rect.height
        return self._player_x, self._player_y

    def spawn_player(self):
        self._player_rect.x, self._player_rect.y = self.spawn_player_pos()
        return self._player_rect

    def get_player_pos(self):
        return self._player_x, self._player_y

    def move_player(self, x, y):
        self._player_x, self._player_y = x, y
        self._player_rect.x, self._player_rect.y = self._player_x, self._player_y
        return self._player_rect

    def get_width(self):
        return self._player_rect.width

    def get_height(self):
        return self._player_rect.height