import turtle
import racket1, racket2, ball, utils


myScreen = turtle.Screen()
myScreen.title("Ping Pong by Rachid")
myScreen.bgcolor("black")
myScreen.setup(width=800, height=800)
myScreen.tracer(0)

#racket1
racket1

#racket2
racket2

#ball
ball

#keyboard bindings
myScreen.listen()
myScreen.onkeypress(utils.racket1_up,"w")
myScreen.onkeypress(utils.racket1_down,"s")

#main game loop
while True:
    myScreen.update()