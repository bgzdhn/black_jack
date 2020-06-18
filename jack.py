#####################################################################

#INITIALISE INPUT

import random

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

#####################################################################

#DEALER'S HAND

def dealer_draw():
	suitNum1 = random.randint(1,4)
	if suitNum1 == 1:
		for dealerCard in hearts:
			dealerCard1 = random.choice(hearts)
			deal = dealerCard1, "hearts"
		hearts.remove(dealerCard1)
	elif suitNum1 == 2:
		for dealerCard in diamonds:
			dealerCard1 = random.choice(diamonds)
			deal = dealerCard1, "diamonds"
		diamonds.remove(dealerCard1)
	elif suitNum1 == 3:
		for dealerCard in clubs:
			dealerCard1 = random.choice(clubs)
			deal = dealerCard1, "clubs"
		clubs.remove(dealerCard1)
	elif suitNum1 == 4:
		for dealerCard in spades:
			dealerCard1 = random.choice(spades)
			deal = dealerCard1, "spades"
		spades.remove(dealerCard1)

	dealer_numbers.append(dealerCard1)
	dealer_hand.append(deal)
	return dealer_hand[0]

def draw_for_dealer():
	for x in range(2):
		deal = dealer_draw()

	print(deal)

#PLAYER'S HAND

def player_draw():
	suitNum2 = random.randint(1,4)
	if suitNum2 == 1:
		for playerCard in hearts:
			playerCard1 = random.choice(hearts)
			play = playerCard1, "hearts"
		hearts.remove(playerCard1)
	elif suitNum2 == 2:
		for playerCard in diamonds:
			playerCard1 = random.choice(diamonds)
			play = playerCard1, "diamonds"
		diamonds.remove(playerCard1)
	elif suitNum2 == 3:
		for playerCard in clubs:
			playerCard1 = random.choice(clubs)
			play = playerCard1, "clubs"
		clubs.remove(playerCard1)
	elif suitNum2 == 4:
		for playerCard in spades:
			playerCard1 = random.choice(spades)
			play = playerCard1, "spades"
		spades.remove(playerCard1)

	player_numbers.append(playerCard1)
	player_hand.append(play)
	return player_hand

def draw_for_player():
	for x in range(2):
		play = player_draw()

	print(play)

#####################################################################

#HITTING

def hit():
	suitNum3 = random.randint(1,4)
	if suitNum3 == 1:
		for playerCard in hearts:
			playerCard1 = random.choice(hearts)
			play1 = playerCard1, "hearts"
		hearts.remove(playerCard1)
	elif suitNum3 == 2:
		for playerCard in diamonds:
			playerCard1 = random.choice(diamonds)
			play1 = playerCard1, "diamonds"
		diamonds.remove(playerCard1)
	elif suitNum3 == 3:
		for playerCard in clubs:
			playerCard1 = random.choice(clubs)
			play1 = playerCard1, "clubs"
		clubs.remove(playerCard1)
	elif suitNum3 == 4:
		for playerCard in spades:
			playerCard1 = random.choice(spades)
			play1 = playerCard1, "spades"
		spades.remove(playerCard1)

	player_numbers.append(playerCard1)
	player_hand.append(play1)
	return player_hand

#####################################################################

#DETERMIN THE WINNER

def count_dealer():
	total = sum(dealer_numbers)
	return total

def count_player():
	total = sum(player_numbers)
	return total

def find_winner():
	dealer_total = count_dealer()
	player_total = count_player()

	if player_total > 21:
		return "Dealer:", dealer_total, "Player:", player_total, "Player is bust! Dealer wins!"
	elif dealer_total > 21:
		return "Dealer:", dealer_total, "Player:", player_total, "Dealer is bust! Player wins!"
	elif dealer_total > player_total:
		return "Dealer:", dealer_total, "Player:", player_total, "Dealer wins!"
	else:
		return "Dealer:", dealer_total, "Player:", player_total, "Player wins!"

#####################################################################

#GAME LOOP

def loop():
	#set condition variables
	finished = 0
	first_draw = 0
	#game loop
	while finished == 0:
		#draw the cards
		while first_draw == 0:
			draw_for_dealer()
			draw_for_player()
			first_draw = 1

		
		#Check the deck to make sure its being restocked
		"""
		print(hearts)
		print(diamonds)
		print(spades)
		print(clubs)
		"""
		
		print("Press h to hit. Press p to play your hand.")
		y = input()

		#if players hits
		if y == "h":
			#show dealer's first card
			print(dealer_hand[0])
			#give player another card
			hit()
			#show players new hand
			print(player_hand)
		#if player plays
		elif y == "p":
			#find winner
			print(find_winner())
			#ask if player wants to play again
			print("Play again? (y/n)")
			y2 = input()
			#if player says no, end game
			if y2 == "n":
				print("Game Over!")
				#end loop
				finished = 1
			#if player says yes, shuffle deck and restart loop
			elif y2 == "y":
				#shuffle
				shuffle()
				#reset draw loop
				first_draw = 0
				#reset game loop
				finished = 0

#####################################################################

#START THE GAME

loop()