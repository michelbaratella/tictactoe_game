import os
clear = lambda: os.system('clear')

# Requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

### VARIABLE DEFINITION - START ###
position = [1,2,3,4,5,6,7,8,9]
player1 = 'empty'
player2 = 'empty'
currentPlayer = 'empty'
restart = True
### VARIABLE DEFINITION - END ###

def show_title():
	print('####### ###  #####     #######    #     #####     ####### ####### #######')
	print('   #     #  #     #       #      # #   #     #       #    #     # #      ')
	print('   #     #  #             #     #   #  #             #    #     # #      ')
	print('   #     #  #             #    #     # #             #    #     # #####  ')
	print('   #     #  #             #    ####### #             #    #     # #      ')
	print('   #     #  #     #       #    #     # #     #       #    #     # #      ')
	print('   #    ###  #####        #    #     #  #####        #    ####### #######')
	print('')

# Player 1 chooses if he wants to be X or O
def choose_player_marker(player1, player2):
	while player1 == 'empty':
		player1 = input('Player 1, please choose (X or O): ').upper()
		print('')
		if player1 == 'X':
			player2 = 'O'
		elif player1 == 'O':
			player2 = 'X'
		else:
			clear()
			show_title()
			print('Invalid choice, try again.')
			print('')
			player1 = 'empty'
	return (player1, player2)

# Display initial board
def display_board():
	print(f'{position[0]} | {position[1]} | {position[2]}')
	print(f'{position[3]} | {position[4]} | {position[5]}')
	print(f'{position[6]} | {position[7]} | {position[8]}')
	print('')

# Player 1 makes first move and game loops until someone wins
def player_move(player, position):
	move = 999
	proceed = False
	while not proceed:
		move = input(f"Player '{player}', choose a position from the board (1 through 9): ")
		print('')
		if move.isdigit():
			move = int(move)
			if move not in range(1,10):
				clear()
				display_board()
				print('Invalid choice, try again.')
				print('')
			elif move not in position:
				clear()
				display_board()
				print('This position is already taken, try again.')
				print('')
			else:
				proceed = True
		else:
			clear()
			display_board()
			print('Invalid choice, try again.')
			print('')
	for n in range(0, len(position)):
		if int(move) == position[n]:
			position[n] = player
	return position

# Check if someone has won or tied the game
def check_game(player):
	have_any = False
	if (position[0] == player and position[1] == player and position[2] == player) or (position[3] == player and position[4] == player and position[5] == player) or (position[6] == player and position[7] == player and position[8] == player) or (position[0] == player and position[3] == player and position[6] == player) or (position[1] == player and position[4] == player and position[7] == player) or (position[2] == player and position[5] == player and position[8] == player) or (position[0] == player and position[4] == player and position[8] == player) or (position[2] == player and position[4] == player and position[6] == player):
		game_over()
		print(f"Player '{player}' has won the game!")
		print('')
		return False
	else:
		for n in range(1,10):
			if n in position:
				have_any = True
		if not have_any:
			game_over()
			print("Game Tied!")
			print('')
			return False
		else:
			return True

# Ask if player wants to play again
def play_again():
	restart = 'empty'
	while restart == 'empty':
		restart = input("Do you want to play again? (Y or N) ").upper()
		print('')
	if restart == 'Y':
		return True
	elif restart == 'N':
		return False
	else:
		restart = 'empty'

# Check whose turn it is
def check_turn(i, player1, player2):
	if i % 2 == 0:
		return player1
	else:
		return player2

def game_over():
	print(' #####     #    #     # #######    ####### #     # ####### ###### ')
	print('#     #   # #   ##   ## #          #     # #     # #       #     #')
	print('#        #   #  # # # # #          #     # #     # #       #     #')
	print('#  #### #     # #  #  # #####      #     # #     # #####   ###### ')
	print('#     # ####### #     # #          #     #  #   #  #       #   #  ')
	print('#     # #     # #     # #          #     #   # #   #       #    # ')
	print(' #####  #     # #     # #######    #######    #    ####### #     #')
	print('')

#### CODE EXECUTION BELOW ####
while restart:
	position = [1,2,3,4,5,6,7,8,9]
	player1 = 'empty'
	player2 = 'empty'
	clear()
	game_in_progress = True
	while game_in_progress:
		# 1 - Print the board
		print('')
		show_title()
		player1, player2 = choose_player_marker(player1, player2)
		clear()
		display_board()

		for i in range(0,100):
			currentPlayer = check_turn(i, player1, player2)
			# 2 - Take player input
			position = player_move(currentPlayer, position)
			clear()
			# 3 - Place input on board
			display_board()
			# 4 - Check if game is won/lost or tied
			game_in_progress = check_game(currentPlayer)

			if not game_in_progress:
				break
	# 6 - After game is over, ask if they want to play again
	restart = play_again()
#### CODE EXECUTION ABOVE ####