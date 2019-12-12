#20191212
#Chapter 5: Exercises 5.3 to 5.5 Alien Colors

#Start Program
print(f"\nSTART PROGRAM\n")

#Exercise 5.3: Assigning green, yellow, or red to alien_color. Test for green
#The code below will test positive for being green.

print(f"Exercise 5.3:\n")
alien_color = 'green'

if 'green' in alien_color:
    print("You just earned 5 points.")
print("\n-------------------------------\n")

#The code below will test negative for being green. No output is generated.
alien_color = 'yellow'

if 'green' in alien_color:
    print("You just earned 5 points.")

print("\n-------------------------------\n")

#Exercise 5.4: Running one if block and one else block to assign points
print(f"Exercise 5.4:\n")
print("If Blocks:\n")

alien_color = 'red'

if 'green' in alien_color:
    print ("You get 5 points.")
if 'red' in alien_color:
    print("You get 10 points.")
if 'yellow' in alien_color:
    print("You get 10 points.")

print("\n-------------------------------\n")

print("If Else Block:\n")

alien_color = 'green'

if 'green' in alien_color:
    print("You get 5 points.")
else:
    print("You get 10 points.")

print("\n-------------------------------\n")
print(f"Exercise 5.5:\n")
alien_color = 'green'

if 'green' in alien_color:
    print ("You get 5 points.")
elif 'red' in alien_color:
    print("You get 10 points.")
elif 'yellow' in alien_color:
    print("You get 15 points.")

alien_color = 'red'

if 'green' in alien_color:
    print ("You get 5 points.")
elif 'red' in alien_color:
    print("You get 10 points.")
elif 'yellow' in alien_color:
    print("You get 15 points.")

alien_color = 'yellow'

if 'green' in alien_color:
    print ("You get 5 points.")
elif 'red' in alien_color:
    print("You get 10 points.")
elif 'yellow' in alien_color:
    print("You get 15 points.")

    
#End Program
print(f"\nEND PROGRAM\n")