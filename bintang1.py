from turtle import * 
import colorsys
bgcolor("black")
tracer(5)
pensize(3)
h=0.1
for i in range(700):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.0004
    fd(i)
    rt(100)
    rt(120)
hideturtle()
done()