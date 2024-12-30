from turtle import Turtle, Screen
import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
colours = ["red", "green", "blue", "yellow", "orange", "violet", "purple"]
user_choice = screen.textinput(title="Make your bet",
                               prompt=f"Which colored turtle will win the race?\n{colours}")

y_axis = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[i])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_colour = turtle.pencolor()
                if winning_colour == user_choice:
                    messagebox.showinfo("Winner!", f"You've won! The {
                                        winning_colour} turtle is the winner")

                else:
                    messagebox.showinfo("Winner!", f"You've won! The {
                                        winning_colour} turtle is the winner")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
