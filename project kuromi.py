import turtle
wn = turtle.Screen()
wn.bgcolor('#ba73c1')
head = turtle.Turtle()
head.hideturtle()
head.speed(20)
def oval(rad):
    for loop in range(2):
       head.circle(rad, 90)
       head.circle(rad/2,90)
       
head.penup()
head.goto(-200, 0)  #x.y coordinates
head.pendown()

head.seth(-45)
head.begin_fill()
head.fillcolor('#292329')
oval(200) #radius length
head.end_fill()

face = turtle.Turtle()
face.hideturtle()
face.speed(20)
def oval2(rad):
    for detz in range(2):
       face.circle(rad, 90)
       face.circle(rad/2,90)

nose = turtle.Turtle()
nose.hideturtle()
nose.speed(20)
def oval3(rad):
    for detz in range(2):
       nose.circle(rad, 90)
       nose.circle(rad/2,90)
     
face.penup()
face.goto(-150, -14)  
face.pendown()

face.seth(-45)
face.begin_fill()
face.fillcolor('white')
oval2(140) 
face.end_fill()

nose.penup()
nose.goto(-65, 25)  
nose.pendown()

nose.seth(-45)
nose.begin_fill()
nose.fillcolor('#bb63b1')
oval3(15) 
nose.end_fill()

mouth = turtle.Turtle()
mouth.hideturtle()
mouth.speed(20)
mouth.color('black')
mouth.pensize(4)
mouth.seth(-75)
mouth.penup()
mouth.goto(-70, 10)
mouth.pendown()
mouth.circle(15, 150)


def face_det(x,y,size):
    tri = turtle.Turtle() 
    tri.penup()
    tri.goto(x,y)
    tri.pendown()
    tri.hideturtle()
    tri.speed(20)

    tri.fillcolor('#292329')
    tri.begin_fill()

    tri.right(20)
    tri.forward(size)
    tri.left(50)
    tri.forward(size)

    tri.end_fill()
face_det(-117, 125, 70)

def ear(x,y,h):
    shape = turtle.Turtle()
    
    shape.penup()
    shape.goto(x,y)
    shape.pendown()
    shape.hideturtle()
    shape.speed(20)
    shape.seth(h)

    shape.fillcolor('#292329')
    shape.begin_fill()

    shape.left(20)
    shape.forward(25)
    shape.left(60)
    shape.forward(150)
    
    shape.left(120)
    shape.forward(150)
    shape.left(60)
    shape.forward(25)

    shape.end_fill()

positions = [(80, 125, 5), (-95, 195, 75)]

for pos in positions:
    ear(*pos)

def ear_det(x,y,h):
    bud = turtle.Turtle()
    
    bud.penup()
    bud.goto(x,y)
    bud.pendown()
    bud.hideturtle()
    bud.speed(20)
    bud.seth(h)

    bud.fillcolor('#292329')
    bud.begin_fill()
    bud.circle(15)
    bud.end_fill()

positions = [(120, 280, 6), (-220, 290, 90)]

for pos in positions:
    ear_det(*pos)

def eyes(x,y,h,i):
    eye = turtle.Turtle()
    
    eye.penup()
    eye.goto(x,y)
    eye.pendown()
    eye.hideturtle()
    eye.speed(20)
    eye.seth(h)

    eye.fillcolor('black')
    eye.begin_fill()
    eye.circle(22, i)
    eye.end_fill()

positions = [(-5, 70, -75, 200), (-100, 70, 75, -200)]

for pos in positions:
    eyes(*pos)

skull = turtle.Turtle()
skull.speed(20)
def design(x,y):
    skull.penup()
    skull.goto(x, y)
    skull.pendown()
    skull.seth(-45)
    skull.begin_fill()
    for detz in range(2):
       skull.circle(30, 90)
       skull.circle(30/2,90)   
    skull.fillcolor('#bb63b1')
    skull.end_fill()
    skull.right(45)
    skull.color('#bb63b1')
    skull.pensize(5)
    for teeth in range(3):
        skull.penup()
        skull.goto(x+32-(10*teeth),y)
        skull.pendown()
        skull.forward(10)
    for eyes in range(2):
        skull_eyes = turtle.Turtle()
        skull_eyes.speed(20)
        skull_eyes.begin_fill()
        skull_eyes.fillcolor('white')
        skull_eyes.penup()
        skull_eyes.goto(x+35-(20*eyes),y+5)
        skull_eyes.pendown()
        skull_eyes.hideturtle()
        skull_eyes.seth(45)
        for i in range(2):
            skull_eyes.circle(10,90)
            skull_eyes.circle(10/2, 90)
        skull_eyes.end_fill()
design(-80, 130)

turtle.hideturtle()
turtle.penup()
turtle.goto(-160,-200)
turtle.pendown()
turtle.write("Kuromi<33", font = ("Gabriola", 40, 'normal'))

wn.exitonclick()