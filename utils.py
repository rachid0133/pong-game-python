import racket1, racket2


def racket1_up():
    y = racket1.racket1.ycor()
    y += 20
    racket1.racket1.sety(y)

def racket1_down():
    y = racket1.racket1.ycor()
    y -= 20
    racket1.racket1.sety(y)

def racket2_up():
    y = racket2.racket2.ycor()
    y += 20
    racket2.racket2.sety(y)

def racket2_down():
    y = racket2.racket2.ycor()
    y -= 20
    racket2.racket2.sety(y)