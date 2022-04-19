"""
Created by Tevin

In input you must write rock, paper or scissors
"""


import random as rand

options = ["rock", "paper", "scissors"]

while True: 
	inp = input("Rock/Paper/Scissors: ").lower()

	if inp not in options:
		print("You must write rock or paper or scissors")
		break

	randNum = rand.randint(0,2)
	comp = options[randNum]
	print("\nComputer picked ", comp + ".")

	if inp == "rock" and comp == "scissors":
		print("YOU WON!!!")
		break

	elif inp == "paper" and comp == "rock":
		print("YOU WON!!!")
		break

	elif inp == "scissors" and comp == "paper":
		print("YOU WON!!!")
		break

	elif inp == comp:
		print("Choices are same)) It's draw")
		break

	else:
		print("YOU LOSE! TRY AGAIN))")
		break
	
print("Created by Tevin Thomas")
