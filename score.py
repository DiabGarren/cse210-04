import pygame

class Score():
    """Program keeps count of the players score. It tracks the players collision with rocks and gems. If the player touches a gem they gain a point, if they touch 
    a rock lose a point. When they reach zero points the game ends however, the player can re-play the game as many times as they want."""
    
    def __init__(self, score:int):
        self._score = score
    
    def change_score(self, new_score:int):
        self._score = new_score
    
    def get_score(self):
        return self._score
    
    def display_score(self):
        self._font = pygame.font.Font('freesansbold.ttf', 24)
        self._score_obj = self._font.render(f"Score: {self.get_score()}", 1, (255, 255, 255))
        return self._score_obj
