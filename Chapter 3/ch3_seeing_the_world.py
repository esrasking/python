#20191202
#Chapter 3.8: Seeing the World

#Start Program
print(f"\nSTART PROGRAM\n")

vacation = ['paris','london', 'nyc', 'amsterdam','frankfurt']
#Printing the list in original order
print(f"\nOriginal List\t")
print(vacation)

#Printing the list with a temporary ascending sort
print(f"\nTemp Sorted List\t")
print(sorted(vacation))

#Printing original list again
print(f"\nOriginal List Again\t")
print(vacation)

#Printing and sorting the list in descending order
print(f"\nList in Temp Descending order\t")
print(sorted(vacation,reverse=True))
print(vacation)

#Permantmently reversed the order of the list
vacation.reverse()
print(vacation)

#Restoring the order of the list by using reverse again
vacation.reverse()
print(vacation)

#Permamently sorting the list alphabetically
vacation.sort()
print(vacation)

#Permanently sorting the list alphabetically in descending order
vacation.sort(reverse=True)
print(vacation)

#End Program
print(f"\nEND PROGRAM\n")
