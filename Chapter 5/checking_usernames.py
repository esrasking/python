#20191213
#Chapter 5: Exercise 5.10 Checking Usernames
#This program checks whether the user_name list is empty.
#If yes, it says we need more users. If not, if loops through the names
#and generates personalized messages.

#Start Program
print(f"\nSTART PROGRAM\n")

print(f"------------------------------\n")

current_users = ['arizona2005','esrasking','ajnworb','frankfurt_oma','djoras2007','plaid_hippo']
new_users = ['ESRasking','Parker_Baby','75_Penny','lenny_NYC','djoras2007','FRANKFURT_OMA']

for current_user in current_users:
    current_user = current_user.lower()
    print(current_user)

print(f"\n------------------------------\n")

for new_user in new_users:

    if new_user.lower() in current_users:
        print(f"\nSorry, that username is already taken.")
        print(f"Please pick a new username.\n")
    else:
        print(f"\nCongratulations, your username is available. Welcome, {new_user}.\n")
    
print(f"\n------------------------------\n")

#End Program
print(f"\nEND PROGRAM\n")