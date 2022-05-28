import pygame
  
# Inicializamos el motor de juego
pygame.init()
  
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
  
PI = 3.141592653
 
# Establecemos el largo y alto de la pantalla.
dimensiones = (400, 300)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Código de ejemplo para el módulo de dibujo")
 
#Iteramos hasta que el usuario haga click sobre el botón de salida.
hecho = False
reloj = pygame.time.Clock()
 
# Iteramos en el bucle hasta que hecho == False 
while not hecho:
   
    for evento in pygame.event.get(): # El usuario realizó alguna acción
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir
            hecho = True # Marcamos que hemos acabado y abandonamos este bucle
  
 
    # Todo el código de dibujo sucede después del bucle for y dentro del bucle
    # while not hecho.
     
    # Limpiamos la pantalla y establecemos su fondo.    
    pantalla.fill(BLANCO)
 
    # Dibujamos sobre la pantalla una línea verde de 5 píxeles de ancho que vaya
    # desde (0,0) hasta (50,75).    
    pygame.draw.line(pantalla, VERDE, [0, 0], [50, 75], 5)
      
    # Dibujamos sobre la pantalla varias líneas negras de 5 píxeles de ancho.     
    pygame.draw.lines(pantalla, NEGRO, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
         
    # Dibujamos sobre la pantalla una línea verde de 5 píxeles de ancho que vaya
    # desde (0,50) hasta (50,80).    
    pygame.draw.aaline(pantalla, VERDE, [0, 50], [50, 80], True)
 
    # Dibujamos el borde de un rectángulo.    
    pygame.draw.rect(pantalla, NEGRO, [75, 10, 50, 20], 2)
      
    # Dibujamos un rectángulo sólido.    
    pygame.draw.rect(pantalla, NEGRO, [150, 10, 50, 20])
      
    # Dibujamos el borde de una elipse, usando un rectángulo para definir sus bordes.    
    pygame.draw.ellipse(pantalla, ROJO, [225, 10, 50, 20], 2) 
 
    # Dibujamos una elipse sólida, usando un rectángulo para definir sus bordes.
    pygame.draw.ellipse(pantalla, ROJO, [300, 10, 50, 20]) 
  
    # Dibujamos un triángulo utilizando el comando polygon
    pygame.draw.polygon(pantalla, NEGRO, [[100, 100], [0, 200], [200, 200]], 5)
   
    # Dibujamos un arco como parte de una elipse. 
    # Usamos radianes para determinar qué ángulo tenemos que dibujar.
    pygame.draw.arc(pantalla, NEGRO, [210, 75, 150, 125],  0, PI / 2, 2)
    pygame.draw.arc(pantalla, VERDE, [210, 75, 150, 125],  PI / 2, PI, 2)
    pygame.draw.arc(pantalla, AZUL,  [210, 75, 150, 125],  PI, 3 * PI / 2, 2)
    pygame.draw.arc(pantalla, ROJO,   [210, 75, 150, 125], 3 * PI / 2, 2 * PI, 2)
     
    # Dibujamos un círculo
    pygame.draw.circle(pantalla, AZUL, [60, 250], 40)
     
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # Esto DEBE suceder después del resto de comandos de dibujo.
    pygame.display.flip()
     
    # Aquí limitamos el bucle while a un máximo de 60 veces por segundo.
    #Lo dejamos aquí y usamos toda la CPU que podamos.
    reloj.tick(60)
    
# Pórtate bien con el IDLE.
pygame.quit()