"""
    File name: app.py
	Program name: Rocks, Papers, and Scissors CLI
	Description: A rock, paper, scissors CLI game
    Author: Marvin Ndlovu
    Date created: 22/07/2023
    Date last modified: 22/07/2023
    Python Version: 3.10.6
"""


#$ Main file of the game - Rock, Paper, Scissors CLI Game

# Imports
import random
from misc import processing, dash_divider, intro, init_loader, write_text, randomize, breather, bs, be, save_score
from _commands import _lives, _score, _exit, _rules
from rules import loss, win, draw, invalid_play, game_over, game_over_list


# Sroll effect time
T = 0.1

init_loader(0.05)

breather(1) 
write_text("\n"+bs+"Welcom to Rocks, Papers and Scissors CLI."+be)
write_text("Visit https://github.com/mrvn/rps-cli for more.")
print("")


class app:

	# Game play variables
	lives = 3
	wins = losses = draws = rounds = score = 0


	# Game entry
	while True:
		breather(T)
		write_text("Before we begin..........")

		# Asks the user for basic information
		breather(T)
		username = input(write_text("Please enter your name"))
		username = username.title()
		breather(T)


		processing(T)
		print("")
		write_text("\"WE ARE WITHIN\"")
		breather(T)
		print("")
		breather(T)
		dash_divider()
		dash_divider()

		print("")
		breather(0.5)
		write_text("\nHi "+username+". Let's play!!!\n")

		# Game introduction
		intro(lives, T)

		

		# Game play
		motivations = (
			'Let\'s go again!',
			"Let\'s go!",
			"One more time!",
			"Just one more!",
			"One more time again",
			"Keep going!",
			"You motivate me!"
		)

		while True:
			# Asks the player to play
			print("")
				
			
			breather(T)
			if rounds>0:
				write_text(randomize(motivations))
				breather(T)
			breather(T)
			player_rps = input(write_text("Type:\n R -Rock,\n P - Paper, or\n S - Scissors?\n"))
			player_rps = player_rps.lower()

			if player_rps=="r" or player_rps=="R":
				player_rps = "rock"
			if player_rps=="p" or player_rps=="Paper":
				player_rps = "paper"
			if player_rps=="s" or player_rps=="S":
				player_rps = "scissors"
			

			# The computer responds
			computer_rps = ("rock", "paper", "scissors")
			computer_turn = random.choice(computer_rps)

			# Play begins
			if player_rps != "score" and player_rps != "lives" and player_rps != "exit" and player_rps != "rules":
				breather(T)
				print("")
				print("+"*20)
				breather(T)
				write_text("Round "+(str(rounds+1)))
				print("\n")
				breather(T)
				write_text("You chose: "+player_rps)
				breather(T)
				write_text("The Might Computer chose: "+computer_turn)
				breather(T)
				print("")


			# The player loses
			if (player_rps=="rock" and computer_turn=="paper") or (player_rps=="paper" and computer_turn=="scissors") or (player_rps=="scissors" and computer_turn=="rock"):
				loss(T)
				lives -= 1
				losses += 1
				rounds += 1
				score -= 1

			# The player wins
			elif (player_rps=="rock" and computer_turn=="scissors") or (player_rps=="paper" and computer_turn=="rock") or (player_rps=="scissors" and computer_turn=="paper"):
				win(T)
				lives += 1
				wins += 1
				rounds += 1
				score += 1

			# Stalemate
			elif (player_rps==computer_turn):
				draw(T)
				lives = lives
				draws += 1
				rounds += 1
				score += 0.5

			# System commands
			elif player_rps == "rules":
				_rules(T)
			elif player_rps=="lives":
				_lives(lives, T)

			elif player_rps=="score":
				_score(rounds, wins, draws, losses, score, T)
				
			elif player_rps=="exit":
				save_score(score, rounds, wins, losses, draws, username, T)
				_exit(score, rounds, T)

			else:
				invalid_play(T)

			# Game life cycle
			if lives==0:
				message = randomize(game_over_list)
				breather(T)
				write_text("Sorry, you have run out of lives")
				breather(T)
				write_text(message)
				breather(T)
				print("")
				breather(T)
				save_score(score, rounds, wins, losses, draws, username, T)
				game_over(T)
				exit()

					






						
