import turtle
import random

FONT_SIZE = 30

turtle.colormode(255)

FONT = ("Arial", "25", "bold")

numbers = int(input("pick a number"))

def factors(x):
    print("the factors of ", x, "are;")
    turtle.begin_fill()
    for i in range(1, x + 1):
        if x % i == 0:
            turtle.pendown()
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            turtle.color((r, g, b))



            turtle.fillcolor()
            turtle.begin_fill()
            turtle.circle(i * 5)
            turtle.end_fill()

            turtle.left(90)
            # lift the pen so no line is drawn
            turtle.penup()
            turtle.forward(i * 5)
            # put pen down now (if you need to)
            turtle.pendown()
            turtle.write(i, True, align="center")
            turtle.penup()

            turtle.forward(i * 5)
            turtle.end_fill()

factors(numbers)
turtle.mainloop()
