import turtle
import random
s= turtle.getscreen()
p1 = turtle
p2= p1.clone()

p1.penup()
p2.penup()
p1.goto(-200,200)
p2.goto(-200,-200)
p1.pendown()
p2.pendown()
p1.shape('turtle')
p1.fillcolor('red')
p1.pencolor('blue')
p2.shape('turtle')
p2.fillcolor('green')
p2.pencolor('purple')
dice=[1,2,3,4,5,6]
while 1:
    p1.fd((random.choice(dice)*10))
    p2.fd((random.choice(dice) * 10))

    if p1.xcor()>=200 or p2.xcor()>=200:
        print('p1xcor is ' + str(p1.xcor()))
        print('p2xcor is ' + str(p2.xcor()))
        break
input()