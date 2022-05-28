import turtle
import time
import random

posponer = 0.1

#GOTO (x, y)

#VARIABLES DEL MARCADOR
Score = 0
HighScore = 0

#MOSTRAR INFORMACION EN LA PANTALLA
Cartel = turtle.Turtle()
Cartel.speed(0)
Cartel.color("white")
Cartel.penup()
Cartel.hideturtle()
Cartel.goto(0, 260)
Cartel.write("Score: 0  |   High score: 0", align = "center", font = ("Courier", 20, "normal"))

#INFO DE GAME OVER EN LA PANTALLA
Game_Over = turtle.Turtle()
Game_Over.speed(0)
Game_Over.color("red")
Game_Over.penup()
Game_Over.hideturtle()
Game_Over.goto(0, 10)
#Game_Over.write("GAME OVER", align = "center", font = ("Courier", 20, "normal"))

#CONFIGURACION DE LA VENTANA
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("Black")
window.setup(width = 600, height = 600)
window.tracer(0)

#CABEZA DE LA SERPIENTE
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("Green")
cabeza.penup() #quita el rastro
cabeza.goto(0, 0)
cabeza.direccion = "stop"

#MOVIMIENTO DE LA SERPIENTE
def arriba():
    cabeza.direccion = "up"
    Game_Over.clear()
def abajo():
    cabeza.direccion = "down"
    Game_Over.clear()
def izquierda():
    cabeza.direccion = "left"
    Game_Over.clear()
def derecha():
    cabeza.direccion = "right"
    Game_Over.clear()

def movimiento():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direccion == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("Red")
comida.penup() #quita el rastro
comida.goto(50, 50)
comida.direccion = "stop"

#CUERPO SNAKE
CuerpoSnake = []

#TECLADO
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")

#APARICION DEL CUERPO
def AnimacionDeLaCola():
    #ANIMACION DE LA COLA
    TotalCola = len(CuerpoSnake)
    for index in range(TotalCola -1, 0, -1):
        x = CuerpoSnake[index -1].xcor()
        y = CuerpoSnake[index -1].ycor()
        CuerpoSnake[index].goto(x, y)

    if TotalCola > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()

        CuerpoSnake[0].goto(x, y)

#BUCLE DEL PROGRAMA
while True:
    window.update()

    #COLICION CON LOS MARCOS DEL JUEGO
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(0.1)
        cabeza.goto(0,0)
        cabeza.direccion = "stop"

        #ESCONDER CUERPO UNA VEZ DA GAME OVER
        for ColaSnake in CuerpoSnake:
            ColaSnake.goto(1000, 1000)
        CuerpoSnake.clear()

        #RESETEAR EL MARCADOR
        Score = 0
        Cartel.clear()
        Cartel.write(f"Score: {Score}   |   High score: {HighScore}", align = "center", font = ("Courier", 20, "normal"))
        Game_Over.write("GAME OVER", align = "center", font = ("Courier", 40, "normal"))

    #POSICION RANDOM DE LA COMIDA
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280) 
        y = random.randint(-280, 270) 
        comida.goto(x, y)

        #COLA DE LA SERPIENTE
        ColaSnake = turtle.Turtle()
        ColaSnake.speed(0)
        ColaSnake.shape("circle")
        ColaSnake.color("Gray")
        ColaSnake.penup() #quita el rastro
        CuerpoSnake.append(ColaSnake)
        #AUMENTAR MARCADOR
        Score += 10

        if Score > HighScore:
            HighScore = Score
        Cartel.clear()
        Cartel.write(f"Score: {Score}   |  High score: {HighScore}", align = "center", font = ("Courier", 20, "normal"))
    
    AnimacionDeLaCola()
    movimiento()
    
    #ColicionSnake():
    for ColaSnake in CuerpoSnake:
        if ColaSnake.distance(cabeza) < 5:
            time.sleep(0.1)
            cabeza.goto(0, 0)
            cabeza.direccion = "stop"
        
        #ESCONDER ELEMENTOS
            for ColaSnake in CuerpoSnake:
                ColaSnake.goto(1000, 1000)

            CuerpoSnake.clear()
            #RESETEAR EL MARCADOR
            Score = 0
            Cartel.clear()
            Cartel.write(f"Score: {Score}   |  High score: {HighScore}", align = "center", font = ("Courier", 20, "normal"))
            Game_Over.write("GAME OVER", align = "center", font = ("Courier", 40, "normal"))

    time.sleep(posponer)