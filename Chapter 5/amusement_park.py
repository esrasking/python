#20191210
#Chapter 5: if-elif-else

#Start Program
print(f"\nSTART PROGRAM\n")

age = 12

print(f"The age you entered is {age}.\n")

if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#Below is the same program but simplified.
print(f"\n------------------------------------\n")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price =40
print(f"The age you entered is {age}.")
print(f"Your admission price is {price}.\n")
# The line of code below shows an older method of the print statement
# without using the f (format) method.
print("\nYour admission cost is $" + str(price)+".\n")

#Adding a senior discount with additional elif statements
print(f"\n------------------------------------\n")
age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"The age you entered is {age}.")
print(f"Your admission price is {price}.\n")


#End Program
print(f"\nEND PROGRAM\n")