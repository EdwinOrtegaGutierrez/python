import pygame
  
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
def dibuja_hombrepalitos(pantalla, x, y):
    # Cabeza
    pygame.draw.ellipse(pantalla, NEGRO, [1 + x, y, 10, 10], 0)
  
    # Piernas
    pygame.draw.line(pantalla, NEGRO, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(pantalla, NEGRO, [5 + x, 17 + y], [x, 27 + y], 2)
  
    # Cuerpo
    pygame.draw.line(pantalla, ROJO, [5 + x, 17 + y], [5 + x, 7 + y], 2)
  
    # Brazos
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [1 + x, 17 + y], 2)
     
# Inicio
pygame.init()
 
# Establecemos el largo y alto de la pantalla [largo,alto]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)  
pygame.display.set_caption("Mi Juego")
  
#Iteramos hasta que el usuario pulsa el botón de salir.
hecho = False
  
# Usamos esto para gestionar cuán rápido se actualiza la pantalla.
reloj = pygame.time.Clock()
 
# Ocultamos el cursor del ratón.
pygame.mouse.set_visible(0)
 
 
# Velocidad, en píxeles, por fotograma
x_speed = 0
y_speed = 0
  
# Posición actual
x_coord = 10
y_coord = 10
 
# -------- Bucle Principal del Programa -----------
while not hecho:
    #TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
 
 
            # El usuario presiona una tecla
         
        elif evento.type == pygame.KEYDOWN:
            # Mira si ha sido una de las flechas. Si es así
            # ajusta la velocidad.
            if evento.key == pygame.K_LEFT:
                x_speed =- 3
            elif evento.key == pygame.K_RIGHT:
                x_speed = 3
            elif evento.key == pygame.K_UP:
                y_speed =- 3
            elif evento.key == pygame.K_DOWN:
                y_speed = 3
                  
        # El usuario deja de presionar la tecla
        elif evento.type == pygame.KEYUP:
            # Si es una de las flechas, resetea el vector a cero.
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            elif evento.key == pygame.K_RIGHT:
                x_speed = 0
            elif evento.key == pygame.K_UP:
                y_speed = 0
            elif evento.key == pygame.K_DOWN:
                y_speed = 0
                 
    # TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
 
    # Desplaza al objeto según el vector velocidad.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
      
    # Primero, limpiamos la pantalla con color blanco. No pongas otros comandos de dibujo 
    # encima de esto, de lo contrario serán borrados por el comando siguiente.
    pantalla.fill(BLANCO)
     
    dibuja_hombrepalitos(pantalla, x_coord, y_coord) 
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
      
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
  
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
      
# Pórtate bien con el IDLE.
# Si nos olvidamos de ésta línea, el programa se 'colgará'
# en la salida.
pygame.quit()