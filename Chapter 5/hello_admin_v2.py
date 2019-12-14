#20191213
#Chapter 5: Exercise 5.8 Hello Admin

#Start Program
print(f"\nSTART PROGRAM\n")

print(f"------------------------------\n")

user_names = ['ana','david','jason','liz','georgia','admin']

for user in user_names:
    if user == 'admin':
        print(f"Hello {user}, would you like a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in today.")

print(f"\n------------------------------")

#End Program
print(f"\nEND PROGRAM\n")