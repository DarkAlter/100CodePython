import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "black.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
listAnswer = []
notAsnwerd = []
allState = data.state.to_list()
score = 0

while len(listAnswer) < 50:
    answerState = screen.textinput(title=f"{len(listAnswer)}/{len(allState)} answer are Corect", prompt="Whats another states name?")
    '''
    '''
    if answerState == "Exit":
        '''for states in allState:
            if states not in listAnswer:
                notAsnwerd.append(states)'''
        dataBreak = [state for state in allState if state not in listAnswer]
        frame = pandas.DataFrame(dataBreak)
        frame.to_csv("test.csv")
        break

    if answerState in allState:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answerState]
        listAnswer.append(answerState)
        t.goto(int(state.x), int(state.y))
        t.write(answerState)


