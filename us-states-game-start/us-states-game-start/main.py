import turtle
import pandas
from function_game import Game

screen = turtle.Screen()
game = Game()
screen.title("U.S. States Game")
image = "C:/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_25/us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

again = True
while again: 
    game.guess()
    game.remove()
    if game.guess == "Exit":
        again = False
    else:
        game.move()
        game.reduce_country()

screen.exitonclick()