#20191203
#Chapter 4: Squares

#Start Program
print(f"\nSTART PROGRAM\n")

#Remember, always remember to include a colon when defining an for loop

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    print(square)

#Making the code above more concise by eliminating temp variable
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print('')

#Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
print('')

#Using list comprehension to automate the appending of values
squares = [value**2 for value in range(1,11,)]
print(squares)

#End Program
print(f"\nEND PROGRAM\n")