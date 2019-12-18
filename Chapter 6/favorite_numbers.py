#20191218
#Chapter 6: Exercise 6.2 Favorite Numbers

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

favorite_numbers = {
    'jason': 4,
    'liz': 2,
    'ana zoe': 13,
    'dj': 10,
    'oma': 5
}

for name in favorite_numbers:
    favorite_number = favorite_numbers[name]

    print(f"{name.title()}'s favorite number is {favorite_number}.")

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")