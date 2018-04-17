import pygame

class ActionBox(object):
    def init():
        pass
        
    def __init__(self):
        self.x = 25
        self.y = 575
        self.bWidth = 950
        self.bHeight = 200
        self.color = (84, 84, 84)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, \
                         self.bWidth, self.bHeight), 5)
        pygame.display.update()
        