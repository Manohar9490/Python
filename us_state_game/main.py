import turtle
import os
import pandas as pd;

screen = turtle.Screen()

screen.title("U.S States Game")

# image = "./blank_states_img.gif"


# Path to the image
image = "./blank_states_img.gif"

# Check if the file exists
if os.path.isfile(image):
    # print(f"File {image} found.")
    try:
        # Initialize the turtle screen
        screen = turtle.Screen()
        screen.addshape(image)  # Add the shape to the turtle screen
        turtle.shape(image)     # Set the turtle shape to the image
        # print("Image loaded successfully.")
    except turtle.TurtleGraphicsError as e:
        print(f"Error loading image: {e}")
else:
    print(f"File {image} not found.")

states = pd.read_csv("./50_states.csv")
all_stated = states.state.to_list()
states_guessed=[]

# number_state =50
while len(states_guessed) < 50:
  answer = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").capitalize()

  if answer=="Exit":
      break
  
  if answer in all_stated:
      states_guessed.append(answer)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      fState= states[states.state==answer.capitalize()]
      location = (fState["x"].values[0], fState["y"].values[0])
      # print(location)
      t.goto(location)
      t.write(answer)

      


screen.exitonclick()

# turtle.mainloop()


# print("Manohar", "is" , "studying")
