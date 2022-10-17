import random
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")



mem=len(names)

me=random.randint(0,mem-1)

print(names[me],"is going to buy the meal day")
