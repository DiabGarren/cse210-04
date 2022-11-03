import pygame
import sys
from draw_screen import DrawScreen
from keyboard_support.keyboard_input import Keyboard

class Director(DrawScreen):

    def __init__(self, width, height):
        super(Director, self).__init__(width, height)
        self._play_again = True
        self._keyboard = Keyboard()

    def start_game(self):
        pygame.init()
        self._font = pygame.font.Font('freesansbold.ttf', 24)
        self._screen = pygame.display.set_mode(self._size)
        self.clear_screen()

        while self._play_again:
            
            
            self._screen.blit(self._rock.get_rock(), self._rocks[0])
            self._screen.blit(self._gem.get_gem(), self._gems[0])
            self._screen.blit(self._player.get_player(), self._player.spawn_player())
            self._screen.blit(self._score_obj.display_score(), (10, 10))
            pygame.display.update()

            while self._is_playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                self.clear_screen()
                pygame.time.wait(self.FPS)
                self._frames += 1
                self.draw_player()
                self.draw_rock()
                self.draw_gem()
                self.collision()
                self.update_score()

                
                pygame.display.update()
            
            self.clear_screen()
            self.game_over()
            pygame.display.update()
            
            while True:
                if self._keyboard.restart():
                    self._is_playing = True
                    self.restart()
                    break
                elif self._keyboard.restart() == False:
                    sys.exit()
            
