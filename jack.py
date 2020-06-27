#####################################################################

#INITIALISE INPUT

from shuffle import *
from draw import *
from hit import *
from winner_logic import *

#####################################################################

#cut the deck, imported from shuffle.py

#####################################################################

#draw the dealer's cards and player's cards, imported from draw.py

#####################################################################

#hit player, imported from hit.py

#####################################################################

#use selection to find the winner, imported from winner_logic.py

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