#20191210
#Chapter 5: If Then Else Conditional Statements

#Start Program
print(f"\nSTART PROGRAM\n")

#Using a single ( = ) sign is a statement. You're setting one thing equal to another
#Using a double ( == ) sign is more of a question. Is one thing equal to the specified value?

#Setting an if statement to print bmw in all caps.
#Remember to use a colon ( : ) to define loops and conditional tests
cars = ['audi','bmw','toyota','subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())


#I ran the code below in a jupyter notebook since I was trying to check the values
cat = 'parker'
cat == 'parker'

#Checking for inequality ( != ) ... this symbol means not equal to
requested_topping = 'mushroom'
if requested_topping!= 'anchovies':
    print (f"\nHold the anchovies!\n")

#End Program
print(f"\nEND PROGRAM\n")