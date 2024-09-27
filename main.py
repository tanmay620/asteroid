import pygame
#import constants
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    print("asteroid")
    print("screen width "+str(SCREEN_WIDTH))
    print("screen height "+ str(SCREEN_HEIGHT))    
    
if __name__=="__main__":
    main()