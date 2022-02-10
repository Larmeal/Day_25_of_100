import re
import turtle
import pandas

class Game:

    def __init__(self):
        self.direction = pandas.read_csv("C:/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022\Day_25/us-states-game-start/us-states-game-start/50_states.csv")
        self.states = self.direction.state
        self.screen = turtle.Screen()
        self.pick = turtle.Turtle()
        self.all_country = []
        self.x_y_position = []
        self.answer_country = []
        self.answer_state = []
        self.int_all_country = 0

    def country(self):
        for state in self.states:
            self.all_country.append(state)

    def position(self):
        x_position = self.direction.x
        y_position = self.direction.y
        for i in range(len(x_position)):
            x = x_position[i]
            y = y_position[i]
            position = (x, y)
            self.x_y_position.append(position)

    def reduce_country(self):
        self.int_all_country += 1

    def guess(self):
        self.country()
        self.answer_state = self.screen.textinput(title=f"{self.int_all_country}/50 State Correct", prompt="What's another state's name?").title()
        if self.answer_state == "Exit":   
            data = pandas.DataFrame(self.all_country)
            data.to_csv("All_state_you_should_to_learn.csv")


    def check_position(self):
        self.country()
        self.position()
        country_position = self.all_country.index(self.answer_state)
        self.show_position_country = self.x_y_position[country_position]

    def move(self):
        self.check_position()
        self.pick.hideturtle()
        self.pick.penup()
        self.pick.goto(self.show_position_country)
        self.pick.write(f"{self.answer_state}", font=("Courier", 8, "normal"))
    
    def remove(self):
        self.country()
        self.answer_country.append(self.answer_state)
        for n in self.answer_country:
            self.all_country.remove(n)
