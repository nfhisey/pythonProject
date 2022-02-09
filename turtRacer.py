import time
import turtle
from turtle import Turtle
from random import randint

# WINDOW SETUP
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("#d5dcdc")
turtle.color("#48474b")
turtle.speed(10)
turtle.penup()
turtle.setpos(-275, 200)
turtle.write("TURTLE RACER", font=("Arial", 70, "bold"))
turtle.penup()

# BOTTOM
turtle.setpos (-400, -180)
turtle.color("#fefff4")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

# FINISH LINE
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

# TURTLE 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

# TURTLE 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("#d46151")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# TURTLE 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("#737d5a")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# TURTLE 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("#94adc5")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

time.sleep(1) # Pause the game for 1 seconds

# MOVE TURTLES
for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1, 5))
    turtle3.forward(randint(1, 5))
    turtle4.forward(randint(1, 5))

# DECIDE RANKING
finals_list = [turtle1.xcor(), turtle2.xcor(), turtle3.xcor(), turtle4.xcor()]
finals_dict = {
    turtle1.xcor(): "black",
    turtle2.xcor(): "red",
    turtle3.xcor(): "green",
    turtle4.xcor(): "blue"
}

finals_list = sorted(finals_list, reverse=True)

# RANKING BOARD
turtle.up()
turtle.color("black")
turtle.setposition(-70, -210)
turtle.write("Ranking Board", align="left", font=(None, 20, "bold"))

# FIRST PLACE
turtle.setposition(-70, -230)
rank=finals_list[0]
turtle.write("1st place: " + finals_dict[rank], align="left", font=(None, 20))

# SECOND PLACE
turtle.setposition(-70, -250)
rank=finals_list[1]
turtle.write("2nd place: " + finals_dict[rank], align="left", font=("None", 20))

# THIRD PLACE
turtle.setposition(-70, -270)
rank=finals_list[2]
turtle.write("3rd place: " + finals_dict[rank], align="left", font=("None", 20))

# FOURTH PLACE
turtle.setposition(-70, -290)
rank=finals_list[3]
turtle.write("4th place: " + finals_dict[rank], align="left", font=("None", 20))




turtle.exitonclick()