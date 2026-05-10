from turtle import *

t_i = Turtle()
t_i.speed(0)

def draw_symbol(symbol):
    t_i.pendown()
    t_i.color('black')
    t_i.write(symbol, font=('Arial', 10, 'normal'))
    t_i.penup()

def draw_line(width):
    t_i.pendown()
    t_i.color('gray')
    t_i.pensize(width)
    t_i.forward(10)
    t_i.penup()

def draw_colors(color):
    t_i.pendown()
    t_i.color(color)
    t_i.begin_fill()
    t_i.circle(5)
    t_i.end_fill()
    t_i.penup()

def draw_backdrop(color):
    t_i.pensize(2)
    t_i.pendown()
    t_i.color('gray', color)
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(20)
        t_i.left(90)
    t_i.end_fill()
    t_i.penup()

t_i.penup()
t_i.goto(50,300)
draw_line(5)
t_i.goto(100,300)
draw_line(10)
t_i.goto(150,300)
draw_line(15)
t_i.goto(200,300)
draw_line(20)

t_i.goto(-200, 300)
draw_colors('red')
t_i.goto(-150, 300)
draw_colors('orange')
t_i.goto(-100, 300)
draw_colors('yellow')
t_i.goto(-50, 300)
draw_colors('green')

t_i.goto(-200, 240)
draw_colors('lightblue')
t_i.goto(-150, 240)
draw_colors('blue')
t_i.goto(-100, 240)
draw_colors('pink')
t_i.goto(-50, 240)
draw_colors('purple')



t_i.goto(50,240)
draw_backdrop('black')
t_i.goto(100,240)
draw_backdrop('white')
t_i.goto(150,240)
draw_backdrop('blue')
t_i.goto(200,240)
draw_backdrop('green')


t_i.goto(50,280)
draw_symbol('1')
t_i.goto(100,280)
draw_symbol('2')
t_i.goto(150,275)
draw_symbol('3')
t_i.goto(200,275)
draw_symbol('4')

t_i.goto(-205,275)
draw_symbol('К')
t_i.goto(-155,275)
draw_symbol('О')
t_i.goto(-105,275)
draw_symbol('Ж')
t_i.goto(-55,275)
draw_symbol('З')

t_i.goto(-205,215)
draw_symbol('Г')
t_i.goto(-155,215)
draw_symbol('С')
t_i.goto(-105,215)
draw_symbol('Р')
t_i.goto(-55,215)
draw_symbol('Ф')

t_i.goto(50,215)
draw_symbol('B')
t_i.goto(100,215)
draw_symbol('W')
t_i.goto(150,215)
draw_symbol('D')
t_i.goto(200,215)
draw_symbol('G')
