#20191212
#Chapter 5

#Start Program
print(f"\nSTART PROGRAM\n")

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print(f"\nFinished making your pizza!\n")

print(f"------------------------------\n")

#When running a single block of code, use if-elif
#When running multiple blocks of code, use multiple if statements.

#Here we are simplifying the loop.

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
print(f"\n------------------------------\n")

#Now we want to check for special items

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we're all out of {requested_topping}.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
print(f"\n------------------------------\n")

#Now we want to check that a list is not empty
#The statement "if requested_toppings:" tests to see if the list is empty.
#If values are contained in the list, it will print the personalized msgs.
#If the list is empty, it will ask the user if they're sure they want a plain pizza.

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print(f"\n------------------------------\n")

#Using multiple lists (making a comparison)

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','cats','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("Finished making your pizza.")


#End Program
print(f"\nEND PROGRAM\n")