#20191201
#Chapter 3.5: Changing Guest List

#Start Program
print('')
print("START PROGRAM")
print('')

#Original program from exercise 3.4
guests=['dave matthews','albert einstein','robin williams']
print(f"{guests}\n")
print(f"These are the guests I'd like to individually invite to dinner:\n\t{guests[0].title()}, \n\t{guests[1].title()}, \n\t{guests[2].title()}.\n")
print(f"Dear {guests[0].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[1].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[2].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")

#Now, I picked a guest to remove and choose another to substitute and then reissued the invites
print(f"Regretfully, Mr. {guests[1].title()} will be able to attend.\n")
new_guest = 'dr. seuss'
guests.remove('albert einstein')

#Here is the new list
print(f"\n{guests}\n")

#Inserting the new guest into the list
guests.insert(1,new_guest)
print(guests)
print('')

#Reissuing the invites to people still on the list
print(f"These are the guests I'd like to individually invite to dinner:\n\t{guests[0].title()}, \n\t{guests[1].title()}, \n\t{guests[2].title()}.\n")
print(f"Dear {guests[0].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[1].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")
print(f"Dear {guests[2].title()}, we would like to cordially invite you to our next roundtable dinner. Please RSVP by Friday.\n")

#End Program
print('')
print("END PROGRAM")
print('')