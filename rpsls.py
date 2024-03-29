# Mekedelawit E. Hailu 

# Rock-Paper-Scissors-Lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    
    # convert name to number using if/elif/else
    # don't forget to return the result!

    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4  
    else:
        return None


def number_to_name(number):
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return None

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games

    print 
    
    # print out the message for the player's choice

    print "Player chooses", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    player_number = name_to_number(player_choice)

    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_number = random.randrange(0, 5)

    # print out the message for computer's choice
    
    comp_choice = number_to_name(comp_number)

    # compute difference of comp_number and player_number modulo five
    
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    
    difference = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message

    if difference == 0:
        print "Player and computer tie!"
    elif difference == 1 or difference == 2:
        print "Player wins!"
    else:
        print "Computer wins!"
    
          
# test your code 

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
