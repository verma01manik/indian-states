import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian states game ")
image = "Map_good.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 guessed correct" , prompt= "what is another state name").title()
    print(answer_state)


    if answer_state == "Exit":
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        guessed_state.append(answer_state)
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)







