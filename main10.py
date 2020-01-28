#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # prints greetings!
colors = ['red','orange','yellow','green','blue','violet','purple'] # defines what colors are
play_again = '' # defines what the play_again variable is
best_count = sys.maxsize # defines the best_count variable           # the biggest number

while (play_again != 'n' and play_again != 'no'): # begins the code with a while statment that all else will fall under
    match_color = random.choice(colors) # picks a color from the set randomly
    count = 0 # sets variable count to 0
    color = '' # defines variable color
    while (color != match_color):
        color = input("\nWhat is my favorite color? ") # prompts the player on a new line to answer the query #\n is a special code that adds a new line
        color = color.lower().strip() #pulls the player's input from the area where the answer is typed
        count += 1 # adds 1 to the count for each guess
        if (color == match_color): # determines what the correct answer is based off of the color randomly picked
            print('Correct!') # prints correct if the player was correct
        else: # begins else statement
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # tells the player they were incorrect, as well as defines the variable guesses as the count
    
    print('\nYou guessed it in {} tries!'.format(count)) # tells the player that they were correct and displays the amount of guesses

    if (count < best_count): # if  statement saying if the count was lower than best_count variable to begin an action
        print('This was your best guess so far!') # prints that this was the best guess so far if aforementioned count was lower than best_count
        best_count = count # defines best_count once again as the new best_count IF the player had their best count so far

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() # asks the player if they would like to play again, resets or does not based on input

print('Thanks for playing!') # standard goodbye message, terminates