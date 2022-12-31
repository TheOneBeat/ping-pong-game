from turtle import Turtle#the turtle module


class Player(Turtle):#the class Player
    def __init__(self, posX, posY):#the constructor
        super().__init__()#make the class Player a subclass of the class Turtle,
        #basically it means that the class Player will herit from the class Turtle
        self.shape("square")#the shape of the player
        self.color("white")#the color of the player
        self.shapesize(0.5, 2)#the size of the player
        self.penup()#the penup method is used to make the player not draw a line when it moves
        self.setheading(270)#the setheading method is used to make the player face the right direction
        self.setpos(posX, posY)#set the position of the player

    def goUp(self):#the goUp method is used to make the player go up
        if self.ycor() > 200:#if the player is at the top of the screen
            pass#do nothing
        else:#if the player is not at the top of the screen
            self.bk(20)#make the player go backward of a certain distance (20)

    def goDown(self):#the goDown method is used to make the player go down
        if self.ycor() < -200:#if the player is at the bottom of the screen
            pass#do nothing
        else:#if the player is not at the bottom of the screen
            self.fd(20)#make the player go forward of a certain distance (20)