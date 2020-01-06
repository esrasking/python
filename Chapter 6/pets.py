#20200105
#Chapter 6: Exercise 6.8 Pets

#Making several dictionaries where each represents a different pet.
#Store the dictionaries in a list called Pets.
#Loop through the list and print all the info for each pet.

#START PROGRAM
print(f"\nSTART PROGRAM")
print("--------------------\n")

#Here are my three separate pet dictionaries

pet_1 = {
    'animal' : 'cat',
    'pet_name' : 'parker',
    'owner' : 'liz rasking',
    'location' : 'ellicott city',
}

pet_2 = {
    'animal' : 'dog',
    'pet_name' : 'tiki',
    'owner' : 'carol young',
    'location' : 'orlando',
    }

pet_3 = {
    'animal' : 'rat',
    'pet_name' : 'squeakers',
    'owner' : 'anna white',
    'location' : 'sykesville',
}

#Here is my list storing the dictionaries

pets = [pet_1, pet_2, pet_3]

#Printing raw data in dictionary
for pet in pets:
    print (pet)

print("\n--------------------")

#Printing formatted data from dictionaries
for pet in pets:
    for a,b in pet.items():
        print(f"{a.title()} : {b.title()}")
    print(" ")


print("\n--------------------")
#END PROGRAM
print(f"END PROGRAM")