import pygame
  
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
def dibuja_hombrepalitos(pantalla, x, y):
    """Dibuja un hombre en la posición x, y """
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
 
# Establecemos el largo y alto de la pantalla [largo, alto]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)  
pygame.display.set_caption("Mi Juego")
  
#Iteramos hasta que el usuario pulsa el botón de salir.
hecho = False
  
# Usamos esto para gestionar cuán rápido se actualiza la pantalla.
reloj = pygame.time.Clock()
 
# Ocultamos el cursor del ratón.
pygame.mouse.set_visible(0)
 
# Posición actual
x_coord = 10
y_coord = 10
 
# Cuenta el número de joysticks en el ordenador
numero_de_joysticks = pygame.joystick.get_count()
if numero_de_joysticks == 0:
    # No hay joysticks!
    print ("Error, no he encontrado ningún joystick.")
else:
    # Usamos el joystick #0 y lo inicializamos
    mi_joystick = pygame.joystick.Joystick(0)
    mi_joystick.init()
             
while not hecho:
 
    #TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
             
    # TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
             
    # Mientras halla un joystick
    if numero_de_joysticks != 0:
     
        # Esto obtiene la posición del eje en el control del juego
        # Devuelve un número entre -1.0 y +1.0
        horiz_axis_pos = mi_joystick.get_axis(0)
        vert_axis_pos = mi_joystick.get_axis(1)   
         
        # Desplaza x de acuerdo al eje. Multiplicamos por 10 para acelerar el movimiento.
        x_coord = x_coord + int(horiz_axis_pos * 10)
        y_coord = y_coord + int(vert_axis_pos * 10)
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
      
    # Primero, limpiamos la pantalla con color blanco. No pongas otros comandos de dibujo 
    # encima de esto, de lo contrario serán borrados por el comando siguiente.
    pantalla.fill(BLANCO)    
 
    # Dibuja el objeto en las coordenadas apropiadas.
    dibuja_hombrepalitos(pantalla, x_coord, y_coord)       
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    pygame.display.flip()
    reloj.tick(60)
     
pygame.quit()