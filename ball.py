from turtle import Turtle


class Ball(Turtle):#the class Ball
    def __init__(self):#the constructor
        super().__init__()#make the class Ball a subclass of the class Turtle,
        self.shape("circle")#the shape of the ball
        self.shapesize(0.5, 0.5)#the size of the ball
        self.color("blue")#the color of the ball
        self.newPosX = 0.08#the speed of the ball in the x axis
        self.newPosY = 0.08#the speed of the ball in the y axis
        self.uple = (0, 0)#set the position of the ball


    def bouncingGame(self):
        self.penup()#the penup method is used to make the ball not draw a line when it moves
        self.goto(self.uple)#set the position of the ball
        newPosx = self.xcor() + self.newPosX#the new position of the ball in the x axis
        newPosy = self.ycor() + self.newPosY#the new position of the ball in the y axis
        self.uple = (newPosx, newPosy)#set the new position of the ball
        self.goto(self.uple)#make the ball go on the position that we set


    def boundWall(self):#the boundWall method is used to make the ball bounce on the wall
        self.newPosY *= -1


    def boundPlayer(self):#the boundPlayer method is used to make the ball bounce on the player
        self.newPosX *= -1

    def refresh(self):#the refresh method is used to refresh the position of the ball
        self.uple = (0, 0)#set the position of the ball
        self.bouncingGame()#call the function bouncingGame to make the ball go on the position that we set
        self.newPosX *= -1#make the ball go in the opposite direction
