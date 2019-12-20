#20191219
#Chapter 6: Exercise 6.6 Polling

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

users = ['jen','sarah','edward','phil','jason','karen','liz']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for user in users:
    if user in favorite_languages:
        print(f"Thank you for already taking the poll, {user.title()}.")
    else:
        print(f"Please take our poll, {user.title()}.")

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")