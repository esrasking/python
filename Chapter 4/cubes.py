#20191203 
#Chapter 4.8: Cubes
#Make a list of the first 10 cubes. us a for loop to print each of the values.

#Start Program
print(f"\nSTART PROGRAM\n")

cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
    print(cube)

#End Program
print(f"\nEND PROGRAM\n")