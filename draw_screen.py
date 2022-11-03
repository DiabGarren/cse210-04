import pygame
from sprites.rock import Rock
from sprites.gem import Gem
from sprites.player import Player
from keyboard_support.player_movement import player_movement
from score import Score


class DrawScreen():

    def __init__(self, width, height):
        self._size = (width, height)
        self._rock = Rock(width)
        self._rocks = []
        self._rocks.append(self._rock.gen_rock_pos())

        self._gem = Gem(width)
        self._gems = []
        self._gems.append(self._gem.gen_gem_pos())

        self._player = Player(width, height)
        self._movement = player_movement()
        self._frames = 0

        self._score = 0
        self._score_obj = Score(self._score)
        
        self.FPS = int(1000/30)
        self._move_time = 15

        self._is_playing = True

    def clear_screen(self):
        self._screen.fill((0, 0, 0))     

    def draw_rock(self):
        
        for rocks in self._rocks:
            x, y = rocks

            if self._frames%self._move_time == 0:
                y += 15
                self._rocks[self._rocks.index((x, y-15))] = (x, y)

                if y > self._size[1]:
                    self._rocks.pop(self._rocks.index((x, y)))

            self._screen.blit(self._rock.get_rock(), self._rock.move_rock(x, y))
                
        if self._frames%40 == 0:
            self._rocks.append(self._rock.gen_rock_pos())

    def draw_gem(self):

        for gems in self._gems:
            x, y = gems

            if self._frames%self._move_time == 0:
                y += 15
                self._gems[self._gems.index((x, y-15))] = (x, y)
                
                if y > self._size[1]:
                    self._gems.pop(self._gems.index((x, y)))
            
            self._screen.blit(self._gem.get_gem(), self._gem.move_gem(x, y))
        
        if self._frames%40 == 0:
            self._gems.append(self._gem.gen_gem_pos())
        
        print(len(self._gems), len(self._rocks))
    
    def draw_player(self):
        x, y = self._player.get_player_pos()
        x, y = self._movement.move_player(x, y)
        self._screen.blit(self._player.get_player(), self._player.move_player(x, y))
    
    def collision(self):
        player_x = self._player.get_player_pos()[0], self._player.get_player_pos()[0] + self._player.get_width()
        player_y = self._player.get_player_pos()[1], self._player.get_player_pos()[1] + self._player.get_height()
        
        for rocks in self._rocks:
            rock_x_centre = (rocks[0]*2 + self._rock.get_width())/2
            rock_y_bot = rocks[1]

            if (rock_x_centre >= player_x[0] and rock_x_centre <= player_x[1]) and (rock_y_bot >= player_y[0] and rock_y_bot <= player_y[1]):
                if self._score <= 0:
                    self._is_playing = False
                else:
                    self._score -= 1
                    self._rocks.pop(self._rocks.index(rocks))
            
        for gems in self._gems:
            gem_x_centre = (gems[0]*2 + self._gem.get_width())/2
            gem_y_bot = gems[1]

            
            if (gem_x_centre >= player_x[0] and gem_x_centre <= player_x[1]) and (gem_y_bot >= player_y[0] and gem_y_bot <= player_y[1]):
                self._score += 1
                self._gems.pop(self._gems.index(gems))
        

    def update_score(self):
        self._score_obj.change_score(self._score)
        self._screen.blit(self._score_obj.display_score(), (10, 10))

    def game_over(self):
        font = pygame.font.Font('freesansbold.ttf', 24)
        text1 = "Game over"
        text2 = f"Score: {self._score}"
        text3 = "Restart: y/n"
        self._screen.blit(font.render(text1, 1, (255, 55, 55)), (self._size[0]/2, 100))
        self._screen.blit(font.render(text2, 1, (255, 55, 55)), (self._size[0]/2, 150))
        self._screen.blit(font.render(text3, 1, (255, 55, 55)), (self._size[0]/2, 200))
    
    def restart(self):
        self._score = 0
        self._score_obj.change_score(self._score)

        self._rocks = []
        self._rocks.append(self._rock.gen_rock_pos())

        self._gems = []
        self._gems.append(self._gem.gen_gem_pos())

        self._player.move_player(self._size[0]/2, self._size[1]-self._player.get_height())