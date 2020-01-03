#20191219
#Chapter 6:

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

#Making a list of dictionaries
alien_0 = {'color':'green','points': 5}
alien_1 = {'color':'yellow','points': 10}
alien_2 = {'color':'red','points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print(f"------------------------------")

#Making an empty list to store aliens
aliens = []

#Make aliens green

for alien in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#Now changing the properties for three of the aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens were created
print(f"The total number of aliens generated is {len(aliens)}.")

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")
