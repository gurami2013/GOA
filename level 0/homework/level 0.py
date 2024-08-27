width(7)
color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
# draw a door
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
#draw a roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
left(30)
end_fill()

# draw a window 1
color("brown")
begin_fill()
penup()
goto(15,135)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



# draw a window  2
color("brown")
begin_fill()
penup()
left(90)
forward(120)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()










end_fill()




exitonclick()
