import random
from shuffle import *

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