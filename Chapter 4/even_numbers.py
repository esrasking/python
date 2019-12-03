#20191203   
#Chapter 4: Even Numbers

#Starting to work with range()

#Start Program
print(f"\nSTART PROGRAM\n")

for value in range(1,5):

    print(value)
#Using range() to define a list of numbers
numbers = list(range(1,6))
print(numbers)
print('')

#In the example below, you start at the value 2 and add 2 to the value until you reach
#or surpass the value 11.
even_numbers= list(range(2,11,2))
print(even_numbers)

#End Program 
print(f"\nEND PROGRAM\n")