import turtle

t = turtle.Pen()

t.width(2)

t.speed(10)

for x in range(16):
    t.penup()
    t.goto(-300,300-40*x)
    t.pendown()
    t.goto(300,300-40*x)
    t.penup()
    t.goto(-300+40*x,300)
    t.pendown()
    t.goto(-300+40*x,-300)




turtle.done()
