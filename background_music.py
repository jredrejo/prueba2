# -*- coding: utf-8 -*-
"""
 Aquí mostramos como reproducir música de fondo con Pygame.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import pygame
 
# Definimos algunos colores
BLANCO = (255, 255, 255)
 
pygame.init()
  
# Establecemos la altura y largo de la pantalla
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
 
pygame.display.set_caption("Mi Juego")
 
# Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False
 
# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# Reproduciremos "Oh Fortuna" por el coro del MIT
# Disponible en: 
# http://freemusicarchive.org/music/MIT_Concert_Choir/Carmina_Burana_Carl_Orff/01_1355
pygame.mixer.music.load('MIT_Concert_Choir_-_01_-_O_Fortuna.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()
 
 
 
# -------- Bucle Principal del Programa -----------
while not hecho:

    # TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():  # El usuario hizo algo
        print evento.type
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
        elif evento.type == pygame.constants.USEREVENT:
            # Este evento es disparado cuando la canción deja de reproducirse.
            #
            # Luego, Reproduciremos "Alone" por Saito Koji
            # Disponible en: 
            # http://freemusicarchive.org/music/Saito_Koji/Again/01-Alone

            pygame.mixer.music.load('Saito_Koji_-_01_-_Alone.mp3')
            pygame.mixer.music.play()
             
    # TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR ENCIMA DE ESTE COMENTARIO
  
  
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
     
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
     
    # Primero, limpiamos la pantalla con color blanco. No pongas otros comandos de dibujo 
    # encima de esto, de lo contrario serán borrados por el comando siguiente.
    pantalla.fill(BLANCO)
     
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
     
    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
     
# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
 
pygame.quit ()
