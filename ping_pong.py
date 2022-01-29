from turtle import Screen, Turtle
from time import sleep

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1)
        self.penup()
        self.goto(x,y)

    def go_up(self):
        if self.ycor()<300:
            new_y = self.ycor()+80
            self.goto(self.xcor(),new_y)
    
    def go_down(self):
        if self.ycor()>-300:
            new_y = self.ycor()-80
            self.goto(self.xcor(),new_y)


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_mov
        new_y = self.ycor()+self.y_mov
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_mov *= -1
    
    def bounce_x(self):
        self.x_mov *= -1
        

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1

class Scorebaord(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def l_point(self):
        self.l_score+=1
    
    def r_point(self):
        self.r_score+=1
    
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",50,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",50,"normal"))



screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Ping Pong")

screen.tracer(0)

l_Paddle = Paddle(-350,0)
r_Paddle = Paddle(350,0)
ball = Ball()
score = Scorebaord()



screen.listen()
screen.onkey(r_Paddle.go_up,"Up")
screen.onkey(r_Paddle.go_down,"Down")
screen.onkey(l_Paddle.go_up,"w")
screen.onkey(l_Paddle.go_down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    
    sleep(ball.ball_speed)
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if (ball.distance(r_Paddle)<50 and ball.xcor()>320) or (ball.distance(l_Paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()
        ball.ball_speed/=1.5
    if ball.xcor()>400 or ball.xcor()<-400:
        if ball.xcor()>400:
            score.l_point()
        else: score.r_point()
        score.update_score()
        ball.reset_ball()
    
    if score.l_score==5:
        screen.clear()
        score.write("LEFT guy WON!",align='center',font=("Courier",50,"normal"))
    elif score.r_score==5:
        score.clear()
        score.write("RIGHT guy WON!",align='center',font=("Courier",50,"normal"))

screen.exitonclick()


