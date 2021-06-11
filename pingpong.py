#I have created a 2D ping-pong game in my python project
#I used turtle to insert graphics in my game

import turtle

wn = turtle.Screen() #used to insert a screen
wn.title("PING PONG") #used to give title to the screen
wn.setup(width=800,height=600) #gives size to the screen
wn.bgcolor("black") #to set background colour
wn.tracer(0) #used for animation
# score
#Defined variables to store score of players
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() #create an object in turtle
paddle_a.speed(0)  #sets the animation speed
paddle_a.shape("square") #gives shape to the object
paddle_a.color("white") #gives colour to the object
paddle_a.shapesize(stretch_len=1,stretch_wid=4) #defines size of the object
paddle_a.penup() #avoid tracing of the ibject
paddle_a.goto(-350,0) #sets the position of the object

# Paddle B
#Similar steps for inserting paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=4)
paddle_b.penup()
paddle_b.goto(350,0) # this object lies on the positive x-axis

# Ball
ball = turtle.Turtle() #creating ball object in turtle
ball.speed(0) #stes the animation speed of ball
ball.shape("circle") 
ball.color("white")
ball.penup() #avoid tracing of ball
ball.goto(0,0) #sets the positon of ball
ball.dx = 0.2 #sets the speed as well as direction of ball
ball.dy = -0.2 #sets the speed as well as direction of ball

# score
 
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle() 
score.goto(0,260)
score.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal")) 


# Function
#defines paddle up movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y +=20 #on every click paddle_a moves by 20 in upward direction
        paddle_a.sety(y)
    else :
        y +=0 #no movement
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:    
        y -=20 #on every click paddle_a moves by 20 in downward direction
        paddle_a.sety(y)
    else :
        y +=0 #no movement
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:    
        y +=20 #on every click paddle_b moves by 20 in upward direction
        paddle_b.sety(y)
    else :
        y +=0 #no movement
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -=20  #on every click paddle_b moves by 20 in downward direction
        paddle_b.sety(y)
    else :
        y +=0 #no movement
        paddle_b.sety(y)

# Keyboard binding
wn.listen() #used to make system understand keyboard input
wn.onkeypress(paddle_a_up, "w") #on pressing "W" key paddle will go up

wn.listen()
wn.onkeypress(paddle_a_down, "s") #on pressing "S" key paddle will go up

wn.listen()
wn.onkeypress(paddle_b_up, "Up") #on pressing "UP ARROW" key paddle will go up

wn.listen()
wn.onkeypress(paddle_b_down, "Down") #on pressing "DOWN ARROW" key paddle will go up

#Main game loop
while True:
    wn.update() #updates the game and sets the score to zero

    #sets the movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: #if ball hits the top
        ball.sety(290)  #sets the turtle second co-ordinate to y
        ball.dy *= -1  #reverse the direction of ball

    if ball.ycor() < -290: #if ball hits the floor
        ball.sety(-290) #sets the turtle second co-ordinate to y
        ball.dy *= -1 #reverse the direction of ball

    if ball.xcor() > 390: #ball crosses the positive x-axis
        ball.goto(0,0) #gets ball back to its position
        ball.dx *= -1 #after the ball gets back to its original position it moves in reverse direction
        score_a +=1 #updates score
        score.clear() #deletes the initial score
        score.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal")) #displays the updated score 
        

    if ball.xcor() < -390:  #ball crosses the negative x-axis
        ball.goto(0,0) #gets ball back to its position
        ball.dx *= -1  #after the ball gets back to its original position it moves in reverse direction
        score_b +=1  #updates score
        score.clear() #deletes the initial score
        score.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal")) #displays the updated score
        

#when ball hits the paddle
    #it checks for the condition if the ball ocupies the right paddle surface area
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        #in above condition if the ball touches the paddle then it reverse its direction otherwise it continues
        ball.setx(340) #set the turtke first co-ordinate to x
        ball.dx *=-1 #reverse the direction

    #it checks for the condition if the ball ocupies the left paddle surface area
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        #in above condition if the ball touches the paddle then it reverse its direction otherwise it continues
        ball.setx(-340)  #set the turtke first co-ordinate to x
        ball.dx *=-1 #reverse the direction

        #THANK YOU....!

