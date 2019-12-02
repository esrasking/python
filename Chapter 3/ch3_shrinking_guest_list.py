#20191201
#Chapter 3.7: Shrinking Guest List

#Start Program
print('')
print("START PROGRAM")
print('')

#Picking up from Exercise 3.6, we need the original list as a reference
guests=['dave matthews','dr. seuss','robin williams']

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

#Announcing the table is canceled and will only seat 2.
print(f"I'm sorry to share that our table was cancelled. \nWe've had to relocate to a smaller venue. \nSadly, we can only seat 2 guests. ")
print(f"Please stay tuned for to see whether you will be able to attend.")

print(f"\nHere is the guest list:\n {guests}\n")
ex_guest = guests.pop(0).title()
print(ex_guest)
print(f"Sadly, {ex_guest}, we will not be able to enjoy the pleasure of your company.\n")

ex_guest = guests.pop(0).title()
print(ex_guest)
print(f"Sadly, {ex_guest}, we will not be able to enjoy the pleasure of your company.\n")

ex_guest = guests.pop(0).title()
print(ex_guest)
print(f"Sadly, {ex_guest}, we will not be able to enjoy the pleasure of your company.\n")

ex_guest = guests.pop(0).title()
print(ex_guest)
print(f"Sadly, {ex_guest}, we will not be able to enjoy the pleasure of your company.\n")

#Printing invite to last 2 remaining guests
print(f"We are pleased to be able to enjoy your company, {guests[0].title()}.\n")
print(f"We are pleased to be able to enjoy your company, {guests[1].title()}.\n")

#Using del method to remove final two names on list
#and printing confirmation that no names are left on the list

del guests[0]
print(guests)
print('')
del guests[0]
print(guests)
print('')

#End Program
print('')
print("END PROGRAM")
print('')