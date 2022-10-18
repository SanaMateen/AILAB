import random
choice=int(input("Type your choice--0--rock, 1--paper,2--scissors"))
print("You choose:",choice)
comp=random.randint(0,2)
print("Computer choose:",comp)

if choice>=3 or choice<0:
	print("You typed invalid number")
else:
	if choice==0 and comp==2:
		print("You win!")
	elif comp==0 and choice==2:
		print("You lose")
	elif comp>choice:
		print("You lose")
	elif choice>comp:
		print("You win")
	elif comp==choice:
		print("it is draw")
	