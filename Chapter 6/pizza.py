#20200104
#Chapter 6

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")


#Storing information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese']
}

#Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t" + topping)

#IMPORTANT: When you have a long string that you need to break up, choose 
#a point to break the line, indent, and then continue with an open 
#quotation mark. The ouput will still print on one line.

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")