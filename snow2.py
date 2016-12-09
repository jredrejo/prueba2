
import pygame
import random

pygame.init()

black = [ 0, 0, 0]
white = [255,255,255]
size=[1067,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Space Animation")
imagen_fondo = pygame.image.load("graficos/fondo_bolas.jpg").convert()
celula = pygame.image.load("graficos/chaoz.png").convert()
bala = pygame.image.load("graficos/bala.png").convert()
bola = pygame.image.load("graficos/bola.png").convert()
maestro=pygame.image.load("graficos/maestro.png").convert()
celula.set_colorkey(white)
bola.set_colorkey(white)
maestro.set_colorkey(white)

x_speed = 0
y_speed = 0
x_coord = 300
y_coord = 500
x_speed_bola = 0
y_speed_bola = 0
x_coord_bola = 300
y_coord_bola = 500
bloque_lista = pygame.sprite.Group()
listade_todoslos_sprites = pygame.sprite.Group()



class Personajes(pygame.sprite.Sprite):
    def __init__(self):
        super(Personajes,self).__init__()
        self.image = pygame.image.load("graficos/maestro.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def actualizar(self):
        self.rect.y += 1
        if self.rect.y > 420:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, 680)
        if self.rect.y > 420:
            self.reset_pos()
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, 680)
class Disparo(pygame.sprite.Sprite):
    def __init__(self):
        super(Disparo,self).__init__()
        self.image = pygame.image.load("graficos/bola.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = y_coord_bola
        self.rect.x = x_coord_bola

for i in range(5):
    maestro = Personajes()
    maestro.rect.x = random.randrange(1067)
    maestro.rect.y = random.randrange(450)

    bloque_lista.add(maestro)
    listade_todoslos_sprites.add(maestro)


clock = pygame.time.Clock()
marcador = 0

done=False
while done==False:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            done=True

        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                x_speed = -3
            if evento.key == pygame.K_RIGHT:
                x_speed = 3
            if evento.key == pygame.K_UP:
                y_speed_bola = -3
            if evento.key == pygame.K_DOWN:
                y_speed = 0

        elif evento.type == pygame.KEYUP:

            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
            if evento.key == pygame.K_UP:
                y_speed_bola = -3
            if evento.key == pygame.K_DOWN:
                y_speed = 0

    x_coord += x_speed
    if x_coord<0:
        x_coord=0
    if x_coord>1000:
        x_coord=1000
    if x_coord_bola<0:
        x_coord_bola=0
    if x_coord_bola>1000:
        x_coord_bola=1000
    if y_coord_bola<0:
        x_coord_bola = x_coord
        y_coord_bola = y_coord

    x_coord_bola += x_speed
    y_coord_bola += y_speed_bola



    screen.fill(black)
    screen.blit(imagen_fondo,[0,0])
    screen.blit(celula,[x_coord,y_coord])
    screen.blit(bola,[x_coord_bola,y_coord_bola])

    disparo = Disparo()

    lista_impactos_bloques = pygame.sprite.spritecollide(disparo, bloque_lista, True)
    print "disparo----------",disparo.rect.x,disparo.rect.y
    for maestro in bloque_lista:
        print maestro.rect.x,maestro.rect.y

    for icono in lista_impactos_bloques:
        marcador +=1
        bloque_lista.actualizar()

    

    listade_todoslos_sprites.draw(screen)
    #maestro.reset_pos()


    # Process each star in the list


    pygame.display.flip()
    clock.tick(20)

pygame.quit ()
