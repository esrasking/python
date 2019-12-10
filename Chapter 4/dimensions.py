#20191209
#Chapter 4: Tuples

#Start Program
print(f"\nSTART PROGRAM\n")

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0]=250 ... FORCED ERROR
print(f"\nHere are the dimnesions of the rectangle\n")
for dimension in dimensions:
    print(dimension)

#Writing over a tuple
dimensions = (400,80)
print(f"\nHere are the original dimensions:\n")
for dimension in dimensions:
    print (dimension)

dimensions = (500,25)
print(f"\nHere are the modified dimensions:\n")
for dimension in dimensions:
    print(dimension)

#End Program
print(f"\nEND PROGRAM\n")