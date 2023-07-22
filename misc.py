"""
    File name: app.py
	Program name: Rocks, Papers, and Scissors CLI
	Description: A rock, paper, scissors CLI game
    Author: Marvin Ndlovu
    Date created: 22/07/2023
    Date last modified: 22/07/2023
    Python Version: 3.10.6
"""

## Miscellenious functions of RPS

# Imports
import time, random


# Variables
ROCK = "🪨"
PAPER = "📄"
SCISSORS = "✂️"
bs = "\033[1m"
be = "\033[0;0m"

# Timer function
def breather(t):
	time.sleep(t)

# The stars
def stars():
	print("*"*80)

# The processing effect
def processing(t):
	print("Processing.....")
	breather(t)
	print("Processing.....")
	breather(t)
	print("Processing.....")
	breather(t)
	print("Processing.....")
	breather(t)
	print("Processing.....")
	print("Processing.....")
	breather(0.35)


# Incorrect credentials
def incorrect_credentials(t):
	breather(t)
	write_text("Incorrect credentials")
	breather(0.3)
	stars()
	breather(t)


def dash_divider():
	print("-"*80)


# Introduction message
def intro(lives, t):
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)
	write_text("GAME RULES")
	breather(t)
	write_text("You start with "+str(lives)+" lives")
	breather(t)
	write_text("If you win, you gain a life.")
	breather(t)
	write_text("If you lose, you lose a life.")
	breather(t)
	write_text("If you draw, your lives remain the same")
	breather(0.5)
	print("")
	breather(t)
	print("You get the gist!")
	breather(t)
	print("")
	breather(t)
	dash_divider()
	breather(t)
	dash_divider()
	breather(t)
	write_text("Rule No. 1: Respect the rules.")
	breather(t)
	print("")
	breather(t)
	dash_divider()
	breather(t)
	write_text("Rule No. 2: Remember Rule No. 1")
	breather(t)
	print("")
	breather(t)
	dash_divider()
	breather(t)
	write_text("Type \"rules\" to see the list of rules")
	breather(t)
	write_text("Type \"exit\" to exit the game")
	breather(t)
	write_text("Type \"score\" to view your statistics")
	breather(t)
	write_text("Type \"lives\" to view lives you have left ❤️")
	breather(t)
	print("")
	breather(t)
	dash_divider()
	breather(t)
	dash_divider()
	breather(t)
	write_text("Your opponent is The Mighty Computer with infinite lives 💻")
	breather(t)
	write_text("How many rounds can you last against The Mighty Computer?")
	breather(t)
	write_text("Good luck! 💪")
	breather(t)
	print("")
	breather(t)
	dash_divider()
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)


# The intitial loader
def init_loader(t):
	i = 80
	print("#"*80)
	while i > 0:
		breather(0.1)
		print("-", end="", flush=True)
		i -= 1


def write_text(text):
	print("")
	i = 0
	for c in text:
		print(c, end="", flush=True)
		i += 1
		breather(0.05)

	return ": "


# Function to iterate a list randomy
def randomize(list):
	return random.choice(list)


# Write score to file
def save_score(score, rounds):
	if rounds!=0:
		score = score/rounds
	scoreboard.write(username)
	scoreboard.write("\t")
	scoreboard.write(str(rounds))
	scoreboard.write("\t")
	scoreboard.write(str(wins))
	scoreboard.write("\t")
	scoreboard.write(str(losses))
	scoreboard.write("\t")
	scoreboard.write(str(draws))
	scoreboard.write("\t")
	scoreboard.write(str(score))
	scoreboard.write("\n")
	scoreboard.close()
	_exit(rounds, T)