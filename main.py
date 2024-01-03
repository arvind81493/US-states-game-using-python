# with open("weather_data (1).csv") as datafile:
#     data=datafile.readlines()
#
#
# import csv
#
# with open("weather_data (1).csv") as datafile:
#     data =csv.reader(datafile)
#
#     tempreature=[]
#     for row in data:
#         if(row[1]!="temp"):
#             tempreature.append(row[1])
#     print(tempreature)

#
# import pandas
# data=pandas.read_csv("weather_data (1).csv")
# print(data)
# print(data.to_dict())
# print(data["temp"].to_list())
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data.condition)
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])
# moday=data[data.day=="Monday"]
# print(moday.condition)
# temp_mon_in_f=moday.temp*9/5+32
# print(temp_mon_in_f)
#
# data_dict={
#     "students": ["Amy","James","Angela"],
#     "Scores":[76,56,65]
# }
#
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

# import pandas
# data=pandas.read_csv("central_park.csv")
# grey_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
# red_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
# data_dict={"Fur Color": ["Gray","cinnamon","Black"],
# "Count":[grey_squirrels,red_squirrels,0]}
#
# df=pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
# print(df)

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
