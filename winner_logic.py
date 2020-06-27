from shuffle import *

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