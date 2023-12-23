import pygame, sys
from pygame.locals import *

from gameProperties import settings
from tools import collision

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((settings.windowWidth, settings.windowHeight))

    def run(self):
        while (True):
            self.window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

pygame.init()
game = Game()
game.run()