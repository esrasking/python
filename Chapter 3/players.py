#20191203 
#Chapter 4: Players
#Working with part of a list

#Start Program
print(f"\nSTART PROGRAM\n")

#Slicing a list, the following code will only print the first three players in the list
#Remember, Python stops one element short of the second index specified. 
#Asking for the first three values will generate index numbers 0, 1, and 2.

players = ['charles','martina','michael','florence','eli']
print(players)
print(players[0:3])

#We can also choose a slice within a list by calling on specific index ranges
#Rememeber, the first value in the range is where the program starts, where 0 is the first position
#the second value is the boundary of where the program ends 4 refers to the 5th term, so the 
#program will end on the fourth term (or index 3)
print(players[1:4])

#Now we omit the starting index, this will include everything up to the 4th index (or 5th term)
print(players[:4])

#Now we include the starting index position, but omit the boundary. This returns everything from
#the second index (or third term)
print(players[2:])

#You can also choose a slice relative to the bottom of the list. This following will pick the 
#last three terms of the list
print(players[-3:])

#Looping through a slice, the code below starts at the beginning and then returns first 3 terms
print("\nHere are the first three players on my team:\n")
for player in players[:3]:
    print(player.title())

#End Program
print(f"\nEND PROGRAM\n")
