import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill((255,255,255))
pygame.draw.circle(screen,(0,255,0),(200,200),90,15)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

