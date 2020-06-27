
hearts = 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
diamonds =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
clubs = 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
spades = 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

dealer_hand = []
player_hand = []

dealer_numbers = []
player_numbers = []

def shuffle():

	hearts[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	diamonds[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	clubs[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	spades[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

	dealer_hand[:] = []
	player_hand[:] = []

	dealer_numbers[:] = []
	player_numbers[:] = []