import turtle

colors = ["red","blue","purple","green","yellow","orange"]

turtle.bgcolor("black")

s = turtle.Pen()

i = 0
while True:
    for j in range(len(colors)):
        s.width(i / 100 + 1)
        s.pencolor(colors[j])
        s.forward(i)
        s.left(59)
        i+=1