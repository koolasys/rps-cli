"""
    File name: app.py
	Program name: Rocks, Papers, and Scissors CLI
	Description: A rock, paper, scissors CLI game
    Author: Marvin Ndlovu
    Date created: 22/07/2023
    Date last modified: 22/07/2023
    Python Version: 3.10.6
"""

## House Commands of RPS

# Imports
from misc import write_text, stars, breather, save_score


# Command to exit the game
def _exit(score, rounds, t):
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	write_text("\"QUITER\" (\"coughs\"), said The Might Computer.")
	breather(t)
	print("")
	stars()
	breather(0.2)
	outro = "| But hey! At least you lasted about "+str(rounds)+" rounds |"
	print("-"*(len(outro)+1))
	write_text(outro)
	print("")
	print("-"*(len(outro)+1))
	breather(t)
	write_text("Your score has been recorded")
	breather(t)
	print("")
	
	i = 80
	while i > 0:
		breather(0.1)
		print("-", end="", flush=True)
		i -= 1
	print("")
	print("#"*80)
	breather(t)
	exit()
	


# Command to view current score
def _score(rounds, wins, draws, losses, score, t):
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	write_text("Score")
	breather(t)
	print("")
	breather(t)
	stars()
	write_text("Rounds played: "+str(rounds))
	breather(t)
	write_text("Rounds won: "+str(wins))
	breather(t)
	write_text("Rounds lost: "+str(losses))
	breather(t)
	write_text("Rounds drew: "+str(draws))
	breather(t)
	write_text("Current score: "+str(score))
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	print("")
	breather(t)
	write_text("""\n.\n.\n.""")
	print("")
	i = 80
	while i > 0:
		breather(0.1)
		print("-", end="", flush=True)
		i -= 1
	print("")
	print("#"*80)
	breather(1)
	exit()


# Command to view current lives left
def _lives(lives, t):
	print("")
	breather(t)
	stars()
	breather(t)
	write_text("Lives")
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	write_text("You have "+"❤️"*lives+" left")
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	print("")
	breather(t)


# Command to view the game rules
def _rules(t):
	print("")
	breather(t)
	stars()
	breather(t)
	write_text("Rules")
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	write_text("-Rock loses to Paper")
	breather(t)
	write_text("-Paper loses to Scissors")
	breather(t)
	write_text("-Scissors loses to Rock")
	breather(t)
	print("")
	breather(t)
	stars()
	breather(t)
	print("")
	breather(t)








