# coding : uf8
# author : pc
import turtle as t


def nose(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-30)
    t.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.left(3)
            t.forward(a)
        else:
            a = a - 0.08
            t.left(3)
            t.forward(a)
    t.end_fill()

    t.penup()
    t.setheading(90)
    t.forward(25)
    t.setheading(0)
    t.forward(10)
    t.pendown()
    t.pencolor(255, 155, 192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82, 45)
    t.end_fill()

    t.penup()
    t.setheading(0)
    t.forward(20)
    t.pendown()
    t.pencolor(255, 155, 192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82, 45)
    t.end_fill()


def head(x, y):
    t.color((255, 255, 192), "pink")
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.setheading(161)
    t.circle(-300, 15)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.lt(3)
            t.fd(a)
        else:
            a = a - 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()


def ears(x, y):
    t.color((255, 255, 192), "pink")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()

    t.penup()
    t.setheading(90)
    t.forward(-12)
    t.setheading(0)
    t.forward(30)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()


def eyes(x, y):
    t.color((255, 155, 192), "white")
    t.penup()
    t.setheading(90)
    t.forward(-20)
    t.setheading(0)
    t.forward(-95)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.color("black")
    t.penup()
    t.setheading(90)
    t.forward(12)
    t.setheading(0)
    t.forward(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    t.color((255, 155, 192), "white")
    t.penup()
    t.seth(90)
    t.forward(-25)
    t.seth(0)
    t.forward(40)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.color("black")
    t.penup()
    t.setheading(90)
    t.forward(12)
    t.setheading(0)
    t.forward(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()


def cheek(x, y):
    t.color((255, 155, 192))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def mouth(x, y):
    t.color(139, 69, 19)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-80)
    t.circle(30, 40)
    t.circle(40, 80)


def setting():
    t.pensize(4)
    t.hideturtle()
    t.colormode(255)
    t.color((255, 155, 192), "pink")
    t.setup(840, 500)
    t.speed(10)


def main():
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    t.done()


if __name__ == '__main__':
    main()


