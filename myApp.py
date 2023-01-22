import turtle
import racket1, racket2


myScreen = turtle.Screen()
myScreen.title("Ping Pong by Rachid")
myScreen.bgcolor("black")
myScreen.setup(width=800, height=800)
myScreen.tracer(0)

#racket1
racket1

#racket2
racket2

#main game loop
while True:
    myScreen.update()