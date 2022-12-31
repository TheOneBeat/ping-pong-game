from turtle import Turtle


class Score(Turtle):#the class Score
    def __init__(self):#the constructor
        super().__init__()#make the class Score a subclass of the class Turtle,
        self.ht()#hide the turtle
        self.penup()#the penup method is used to make the player not draw a line when it moves
        self.setpos(0, 230)#set the position of the player
        self.countY = 0#the score of the player Y
        self.countX = 0#the score of the player X
        self.color('Orange')#the color of the score

        self.display()#call the function display to display the score



    def incrementX(self):#the incrementX method is used to increment the score of the player X
        self.countX += 1


    def incrementY(self):#the incrementY method is used to increment the score of the player Y
        self.countY += 1


    def display(self):#the display method is used to display the score
        self.clear()
        self.write(f"  Y : {self.countY} | X : {self.countX}", False, align="center", font=('Arial', 18, 'normal'))


    def finish(self):#the finish method is used to display the winner
        if self.countX == 3:#if the score of the player X is equal to 3
            self.end("X")#call the function end to display the winner
            return False

        if self.countY == 3:#if the score of the player Y is equal to 3
            self.end("Y")#call the function end to display the winner
            return False
        return True


    def end(self,n):#the end method is used to display the winner
        tim = Turtle()#create a new turtle
        tim.color("red")#set the color of the turtle
        tim.penup()#the penup method is used to make the player not draw a line when it moves
        tim.write(f"le joueur {n} a gagné", False, align="center", font=('Arial', 25, 'normal'))
        #write the winner




