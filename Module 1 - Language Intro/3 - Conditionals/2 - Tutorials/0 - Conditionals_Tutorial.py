# In this file we are going to walk through setting up
# some conditional statements.

# Here is the first variable we are going to use:
age = 19

# First, let's write a function that prints out if
# a person's age is over 18. Also, have an else statement
# if they are not over 18.

if age > 18:
    print("This person is over 18")
else:
    print("This person is not over 18")

# Next, choose a value to make the following statement print out
# the 2nd elif statement! You can also mess around to see how other
# values print different outcomes!

temperature = 90

if temperature <= 32:
    print("It's Freezing! Brrrrr")
elif 32 < temperature <= 60:
    print("It's a bit brisk out. Bring a jacket!")
elif 60 < temperature <= 80:
    print("It's pretty comfy out!")
else:
    print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")

# Lastly, let's do a nested if statement! That means an if statement
# within an if statement!

# Here is our variable to check
weight = 190

# First, write an if statement to check if the weight is over 150:
if weight > 150:
    print("Weight is over 150!")
    # Now in here, write an if statement to check if it's below 180:
    if weight < 180:
        print("Weight is also under 180!")
    else:
        print("Weight is also over 180!")


# Now go back and change weight to be over 180, see what changes in the print out!
