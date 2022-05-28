import math
import pygame
import random
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
 
# Esta clase representa la pelota
# Se deriva de la clase "Sprite" en Pygame
class Pelota(pygame.sprite.Sprite):    
     
    # Constructor. Pasa el color y las posiciones x e y de la pelota.
    def __init__(self):
        # Llamada al constructor de la clase padre (Sprite) 
        super().__init__()
         
        # Creamos la imagen de la pelota
        self.image = pygame.Surface([10, 10])
         
        # Color de la pelota
        self.image.fill((BLANCO))
         
        # Obtenemos un objeto rectángulo para mostrar donde se encuentra nuestra imagen
        self.rect = self.image.get_rect()
         
        # Obtenemos los atributos para el alto/largo de la pantalla
        self.alto_pantalla = pygame.display.get_surface().get_height()
        self.largo_pantalla = pygame.display.get_surface().get_width()
 
        # Velocidad en píxeles por ciclo
        self.velocidad = 0
 
        # Representación en coma flotante de la ubicación de la pelota
        self.x = 0
        self.y = 0
 
        # Rumbo de la pelota en grados
        self.rumbo = 0
 
        # Altura y largo de la pelota
        self.largo = 10
        self.alto = 10
         
         
        # Definimos la posición y velocidad inicial de la pelota
        self.reset()
         
    def reset(self):
        self.x = random.randrange(50,750)
        self.y = 350.0
        self.velocidad = 8.0
 
        # Rumbo de la pelota (en grados)
        self.rumbo = random.randrange(-45,45)
         
        # Lanzamos una 'moneda'
        if random.randrange(2) == 0 :
            # Revertimos el rumbo de la pelota y dejamos que le llegue primero a nuestro compañero.
            self.rumbo += 180
            self.y = 50
         
    # Esta función hará rebotar la pelota sobre una superficie horizontal (no en una vertical)
    def botar(self,diff):
        self.rumbo = (180-self.rumbo) % 360
        self.rumbo -= diff
         
        # Aceleramos la bola hacia arriba
        self.velocidad *= 1.1
     
    # Actualizamos la posición de la pelota
    def update(self):
        # El Seno y el Coseno funcionan en grados, por eso tenemos
        # que convertirlos a radianes
        rumbo_radianes = math.radians(self.rumbo)
         
        # Modificamos la posición (x e y) en función de la velocidad y el rumbo
        self.x += self.velocidad * math.sin(rumbo_radianes)
        self.y -= self.velocidad * math.cos(rumbo_radianes)
         
        if self.y < 0:
            self.reset()
             
        if self.y > 600:
            self.reset()
             
        # Desplazamos la imagen hacia donde se encuentran x e y.
        self.rect.x = self.x
        self.rect.y = self.y
         
        # ¿Hemos botado contra el lado izquierdo de la pantalla?
        if self.x <= 0:
            self.rumbo = (360-self.rumbo)%360
            print(self.rumbo)
            #self.x=1
             
        # ¿Hemos botado contra el lado derecho de la pantalla?
        if self.x > self.largo_pantalla-self.largo:
            self.rumbo = (360-self.rumbo)%360
                
# Esta clase representa la barra inferior que controla el protagonista
class Protagonista(pygame.sprite.Sprite):
    # Función constructor
    def __init__(self, joystick, y_pos):
        # Llamada al constructor padre
        super().__init__()
         
        self.largo = 75
        self.alto = 15
        self.image = pygame.Surface([self.largo, self.alto])
        self.image.fill((BLANCO))
        self.joystick = joystick
         
        # Hacemos que la esquina superior izquierda sea la ubicación inicial.
        self.rect = self.image.get_rect()
        self.alto_pantalla = pygame.display.get_surface().get_height()
        self.largo_pantalla = pygame.display.get_surface().get_width()
 
        self.rect.x = 0
        self.rect.y = y_pos
     
    # Actualizamos al protagonista
    def update(self):
         
        # Esto obtiene la posición del eje en el mando de juego
        # Devuelve un número entre -1.0 y +1.0
        horiz_axis_pos = self.joystick.get_axis(0)
          
        # Desplaza x en función del eje. Multiplicamos por 15 para acelerar el movimiento.
        self.rect.x = int(self.rect.x+horiz_axis_pos*15)
                 
        # Nos aseguramos que no hemos empujado la pala del protagonista fuera del lado derecho de la pantalla.
        if self.rect.x > self.largo_pantalla - self.largo:
            self.rect.x = self.largo_pantalla - self.largo
 
puntuacion1 = 0
puntuacion2 = 0
 
# Iniciamos Pygame
pygame.init()
 
# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([800, 600])
 
# Establecemos rl título de la ventana
pygame.display.set_caption('Pong')
 
# Habilitamos esto para que el ratón desaparezca cuando esté encima de nuestra ventana.
pygame.mouse.set_visible(0)
 
# Fuente para dibujar el texto en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
# Creamos una superficie sobre la que poder dibujar
imagen_de_fondo = pygame.Surface(pantalla.get_size())
 
# Creamos la pelota
pelota = Pelota()
# Creamos un grupo de 1 pelota (usada para comprobar colisiones)
pelotas = pygame.sprite.Group()
pelotas.add(pelota)
 
# Cuenta los joysticks conectados al ordenador
joystick_count = pygame.joystick.get_count()
if joystick_count < 1:
    # No hay joysticks!
    print ("Error, no he podido encontrar suficientes joysticks.")
    pygame.quit()
    exit()
else:
    # Usamos el  joystick #0 y lo inicializamos
    joystick1 = pygame.joystick.Joystick(0)
    joystick1.init()
    joystick2 = pygame.joystick.Joystick(1)
    joystick2.init()
     
# Creamos los objetos pala protagonistas
pala1 = Protagonista(joystick1,580)
pala2 = Protagonista(joystick2,25)
 
desplazar_sprites = pygame.sprite.Group()
desplazar_sprites.add(pala1)
desplazar_sprites.add(pala2)
desplazar_sprites.add(pelota)
 
reloj = pygame.time.Clock()
hecho = False
salirdel_programa = False
 
while not salirdel_programa:
    reloj.tick(30)
     
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salirdel_programa = True
     
    # Detenemos el juego si hay una diferencia de 3 puntos
    if abs(puntuacion1 - puntuacion2) > 3:
        hecho = True
         
    if not hecho:
        # Actualizamos las posiciones de las palas y la pelota
        pala1.update()
        pala2.update()
        pelota.update()
     
    # Si hemos acabado, mostramos el mensaje 'game over'
    if hecho:
        texto = fuente.render("Game Over", 1, (200, 200, 200))
        textopos = texto.get_rect(centerx=imagen_de_fondo.get_width()/2)
        textopos.top = 50
        pantalla.blit(texto, textopos)
     
    # Observamos si la pelota golpea la pala.
    if pygame.sprite.spritecollide(pala1, pelotas, False):
        # El 'diff' te permite botar la pelota, a la izquierda o derecha, dependiendo conque parte de la pala la golpeaste.
        diff = (pala1.rect.x + pala1.largo/2) - (pelota.rect.x+pelota.largo/2)
         
        # Establecemos la posición y de la pelota en caso la golpeemos con el borde de la pala.
        pelota.y = 570
        pelota.botar(diff)
        puntuacion1 += 1
     
    # Observamos si la pelota golpea la pala.
    if pygame.sprite.spritecollide(pala2, pelotas, False):
        # El 'diff' te permite botar la pelota, a la izquierda o derecha, dependiendo conque parte de la pala la golpeaste.
        diff = (pala2.rect.x + pala2.largo/2) - (pelota.rect.x+pelota.largo/2)
         
        # Establecemos la posición y de la pelota en caso la golpeemos con el borde de la pala.
        pelota.y = 40
        pelota.botar(diff)
        puntuacion2 += 1
     
    # Imprimimos la puntuación
    imprimir_puntuacion = "Protagonista 1: " + str(puntuacion1)
    texto = fuente.render(imprimir_puntuacion, 1, BLANCO)
    textopos = (0,0)
    pantalla.blit(texto, textopos)
 
    imprimir_puntuacion = "Protagonista 2: " + str(puntuacion2)
    texto = fuente.render(imprimir_puntuacion, 1, BLANCO)
    textopos = (300,0)
    pantalla.blit(texto, textopos)
     
    #Dibujamos todo
    desplazar_sprites.draw(pantalla)
     
    # Actualizamos la pantalla
    pygame.display.flip()
 
    reloj.tick(30)
 
pygame.quit()