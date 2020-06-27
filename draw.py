import random
from shuffle import *

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