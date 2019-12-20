#20191219
#Chapter 6: Exercise 6.5 Rivers

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'usa',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print(f"------------------------------")

for river, country in rivers.items():
    print(river.title())

print(f"------------------------------")

for river, country in rivers.items():
    print(country.title())

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")