from turtle import Screen
from player import Player
from ball import Ball
from score import Score

myScreen = Screen()#the screen
theBall = Ball()#the ball
theScore = Score()#the score
myScreen.setup(width=600, height=600)#the screen size
myScreen.bgcolor("black")#the background color
myScreen.title("The Ping Pong's Game")#the screen title

myScreen.tracer(0)#cancel the animation

continueGame = True#the variable to continue the game

player1 = Player(250, 0)#create the player 1 at the right
player2 = Player(-250, 0)#create the player 2 at the left

myScreen.listen()#make the screen listen to the keyboard
myScreen.onkey(player1.goUp, "Up")#the player 1 go up when the key "Up" is pressed
myScreen.onkey(player1.goDown, "Down")#the player 1 go down when the key "Down" is pressed
myScreen.onkey(player2.goUp, "z")#the player 2 go up when the key "z" is pressed
myScreen.onkey(player2.goDown, "s")#the player 2 go down when the key "s" is pressed

while continueGame:#the loop to continue the game
    myScreen.update()#update the screen

    theBall.bouncingGame()#make the ball bouncing

    if theBall.distance(player1) < 15 or theBall.distance(player2) < 15:#if the ball touch a player
        theBall.boundPlayer()#make the ball bounce

    if theBall.ycor() > 220 or theBall.ycor() < -220:#if the ball touch the wall
        theBall.boundWall()#make the ball bounce

    if theBall.xcor() > 260:#if the ball touch the right wall
        theScore.incrementY()#increment the score of the player 2
        theScore.display()#display the score
        theBall.refresh()#refresh the ball

    if theBall.xcor() < -260:#if the ball touch the left wall
        theScore.incrementX()#increment the score of the player 1
        theScore.display()#display the score
        theBall.refresh()#refresh the ball

    continueGame = theScore.finish()#check if the game is finish



myScreen.exitonclick()#the screen wait for a click to close
