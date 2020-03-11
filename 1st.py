import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#wn.tracer(0)

#Paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    if  y < 250:
        y+= 10
        paddle_a.sety(y)

def paddle_a_dwn():
    y = paddle_a.ycor()
    if y > -250 :
        y-= 10
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if  y < 250:
        y+= 10
        paddle_b.sety(y)

def paddle_b_dwn():
    y = paddle_b.ycor()
    if y > -250 :
        y-= 10
        paddle_b.sety(y)

#keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_dwn, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_dwn, "Down")

#main game
while True:
    wn.update()


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
    
    #paddle nd ball

    if  ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50) :
        ball.dx *= -1
    
    if  ball.xcor() > -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() + 50) :
        ball.dx *= -1