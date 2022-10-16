import random
print("Rock Paper Scissor Game")
usr=int(input("What is your choice? Type 0 for Rock, 1 for Paper, 2 for scissor"))
print("You choose:")
print(usr)
if usr>=3 or usr<0:
	print("invalid choice")
else:
	print("Computer choose:")
	comp=random.randint(0,2)
	print(comp)
	if comp==0 and usr==2:
		print("You lose")
	elif usr==0 and comp==2:
		print("You win")
	elif comp>usr:
		print("You lose")
	elif usr>comp:
		print("you win")
	elif comp==usr:
		print("it's draw")
	else:
		print("....")
	