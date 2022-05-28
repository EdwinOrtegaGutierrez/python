import pygame
 
def dibujar_hombredenieve(pantalla, x, y):
    """ --- Función para dibujara al hombre de nieve ---
    Define una función que dibujará un hombre de nieve en una determinada ubicación.
    """
    pygame.draw.ellipse(pantalla, BLANCO, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(pantalla, BLANCO, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(pantalla, BLANCO, [0 + x, 65 + y, 100, 100])
     
# Inicializamos el motor de juegos.
pygame.init()
 
# Definimos en formato RGB los colores que usaremos.
NEGRO = [0,   0,   0]
BLANCO = [255, 255, 255]
 
# Establecemos el largo y alto de la pantalla
dimensiones = [400, 500]
pantalla = pygame.display.set_mode(dimensiones)
 
#Iteramos hasta que el usuario pulse el botón de salida.
hecho = False
reloj = pygame.time.Clock()
 
while not hecho:
 
    for evento in pygame.event.get(): # El usuario realizó alguna acción.
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir.
            hecho = True # Marcamos que hemos acabado y abandonamos este bucle.
 
 
    # Establecemos el color de fondo.
    pantalla.fill(NEGRO)
 
    # Posicionamos al hombre de nieve en la esquina superior izquierda de la pantalla.
    dibujar_hombredenieve(pantalla, 10, 10)
     
    # Posicionamos al hombre de nieve en la esquina superior derecha de la pantalla.
    dibujar_hombredenieve(pantalla, 300, 10)
     
    # Posicionamos al hombre de nieve en la esquina inferior izquierda de la pantalla.
    dibujar_hombredenieve(pantalla, 10, 300)
 
    # Avanzamos y actualizamos con lo que hemos dibujado.
    # Esto DEBE suceder después de todos los otros comandos de dibujo.
    pygame.display.flip()
 
    # Limitamos el bucle while a 60 veces por segundo.
    # Salimos y usamos toda la CPU que podamos.
    reloj.tick(60)
     
 
# Pórtate bien con el IDLE.
pygame.quit ()