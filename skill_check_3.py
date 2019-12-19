#!/usr/bin/env python

'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

# Define a dictionary of the rules for the game
rules = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}

'''
Create a function to determine the winner of the game.  This function will have two arguments:
    player1_move
    player2_move

This function will compare the results provided- if they are the same it is a draw
If the results are not the same, the player1 provided move will be compared against the rules dictionary.
The move provided by player 1 will be used as the key to search for.  When that key is found, the value for the
key value pair will be compared against the move provided by Player 2.  If there is a match, player 1 has won.
If it isn't a draw, and player 1 did not beat player 2, the next result is that player 2 wins.
The function will return the string that will be printed to stdout.
'''
def determine_winner(player1_move, player2_move):
    if player1_move.lower() == player2_move.lower():
        return "It is a Draw!"
    for check in rules:
        if player1_move.lower() == check and player2_move.lower() == rules[check]:
            return "Player 1 Wins!"
        else:
            return "Player 2 Wins!"

# Start the infinite loop for a new game
# As long as new_game is True, the loop will run indefinitely unless broken or new_game becomes False
new_game = True

while new_game:
    # Define a list of available moves
    moves = ['rock', 'paper', 'scissors']

    # Prompt Player 1 for their Move
    player1_move = input(f"Player 1, Select from {moves}: ")

    # Start a loop for the user move if the value provided was not in the 'moves' list
    # Break the loop when the user provides a correct move
    while player1_move.lower() not in moves:
        player1_move = input(f"Player 1, Select from {moves}: ")

    # Prompt Player 2 for their Move
    player2_move = input(f"Player 2, Select from {moves}: ")

    # Start a loop for the user move if the value provided was not in the 'moves' list
    # Break the loop when the user provides a correct move
    while player2_move.lower() not in moves:
        player2_move = input(f"Player 2, Select from {moves}: ")

    # Provide the user moves to the determine_winner function and store the returned data as the variable result
    result = determine_winner(player1_move, player2_move)

    # Print the results to stdout
    print(f"\n{result}\n")

    # Define the options for continuing the game
    continue_opts = ['Y', 'N']

    # Prompt if the user would like to play a new game
    new_game = input("Would you like to play a new game? [Y/N]: ")

    # Start a loop to validate if the user would like to play a new game
    # if the value provided was not in the 'continue_opts' list
    while new_game.upper() not in continue_opts:
        new_game = input("Would you like to play a new game? [Y/N]: ")

    # If the user does not want a new game, set the value to False, which will end the loop
    if new_game.upper() == "N":
        new_game = False
    # If the user wants a new game, the loop will start over from the beginning.
    elif new_game.upper() == "Y":
        print("Starting over\n")