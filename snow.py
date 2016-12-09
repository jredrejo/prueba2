# -*- coding: utf-8 -*- 
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
 
# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
black = [ 0, 0, 0]
white = [255,255,255]
 
# Set the height and width of the screen
size=[400,400]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
star_list=[]
 
# Loop 50 times and add a star in a random x,y position
for i in range(10):
    x=random.randrange(0,400)
    y=random.randrange(0,400)
    star_list.append([x,y])
 
clock = pygame.time.Clock()
 
#Loop until the user clicks the close button.
done=False

nave = pygame.image.load("graficos/marciano.png").convert()
nave.set_colorkey([ 0, 0, 16])
imagen_defondo = pygame.image.load("graficos/espacio.jpg").convert()
navex=200
navey=350
fuente = pygame.font.Font(None, 36)

while done==False:
 
    for evento in pygame.event.get(): # User did something
        if evento.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                navex=navex-3
            if evento.key == pygame.K_RIGHT:
                navex=navex+3            
            
    # Set the screen background
    screen.fill(black)
    screen.blit(imagen_defondo, [0, 0])
 
    # Process each star in the list
    for i in range(len(star_list)):
        # Draw the star
        pygame.draw.circle(screen,white,star_list[i],2)
         
        # Move the star down one pixel
        star_list[i][1]+=1
         
        # If the star has moved off the bottom of the screen
        if star_list[i][1] > 400:
            # Reset it just above the top
            y=random.randrange(-50,-10)
            star_list[i][1]=y
            # Give it a new x position
            x=random.randrange(0,400)
            star_list[i][0]=x
    
    
    # Vuelca la imagen en la pantalla:
    screen.blit(nave, [navex, navey])  
        
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
"""
  Sample code shows "Game Over" message.
   
  Sample Python/Pygame Programs
  Simpson College Computer Science
  http://programarcadegames.com/
  http://simpson.edu/computer-science/
"""
 
import pygame
 
# Definimos algunos colores
NEGRO    = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
VERDE    = (   0, 255,   0)
ROJO      = ( 255,   0,   0)
 
pygame.init()
  
# Establecemos la altura y largo de la pantalla
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
 
pygame.display.set_caption("Ejemplo de: El Juego Se Acabó")
 
#Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False
  
# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
  
# Posición de partida del rectángulo
rect_x = 50
rect_y = 50
 
# Velocidad y dirección del rectángulo
rect_cambio_x = 5
rect_cambio_y = VERDE5
 
# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
# Usamos esta variable booleana para avisar que el juego se acabó variable.
juego_terminado = False;
 
# -------- Bucle Principal del Programa -----------
while not hecho:
     
    # --- Procesamiento de Eventos
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
             
        # Usaremos un click del ratón para indicar que el juego se acabó.
        # Reemplaza éste, y establece juego_terminado a verdadero en tu propio
        # juego cuando sepas que el juego se acabó. (Algo así como vidas==0)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            juego_terminado = True
             
    # --- Lógica del Juego
 
    # Solo mueve y procesa la lógica del juego si éste no ha terminado.
    if juego_terminado == False:
        # Mueve el punto de partida del rectángulo        
        rect_x += rect_cambio_x
        rect_y += rect_cambio_y
 
       # Rebota el rectángulo, si hace falta.
        if rect_y > 450 or rect_y < 0:
            rect_cambio_y = rect_cambio_y * -1
        if rect_x > 650 or rect_x < 0:
            rect_cambio_x = rect_cambio_x * -1
     
    # --- Dibuja el marco
 
    # Establecemos el color de fondo
    #pantalla.fill(NEGRO)

    # Dibujamos el rectángulo
    #pygame.draw.rect(pantalla, VERDE, [rect_x, rect_y, 50, 50])
    texto = fuente.render("Puntos", True, VERDE)
    pantalla.blit(texto, [10,450])    
    pygame.display.flip()
 

    # Si el juego finalizó, dibujamos 'el juego se acabó'.

        
            
             
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
