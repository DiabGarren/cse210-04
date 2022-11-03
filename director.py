import pygame
import sys
from draw_screen import DrawScreen
from keyboard_support.keyboard_input import Keyboard

class Director(DrawScreen):

    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
        
    """

    def __init__(self, width, height):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            width: The width of the game screen
            height: The height of the game screen
        """
        super(Director, self).__init__(width, height)
        self._play_again = True
        self._keyboard = Keyboard()

    def start_game(self):
        """
        Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        pygame.init()
        self._font = pygame.font.Font('freesansbold.ttf', 24)
        pygame.display.set_caption("Greed")
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
            
