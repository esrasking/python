#20191202
#Chapter 4: Introducing for Loops

#Start Program
print(f"\nSTART PROGRAM\n")

#Creating first for loop for magicians, simply print names
magicians = ['alice','david','caroline']
for magician in magicians:
    print(magician)

print('')

#Using a for loop to personalize messages
magicians = ['alice','david','caroline']
for magician in magicians:
    print(f"{magician.title()}, that was a lame trick. You suck!")
    print(f"I hope your next trick is better, {magician.title()}.\n")

print("Geez, thanks everyone. I'll never get that time back.")

#End Program
print(f"\nEND PROGRAM\n")