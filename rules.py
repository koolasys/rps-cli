"""
    File name: rules.py
	Program name: Rocks, Papers, and Scissors CLI
	Description: A rock, paper, scissors CLI game
    Author: Marvin Ndlovu
    Date created: 22/07/2023
    Date last modified: 22/07/2023
    Python Version: 3.10.6
"""


###############################################################################
## The House Rules of RPS

# Imports
from misc import dash_divider, write_text, breather, randomize


# Variables

winner = [
	"Rock, paper, scissors... and you rule!",
	"You're on a roll, rock-paper-scissors pro!",
	"You must be the chosen one, mastering rock-paper-scissors!",
	"Who needs luck when you have skills like that?",
	"You're the master of the hand games!",
	"No doubt, you're the rock-paper-scissors boss!",
	"The champion of hands, it's you!",
	"Scissors and paper need a new strategy against you!",
	"You make rock-paper-scissors look easy!",
	"Rock beats scissors, but you beat them all! 🏆✊✋✌️",
	"Scissors, the ultimate ruler of... scissoring stuff, I guess?",
	"Damn! You actually won!",
	"You've mastered the ancient art of rock-paper-scissors-fu!",
	"You slowly becoming the RPS Grandmaster!",
	"Your rock-paper-scissors prowess is the stuff of legends!",
	"You've left a trail of CPUs in your wake—impressive!",
	]

loser = [
	"Wow, what a surprise there! So unexpected!",
	"Better luck next time!",
	"You lose. Sorry!"
	"No shame in losing to a rock-paper-scissors pro like them!"
	"You've got potential!",
	"\"Don't worry, it's just a game!!\", said the Winner after woopin' @$$",
	"It's just one game, there are plenty more to go!",
	"You played well! Rock-paper-scissors can be tricky!",
	"Scissors, the master of snipping air! You almost had 'em!",
	"Scissors, the world's greatest at cutting...your hopes!",
	"Really almost had me in the first half!",
	"If only there was an award for trying!",
	"In an alternate universe, you'd be the rock-paper-scissors MVP!",
	"You've unlocked the achievement: 'Loser Extraordinaire'! 😏👏",
	"You've got potential!",
	"Not winning is just another way to keep life interesting!",
	"Losing is just your secret plan to give others a chance to shine!",
	"You lost this round, but your witty banter game is on point!",
	"As long as you having fun!",
	"I mean, we can\'t all be winners!",
	"Congrats on your incredible performance...of making others look good!",
	"You're like a diamond—losing just brings out more of your sparkle!"
]

drawer = [
	"It's a draw!"
	"Keep your chin up, Buttercup!",
	"Oh, a draw! The ultimate showdown of indecisiveness!",
	"Wow, it's like you two were destined to be equally mediocre!",
	"The universe couldn't decide, so it settled for a tie!",
	"It's a draw! The universe couldn't handle picking the loser!",
	"Haha! You both lose!",
	"In the history of rock-paper-scissors, this is... forgettable.",
	"Rematch!",
	"Behold, the ultimate display of balanced mediocrity!",
	"Not winning is just another way to keep life interesting!"
]

game_over_list = [
	"Well, losing is a talent too, and you've got it in spades!",
	"Hey, at least you lost with style! Nobody does it quite like you!",
	"Not winning is just another way to keep life interesting!",
	"Losing is just your secret plan to give others a chance to shine!",
	"Don't sweat it! Losing is just a momentary pause in your domination!",
	"Congrats on your incredible performance...of making others look good!",
	"Every champion needs a rest—losing is just your well-deserved break!",
	"Remember, it's not about winning every time; it's about having fun!",
	"Even when you lose, you win the title of 'Most Fun Loser'!",
	"Congratulations on being the most gracious RPS participant! 😄🏆",
	"Thanks for playing. I mean it."
]


# End of game lives
def game_over(rounds, wins, draws, t):
	message = randomize(game_over_list)
	breather(t)
	write_text("Sorry, you have run out of lives")
	breather(t)
	write_text(message)
	breather(t)
	print("")
	breather(t)
	write_text("Your Score")
	breather(t)
	write_text("Rounds played: "+str(rounds))
	breather(t)
	write_text("Rounds won: "+str(wins))
	breather(t)
	write_text("Rounds lost: "+str(rounds-wins-draws))
	breather(t)
	write_text("Rounds drew: "+str(draws))
	breather(t)
	print("")
	breather(t)
	dash_divider()
	breather(t)
	print("")
	breather(t)
	
	stop = input("Press \"Enter\" to exit.")
	i = 80
	while i > 0:
		breather(0.1)
		print("-", end="", flush=True)
		i -= 1
	print("")
	print("#"*80)
	breather(t)
	exit()


# Invalid play rule
def invalid_play(t):
	breather(t)
	write_text("Invalid play! Try again.")
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)


# Game drawn
def draw(t):
	message = randomize(drawer)
	breather(t)
	write_text(message)
	breather(t)
	write_text("❤️")
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)


# Player wins
def win(t):
	message = randomize(winner)
	breather(t)
	write_text(message)
	breather(t)
	write_text("❤️+1")
	breather(t)
	print("")
	breather(t)
	print("")
	breather(t)


# Player loses
def loss(t):
	message = randomize(loser)
	breather(t)
	write_text(message)
	breather(t)
	write_text("💔-1")
	breather(t)
	print("")
	breather(t)
	print("")









