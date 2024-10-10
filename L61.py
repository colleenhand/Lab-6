#The author's name is Colleen
def mood_star(mood):
    import turtle
    if mood == "happy":
        riley = turtle.Turtle()
        riley.width(5)
        riley.speed(0)
        for side in range(5):
            riley.forward(100)
            riley.right(144)
            riley.color("pink")
    elif mood == "sad":
        riley = turtle.Turtle()
        riley.width(5)
        riley.speed(0)
        for side in range(5):
            riley.forward(100)
            riley.right(144)
            riley.color("blue")
    elif mood == "sleepy":
        riley = turtle.Turtle()
        riley.width(5)
        riley.speed(0)
        for side in range(5):
            riley.forward(100)
            riley.right(144)
            riley.color("green")
    elif mood == "angry":
        riley = turtle.Turtle()
        riley.width(5)
        riley.speed(0)
        for side in range(5):
            riley.forward(100)
            riley.right(144)
            riley.color("red")

mood_star("happy")
mood_star("sad")
mood_star("sleepy")
mood_star("angry")
