#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import math

 
class Bicho(pygame.sprite.Sprite):
    def __init__(self):
        """ Constructor. Pass in the color of the block, 
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Bicho,self).__init__() 
        robotito1 = pygame.image.load("graficos/celula.png")
        robotito2 = pygame.image.load("graficos/chaoz.png")
        self.mis_imagenes= (robotito1, robotito2)
        self.image = self.mis_imagenes[0]
        self.imagen_actual = 0
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        
    def update(self):
        self.rect.x = self.rect.x + 1
        self.rect.y = self.rect.y - 1
        if self.rect.y == 0:
            self.rect.y = 300
        self.image = self.mis_imagenes[self.imagen_actual]
        self.imagen_actual = self.imagen_actual + 1
        if self.imagen_actual == 2:
            self.imagen_actual = 0

        

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        """ Constructor. Pass in the color of the block, 
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Pelota,self).__init__() 
        pelota = pygame.image.load("graficos/bola.png")
        self.image = pelota
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 650)
        self.rect.y = random.randrange(10, 350)
        
    def update(self):
        self.rect.x = self.rect.x + 1
        self.rect.y = self.rect.y - 20 * math.sin(self.rect.x )
        if self.rect.y == 0:
            self.rect.y = 300
        if self.rect.x >= 700:
            self.rect.x = 10


pygame.init()
  
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


done=False

robotito = pygame.image.load("graficos/celula.png")
clock = pygame.time.Clock()



lista_de_sprites= pygame.sprite.Group()
lista_de_pelotas = pygame.sprite.Group()
bichito1 = Bicho()
lista_de_sprites.add(bichito1)

for i in range(30):
    pelota = Pelota()
    lista_de_sprites.add(pelota)
    lista_de_pelotas.add(pelota)


puntos = 0

while not done:
    
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  
    screen.fill(( 255, 255, 255))
    
    lista_de_sprites.update()
    
    choques = pygame.sprite.spritecollide(bichito1, lista_de_pelotas, True)
    for choque in choques:
        puntos = puntos +1
        print puntos
    
    
    
    lista_de_sprites.draw(screen)
    

    pygame.display.flip()
    clock.tick(10)
    

