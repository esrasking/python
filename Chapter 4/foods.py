#20191203
#Chapter 4: Copying a List

#Start Program
print(f"\nSTART PROGRAM\n")

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



#End Program
print(f"\nEND PROGRAM\n")