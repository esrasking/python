#20191209
#Chapter 4: Buffet

#Start Program
print(f"\nSTART PROGRAM\n")

#Create a tuple of five basic buffet foods
buffet = ('salad','soup','pasta','burger','pizza')
print(f"\nHere are the five buffet choices:\n")
for food in buffet:
    print(f"\t{food}")

#the following is a FORCED ERROR
#buffet[1]= 'sandwich'
#print(f"\nHere are the modified buffet foods:\n")
#for food in buffet:
#    print(f"\t{food}")

#Now I have to modify the menu and write a for loop to list the items
buffet=('green salad','sushi','soup','pasta','pizza')
print(f"\nHere is the revised menu:\n")
for food in buffet:
    print(f"\t{food}")

#End Program
print(f"\nEND PROGRAM\n")
