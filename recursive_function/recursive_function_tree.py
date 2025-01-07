'''
Program that draws a recursive tree using Turtle Graphics.
Author: Darren Swann, Brayden Brown
Last Update: 07/01/2025

'''

# Modules imported for the game
import turtle 

# Main Menu code
def main_menu():
    print("\n***** Welcome to the grow a tree game! *****\n")
    print(
        "In this game, you'll create your very own unique tree using Python's Turtle Graphics. "
        "Customise by selecting the tree branch lengths, angles and recursion depth to " 
        "determine how to detail intricate your tree will be. \nYou can experiment with different settting " 
        "to see how your tree grows. We have set some minimum perimeters so things don't go haywire!\n"
        "\n***** Have fun and be creative! *****\n"
          )

# This function handles the user tree input logic
def the_tree_inputs():
    while True:
        try:
            trunk_length = int(input("Please enter a number (between 50-200) for the length of your tree trunk: "))
            if  50 <= trunk_length <= 200:
                break
            else:
                print("Oops! This tree trunk is too big or too small! For a strong tree, please enter a number between 50 and 200 for your tree trunk")
        except ValueError:
            print("Oops, invalid input. Please try again!")
    
    while True:
        try:
            branch_angle_left = int(input("Please enter a number between (15-75) for your left branch angle: "))
            if 15 <= branch_angle_left <= 75:
                break
            else:    
                print("Oops! This amount of degrees to too much! Please enter a number between 15 and 75")
        except ValueError:
            print("Oops, invalid input. Please try again!")

    while True:
        try:
            branch_angle_right = int(input("Please enter a number between (15-75) for your right branch angle: "))
            if 15 <= branch_angle_right <= 75:
                break
            else:    
                print("Oops! This amount of degrees to too much! Please enter a number between 15 and 75")
        except ValueError:
            print("Oops, invalid input. Please try again!")

    while True:
        try:
            branch_reduction = int(input("Please enter a number between (40-90) for your branch reduction: "))
            if 40 <= branch_reduction <= 90:
                break
            else:    
                print("Oops! This amount of reduction is to too much! Please enter a number between 40 and 90")
        except ValueError:
            print("Oops, invalid input. Please try again!")

    while True:
        try:
            recursion_depth = int(input("Please enter a number between (1-5) for your amount of branch generations: "))
            if 1 <= recursion_depth <= 5:
                break
            else:    
                print("Oops! This amount of recursions is too much! Too many recursions will slow the program down. Please enter a number between 1 and 5")
        except ValueError:
            print("Oops, invalid input. Please try again!")

    # Collected inputs from the user
    return trunk_length, branch_angle_left, branch_angle_right, branch_reduction, recursion_depth

# Recursive function to draw the tree
def draw_tree(length, depth, left_angle, right_angle, reduction):
    if depth == 0: # The base case - recursion stops when depth reaches 0
        return
    turtle.forward(length) # Trunk
    turtle.left(left_angle) # Left branch
    draw_tree(length * reduction / 100, depth - 1, left_angle, right_angle, reduction)
    turtle.right(left_angle + right_angle) # Right branch
    draw_tree(length * reduction / 100, depth - 1, left_angle, right_angle, reduction)
    turtle.left(right_angle) # Reset
    turtle.backward(length) # Back to original spot

# Main Menu Flow
def run_program():
    while True:
        main_menu()
        user_input = input("--> Enter 's' to start creating your tree ('q' to quit): ").strip().lower()
        if user_input == "s":
            print("\nLets create a tree!\n")
            trunk_length, left_angle, right_angle, reduction, depth = the_tree_inputs()

            # Turtle Setup
            turtle.speed(0)
            turtle.left(90)
            turtle.penup()
            turtle.goto(0, -200)
            turtle.pendown()

            # Draw tree
            draw_tree(trunk_length, depth, left_angle, right_angle, reduction)

            print("\nTree complete!")
            while True:
                retry = input("Would you like to create another tree? (y/n): ").strip().lower()
                if retry == "y":
                    turtle.reset()
                    break
                elif retry == "n":
                    print("\nGoodbye!\n")
                    turtle.bye()
                    return
                else:
                    print("Invalid input, please enter 'y' or 'n'.")

        elif user_input == "q":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice, please enter 's' to start or 'q' to quit.")

# Start the prgram
run_program()
