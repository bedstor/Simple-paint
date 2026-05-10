from turtle import *
from interface_paint import *


def main():
    t = Turtle()
    t.shape('circle')
    t.color('darkblue')
    t.pensize(5)

    def draw(x,y):
        t.goto(x,y)

    t.ondrag(draw)

    screen = t.getscreen()
    screen.listen()

    def move(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()

    screen.onscreenclick(move)
    def move_right():
        t.goto(t.xcor() + 5,t.ycor())

    def move_left():
        t.goto(t.xcor() - 5,t.ycor())

    def move_up():
        t.goto(t.xcor(),t.ycor() + 5)

    def move_down():
        t.goto(t.xcor(),t.ycor() - 5)

    screen.onkey(move_right, 'Right')
    screen.onkey(move_left, 'Left')
    screen.onkey(move_down, 'Down')
    screen.onkey(move_up, 'Up')

    def draw_green():
        t.color('green')

    def draw_red():
        t.color('red')

    def draw_blue():
        t.color('blue')

    def draw_yellow():
        t.color('yellow')

    def draw_orange():
        t.color('orange')

    def draw_lightblue():
        t.color('light blue')

    def draw_pink():
        t.color('pink')

    def draw_purple():
        t.color('purple')

    screen.onkey(draw_blue, 'c')
    screen.onkey(draw_green, 'p')
    screen.onkey(draw_red, 'r')
    screen.onkey(draw_yellow, ';')
    screen.onkey(draw_orange, 'j')
    screen.onkey(draw_lightblue, 'u')
    screen.onkey(draw_pink, 'h')
    screen.onkey(draw_purple, 'a')

    def size_1():
        t.pensize(5)

    def size_2():
        t.pensize(10)

    def size_3():
        t.pensize(15)

    def size_4():
        t.pensize(20)

    screen.onkey(size_1, '1')
    screen.onkey(size_2, '2')
    screen.onkey(size_3, '3')
    screen.onkey(size_4, '4')

    def bg_white():
        screen.bgcolor('white')

    def bg_black():
        screen.bgcolor('black')

    def bg_blue():
        screen.bgcolor('dark blue')

    def bg_green():
        screen.bgcolor('green')

    screen.onkey(bg_black, 'b')
    screen.onkey(bg_white, 'w')
    screen.onkey(bg_blue, 'd')
    screen.onkey(bg_green, 'g')

    def begin_fil():
        t.begin_fill()

    def end_fil():
        t.end_fill()

    screen.onkey(begin_fil, 'z')
    screen.onkey(end_fil, 'x')
    


if __name__ == '__main__':
    main()