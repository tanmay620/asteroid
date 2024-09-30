import pygame
import sys
#import constants
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt=0 
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroid=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers=(asteroid,updatable,drawable)
    AsteroidField.containers=updatable
    asteroid_field=AsteroidField()
    shoot=pygame.sprite.Group()
    Shot.containers=(shoot,updatable,drawable)
    player = Player(SCREEN_HEIGHT/2,SCREEN_WIDTH/2)
    while running:
        screen.fill("black")
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        for i in asteroid:
            if i.collision(player):
                print("Game Over")
                sys.exit()
            for j in shoot:
                if i.collision(j):
                    j.kill()
                    i.split()
        pygame.display.flip()
        dt=clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    #print("asteroid")
    #print("screen width "+str(SCREEN_WIDTH))
    #print("screen height "+ str(SCREEN_HEIGHT))  
    
if __name__=="__main__":
    main()