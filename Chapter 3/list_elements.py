#20191201
#Chapter 3: List Elements

#Start Program
print('')
print("START PROGRAM")
print("")

#Modifying elements in a list, remember the index starts at 0
print("Modifying the element in a list:\n")
animals=['cat','dog','bird']
print(animals)

animals[2]='mouse'
print(animals)
print('')

#Appending Elements to the End of a List
animals=['cat','dog','bird']
print("Here is the list of original animals again:\n")
print(f"{animals}\n")

print("Now we're appending an item to the end of the list:\n")
animals.append('mouse')
print(f"{animals}\n")

#Appending to an empty list
wine=[]
wine.append('rioja')
wine.append('chardonnay')
wine.append('merlot')
wine.append('pinot grigio')

print(wine)
print('')

#Insert elements to a list
#First list the position, then the element
print(wine)
wine.insert(0, 'riesling')
print(wine)
wine.insert(3,'pinot noir')
print(wine)

#Removing an element from a list
print(f"\n{wine}\n")
del wine[0]
print(wine)

del wine[2]
print(wine)

#Removing an item using the pop() Method
animals=['cat','dog','bird']
print(animals)

#This sets the list to one short of the last entry
popped_animals = animals.pop()
#This prints the shortened list
print(animals)
#This reveals the value of the popped item
print (popped_animals)

#Popping Items from any position in a list
animals = ['cat','dog','bird']
pet=animals.pop(0)
print(f"\nMy current pet is a {pet}.\n")
print(animals)

#Removing an item by value
print(f"\n{wine}\n")
wine.remove('merlot')
print(wine)

#Remove an item by value and setting a variable
exp_wine = 'rioja'
wine.remove(exp_wine)
print(wine)
print(exp_wine)
print(f"I find {exp_wine} way too expensive in the US.\n")

#End Program
print('')
print ("END PROGRAM")
print("")