# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 25 - Intermediate - Working with CSV Data and the Pandas Library
# Project - States Guessing Game
# Day 16 - challenge - replaces several lines of code with a list comprehension method on 2024-11-20

import pandas
import turtle

# Constants definition
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')

states_data = pandas.read_csv("50_states.csv")
# print(states_data) # testing
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
keep_playing = True
correct_states = []

while keep_playing:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        # Create a .scv file with all the states that have not been guessed
        states_list = states_data.state.to_list()
        # new_list = [new_item for item in list if test]
        missing_states = [state for state in states_list if state not in correct_states] # List comprehension - added on 2024-11-20, day 26 challenge
        ## Below code block was replaced by above line on 2024-11-20
        # missing_states = []
        # for state in states_list:
        #     if state not in correct_states:
        #         missing_states.append(state)

        # Convert states_not_guessed list to Pandas data frame and save it as CSV file
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states.csv", index=False)
        # print(states_not_guessed) # testing
        break

    # If correct state was entered row with state, x and y info will be saved, otherwise the DataFrame will be empty
    answer_result = states_data[states_data["state"] == answer_state]
    # print(answer_result)  # testing

    if not answer_result.empty:
        # print(f"{answer_state} was entered, which is one of the states.") # testing
        # Code for placing name of the state on the map
        # answer_result = states_data[states_data["state"] == "California"] # used for testing purposes
        x_coord = answer_result["x"].tolist()[0] # get x coordinate an integer, "answer_result.x.item()" is an alternative
        y_coord = answer_result["y"].tolist()[0] # get x coordinate an integer, "answer_result.y.item()" is an alternative
        state_name = answer_result["state"].tolist()[0] # get state name as a string
        State = turtle.Turtle()
        State.speed("fastest")
        State.penup()
        State.goto(x=x_coord, y=y_coord)
        State.color("black")
        State.hideturtle()
        State.write(f"{state_name}", False, align=ALIGNMENT, font=FONT)

        # Check if state was already entered, if not increase score by one and add the state to correct_states list

        if answer_state not in correct_states:
            score += 1
            correct_states.append(answer_state)
            print(score)
            print(correct_states)
            # End game if all states are entered
            if score == 50:
                break

    ## testing
    # else:
    #     print(f"{answer_state} was entered, which not one of the states.")




# screen.exitonclick() # not needed since code is terminate with "break" in the while loop
