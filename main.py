import turtle
hi = turtle.Turtle()
hi.speed(15)
hi.color("teal")
value = 180
for i in range(10):
  hi.forward(value)
  hi.right(144)
  # value += 5
hi.penup()
hi.forward(value / 2)
hi.right(90)
hi.forward(55)
hi.right(135)
hi.pendown()
hi.color('red')
hi.forward(45)
hi.setheading(90)
hi.circle(-15, 180)
hi.setheading(90)
hi.circle(-15, 180)
hi.setheading(225)
hi.forward(45)



turtle.done()