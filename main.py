import turtle

window=turtle.Screen()
window.title("Turtle Graphics Example")
window.bgcolor("black")


#creating turtle
t = turtle.Turtle()
t.color("green")
t.speed(0)         # fastest
t.left(90)         # point upward
t.penup()
t.goto(0, -250)    # start from bottom center
t.pendown()


def draw_tree(branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)
    t.right(30)
    draw_tree(branch_length * 0.7, level - 1)
    t.left(60)
    draw_tree(branch_length * 0.7, level - 1)
    t.right(30)
    t.backward(branch_length)

x=int(input("Enter the number of levels for the tree (e.g., 4): "))

# Draw tree
draw_tree(100, x)


# Hide the turtle and finish
t.hideturtle()
window.mainloop()