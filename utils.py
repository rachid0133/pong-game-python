import racket1, racket2, ball, score


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



def move_ball():
    ball.bl.setx(ball.bl.xcor() + ball.bl.dx)
    ball.bl.sety(ball.bl.ycor() + ball.bl.dy)

    #border check
    if ball.bl.ycor()>290:
        ball.bl.sety(290)
        ball.bl.dy *= -1
    elif ball.bl.ycor()<-290:
        ball.bl.sety(-290)
        ball.bl.dy *= -1
    elif ball.bl.xcor()>390:
        ball.bl.goto(0,0)
        ball.bl.dx *= -1
        score.sc1+=1
        score.sc.clear()
        score.score_increment(score.sc1,score.sc2)
    elif ball.bl.xcor()<-390:
        ball.bl.goto(0,0)
        ball.bl.dx *= -1
        score.sc2+=1
        score.sc.clear()
        score.score_increment(score.sc1,score.sc2)

def ball_touch_racket():
    if (ball.bl.xcor()>340 and ball.bl.xcor()<350) and (ball.bl.ycor() < racket2.racket2.ycor()+40 and ball.bl.ycor() > racket2.racket2.ycor()-40):
        ball.bl.setx(340)
        ball.bl.dx *= -1
    elif (ball.bl.xcor()<-340 and ball.bl.xcor()>-350) and (ball.bl.ycor() < racket1.racket1.ycor()+40 and ball.bl.ycor() > racket1.racket1.ycor()-40):
        ball.bl.setx(-340)
        ball.bl.dx *= -1