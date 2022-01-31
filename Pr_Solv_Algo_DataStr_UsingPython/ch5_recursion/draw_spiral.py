import turtle


def draw_spiral(t: turtle.Turtle, s: int) -> None:
    if s > 5:
        t.forward(s)
        t.right(90)
        draw_spiral(t, s-5)


if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()