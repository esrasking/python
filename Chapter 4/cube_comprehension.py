#20191203 
#Chapter 4.9: Odd Comprehension
#Use a list comprehension to generate a list of the first 10 cubes.

#Start Program
print(f"\nSTART PROGRAM\n")

#Using list comprehension to automate the appending of values
cubes = [value**3 for value in range(1,11,)]
print(cubes)

#End Program
print(f"\nEND PROGRAM\n")