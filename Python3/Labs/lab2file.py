#упражнение 2
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.width(6)
t.speed(7)

(t.up(), t.goto(-200,0), t.down())
(t.lt(45),t.fd(20),t.rt(135),t.fd(50),t.back(50),t.lt(90)) #1
(t.up(), t.fd(20),t.down())
(t.rt(90),t.fd(20),t.lt(90),t.fd(20),t.lt(90),t.fd(20),t.rt(180),t.fd(50),t.back(50), t.lt(90),t.rt(45))  #4
(t.up(), t.fd(20),t.down())
(t.lt(90),t.fd(20),t.rt(135),t.fd(50),t.back(50),t.lt(90))  #1
(t.up(), t.fd(20),t.down())
(t.fd(25), t.rt(135), t.fd(28), t.lt(45), t.fd(29), t.back(29), t.lt(135), t.fd(28), t.rt(45)) #7
(t.up(), t.fd(15),t.down())
(t.fd(20), t.rt(90), t.fd(50), t.rt(90), t.fd(20), t.rt(90), t.fd(50), t.rt(90), t.fd(20)) #0
(t.up(), t.fd(15),t.down())
(t.fd(20), t.rt(90), t.fd(50), t.rt(90), t.fd(20), t.rt(90), t.fd(50), t.rt(90), t.fd(20)) #0
t.hideturtle()