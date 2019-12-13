#20191213
#Chapter 5: Exercise 5.9 No Users
#This program checks whether the user_name list is empty.
#If yes, it says we need more users. If not, if loops through the names
#and generates personalized messages.

#Start Program
print(f"\nSTART PROGRAM\n")

print(f"------------------------------\n")

#user_names = ['ana','david','jason','liz','georgia','admin']

user_names = []
if user_names:

    for user in user_names:
        if user == 'admin':
            print(f"Hello {user}, would you like a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in today.")
else:
    print(f"We need to find some users!")

print(f"\n------------------------------\n")


#End Program
print(f"\nEND PROGRAM\n")