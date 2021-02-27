import turtle
import math

s= turtle.getscreen()
t=turtle.Turtle()

def draw_detail(l):
    t.fd(l)
    t.left(90)
    t.fd(l)
    t.left(90)
    t.fd(l)
    t.left(90)
    t.fd(l)
    l2multiplied = ((l**2)+(l**2))
    squarootl = math.sqrt(l2multiplied)
    rad = squarootl/2
    t.left(45)
    t.circle(rad)
    t.left(90)
    t.fd(squarootl)
    t.left(135)
    t.penup()
    t.fd(l)
    t.pendown()
    t.left(135)
    t.fd(squarootl)
    print('diagonals are '+str(squarootl))
    print('radius is ' + str(rad))
l=int(input('Enter length of square'))
draw_detail(l)

input()