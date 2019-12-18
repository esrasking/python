#20191213
#Chapter 6: Dictionaries

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(f"------------------------------")


#Assessing the values in a Dictionary
new_points = alien_0['points']
print(f"Well done! You've just earned {new_points} points!")
print(f"------------------------------")

#Setting x and y coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print(f"------------------------------")

#Modifying values in a Dictionary
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print(f"------------------------------")

#Removing Key-Value Pairs
#Using the del statement deletes the key-value pair permanently.
alien_0 = {'color': 'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)
print(f"------------------------------")


#End Program
print(f"\nEND PROGRAM\n")