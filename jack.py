#####################################################################

#INITIALISE INPUT

import random

hearts = 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
diamonds =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
clubs = 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
spades = 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

dealer_hand = []
player_hand = []

#####################################################################

#DEALERS HAND

suitNum1 = random.randint(1,4)
if suitNum1 == 1:
	for dealerCard in hearts:
		dealerCard1 = random.choice(hearts)
		dfinal1 = dealerCard1, "hearts"
	hearts.remove(dealerCard1)
elif suitNum1 == 2:
	for dealerCard in diamonds:
		dealerCard1 = random.choice(diamonds)
		dfinal1 = dealerCard1, "diamonds"
	diamonds.remove(dealerCard1)
elif suitNum1 == 3:
	for dealerCard in clubs:
		dealerCard1 = random.choice(clubs)
		dfinal1 = dealerCard1, "clubs"
	clubs.remove(dealerCard1)
elif suitNum1 == 4:
	for dealerCard in spades:
		dealerCard1 = random.choice(spades)
		dfinal1 = dealerCard1, "spades"
	spades.remove(dealerCard1)

suitNum2 = random.randint(1,4)
if suitNum2 == 1:
	for dealerCard in hearts:
		dealerCard2 = random.choice(hearts)
		dfinal2 = dealerCard2, "hearts"
	hearts.remove(dealerCard2)
elif suitNum2 == 2:
	for dealerCard in diamonds:
		dealerCard2 = random.choice(diamonds)
		dfinal2 = dealerCard2, "diamons"
	diamonds.remove(dealerCard2)
elif suitNum2 == 3:
	for dealerCard in clubs:
		dealerCard2 = random.choice(clubs)
		dfinal2 = dealerCard2, "clubs"
	clubs.remove(dealerCard2)
elif suitNum2 == 4:
	for dealerCard in spades:
		dealerCard2 = random.choice(spades)
		dfinal2 = dealerCard2, "spades"
	spades.remove(dealerCard2)

print ("DEALER'S HAND")
print (dfinal1)
print (dfinal2)

dfinal3 = dealerCard1 + dealerCard2

#####################################################################

#PLAYERS HAND

suitNum3 = random.randint(1,4)
if suitNum3 == 1:
	for playerCard in hearts:
		playerCard1 = random.choice(hearts)
		pfinal1 = playerCard1, "hearts"
	hearts.remove(playerCard1)
elif suitNum3 == 2:
	for playerCard in diamonds:
		playerCard1 = random.choice(diamonds)
		pfinal1 = playerCard1, "diamonds"
	diamonds.remove(playerCard1)
elif suitNum3 == 3:
	for playerCard in clubs:
		playerCard1 = random.choice(clubs)
		pfinal1 = playerCard1, "clubs"
	clubs.remove(playerCard1)
elif suitNum3 == 4:
	for playerCard in spades:
		playerCard1 = random.choice(spades)
		pfinal1 = playerCard1, "spades"
	spades.remove(playerCard1)

suitNum4 = random.randint(1,4)
if suitNum4 == 1:
	for playerCard in hearts:
		playerCard2 = random.choice(hearts)
		pfinal2 = playerCard2, "hearts"
	hearts.remove(playerCard2)
elif suitNum4 == 2:
	for playerCard in diamonds:
		playerCard2 = random.choice(diamonds)
		pfinal2 = playerCard2, "diamonds"
	diamonds.remove(playerCard2)
elif suitNum4 == 3:
	for playerCard in clubs:
		playerCard2 = random.choice(clubs)
		pfinal2 = playerCard2, "clubs"
	clubs.remove(playerCard2)
elif suitNum4 == 4:
	for playerCard in spades:
		playerCard2 = random.choice(spades)
		pfinal2 = playerCard2, "spades"
	spades.remove(playerCard2)

print("PLAYER'S HAND")
print(pfinal1)
print(pfinal2)

pfinal3 = playerCard1 + playerCard2

#####################################################################

#check who is bust, check player first. If noone is bust, check who wins.

if pfinal3 > 21:
	print("Player is bust!")
elif dfinal3 > 21:
	print("Dealer is bust!")
elif dfinal3 > pfinal3:
	print("Dealer is highest! Dealer wins!")
elif dfinal3 == pfinal3:
	print("Draw. Dealer wins!")
else:
	print("Player is highest! Player wins!")

#print(hearts)
#print(diamonds)
#print(clubs)
#print(spades)