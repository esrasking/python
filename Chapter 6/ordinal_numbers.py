#20191213
#Chapter 5: 5.11 Ordinal Numbers

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------\n")

o_numbers = [1,2,3,4,5,6,7,8,9]
print(o_numbers)
print(f"------------------------------\n")


for o_nbr in o_numbers:
    if o_nbr == 1:
        print(f"{o_nbr}st")
    elif o_nbr == 2:
        print(f"{o_nbr}nd")
    elif o_nbr == 3:
        print(f"{o_nbr}rd")
    else:
        print(f"{o_nbr}th")

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")