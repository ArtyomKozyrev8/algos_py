import turtle


def tree(branch_len: int, t: turtle.Turtle) -> None:
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


if __name__ == '__main__':
    _t = turtle.Turtle()
    my_win = turtle.Screen()
    _t.left(90)
    _t.up()
    _t.backward(100)
    _t.down()
    _t.color("green")
    tree(75, _t)
    my_win.exitonclick()