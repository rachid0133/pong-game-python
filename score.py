import turtle
sc1=0
sc2=0

sc = turtle.Turtle()
sc.speed(0)
sc.color("blue")
sc.penup()
sc.hideturtle()
sc.goto(0,260)

def score_increment(sc1, sc2):
    sc.write("Player 1: {} Player 2: {}".format(sc1,sc2), align="center", font=("Courier",24,"normal"))
