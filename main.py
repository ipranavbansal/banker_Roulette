import random

names_string = input("Give me everybody's names, separated by a comma and followed with a single space. ")
names = names_string.split(", ")

random_index = random.randint(0,len(names)-1)
random_person= names[random_index]

print(f"{random_person} is going to buy the meal today!")