#20191209
#Chapter 4: Exercises 4.10 to 4.12

#Start Program
print(f"\nSTART PROGRAM\n")

#4.10 Slices ... need to select three items from the beginning, middle, and end of the list
heroes = ['wonder woman','batman','iron man','black widow','thor','hulk','dr. strange']

print(f"This is the original list:\n{heroes}\n")
print(f"These are the first three heroes:\n{heroes[:3]}\n")
print(f"These are the middle three heroes:\n{heroes[3:6]}\n")
print(f"These are the last three heroes:\n{heroes[-3:]}\n")

#4.11: My Pizzas, Your Pizzas
#Taking the original list from exercise 4.1 and addding a new pizza to the original list
pizzas = ['diavolo','gourmet','peperoni']
#Setting my fave pizzas to the original list
my_pizzas = pizzas[:]
my_pizzas.append('mushroom')
print(pizzas)
print(my_pizzas)

#Adding a different pizza to the list friend_pizzas
friend_pizzas = pizzas[:]
friend_pizzas.append('greek')
print(friend_pizzas)

#Prove the two lists are different by creating a print statement to show list contents
print(f"My favorite pizzas are:\n{my_pizzas}\n")
print(f"My friend's favorite pizzas are:\n{friend_pizzas}\n")

#4.12 More Loops
my_foods = ['pizza','falafel','carrot cake']

#The command below establishes a clone of the original list
friend_foods = my_foods[:]
print("\nMy fave foods are:\n")
print(my_foods)

print("\nMy friend's fave foods are:\n")
print(friend_foods)

#To prove we have 2 different lists, I'm going to append different values to each list
my_foods.append('wine')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#Here are two for loops to print the list items:

print(f"\nHere is a list of my favorite foods:\n")
for food in my_foods:
    print(food)

print(f"\nHere are my friend's favorite foods:\n")
for food in friend_foods:
    print(food)

#End Program
print(f"\nEND PROGRAM\n")