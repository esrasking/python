#20191201
#Chapter 3.6: More Guests

#Start Program
print('')
print("START PROGRAM")
print('')

#Picking up from exercise 3.5
guests=['dave matthews','dr. seuss','robin williams']
print(f"{guests}\n")

print(f"These are the guests I'd like to individually invite to dinner:\n\t{guests[0].title()}, \n\t{guests[1].title()}, \n\t{guests[2].title()}.\n")
print(f"Dear {guests[0].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[1].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[2].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")

#Announcing that we found a bigger table.
print(f"Hello Everyone, we just wanted to let you know that we were able to find a larger table!\nPlease stay tuned for your new invites.\n")

#Inserting a new guest to the beginning of my list
new_guest = 'marylin monroe'
print(f"{new_guest.title()} will be a new guest at dinner.\n")
guests.insert(0,new_guest)
print(f"{guests}\n")

#Inserting a new guest to the middle of my list
new_guest = 'salvador dali'
print(f"{new_guest.title()} will be a new guest at dinner.\n")
guests.insert(2,new_guest)
print(f"{guests}\n")

#Appending a new guest to the end of my list
new_guest = 'jack mcCoy'
print(f"{new_guest.title()} will be a new guest at dinner.\n")
guests.append(new_guest)
print(f"{guests}\n")

#Reissuing the invites to all the guests.
print(f"Dear {guests[0].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[1].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[2].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[3].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[4].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[5].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")

#End Program
print('')
print("END PROGRAM")
print('')