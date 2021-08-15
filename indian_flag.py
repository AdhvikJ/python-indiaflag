import turtle

# Function to draw a Rectangle with given color


def rectangle(color):

    myflag.begin_fill()
    myflag.fillcolor(color)

    for i in range(2):
        myflag.forward(300)
        myflag.right(90)
        myflag.forward(70)
        myflag.right(90)
    myflag.end_fill()


# Initiate Turtle
myflag = turtle.Turtle()
myflag.width(3)
myflag.up()
myflag.goto(0, -300)
myflag.down()
myflag.goto(0, 300)
rectangle('orange')
myflag.goto(0, 230)
rectangle('white')
myflag.forward(150)

# To Draw Circle with blue color and 35 as radius
myflag.color("blue")
myflag.circle(-35)


# To Change direction to move the Turtle to center of the screen
myflag.setheading(270)
myflag.forward(35)
myflag.setheading(0)

# Loop to draw 24 Ashoka Chakra Spikes
for i in range(24):
    myflag.forward(35)
    myflag.bk(35)
    myflag.left(15)

myflag.setheading(90)
myflag.forward(30)
myflag.setheading(0)
myflag.up()
myflag.goto(0, 160)
myflag.down()
myflag.color('black')
rectangle('green')

# create flag stand
myflag.up()
myflag.goto(-120, -250)
myflag.down()
rectangle("dark grey")
myflag.up()
myflag.goto(-70, -200)
myflag.down()
myflag.begin_fill()
myflag.fillcolor('light grey')
for i in range(2):
    myflag.forward(200)
    myflag.right(90)
    myflag.forward(50)
    myflag.right(90)

myflag.end_fill()
input()
