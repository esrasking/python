#20191202 
#Chapter 3.10: Every Function

#This program should serve as a quick reference of list manipulating methods
#as discussed in Chapter 3. The methods covered here are:
#       append()    ... appends a value to the end of a list, ex: list_name.append('value')
#       insert()    ... inserts a value to a specific position 
#                       ex: list_name.insert(index_no,'value')
#       del         ... deletes a value by position number ex: del list_name[2]
#       pop()       ... temporarily removes a value at the end if left blank, or by index_no
#                       ex: list_name.pop(index_no)
#       remove()    ... removing an item by value ex: list_name.remove('value')
#       sort()      ... sorting permanently ex: list_name.sort(reverse = True) for descending 
#                       left blank for ascending ex: list_name.sort()
#       sorted()    ... sorting temporarily ex: sorted(list_name, reverse = True) for descending
#                       left blank for ascending
#       reverse()   ... reversing the order of a list permanently, ex: list_name.reverse()
#       len()       ... determining the length of a list, ex: len(list_name)

#I'll use the list from ch3_seeing_the_world.py

#Start Program
print(f"\nSTART PROGRAM\n")

#Establishing initial list
vacation = ['paris','london','barcelona','cape town','seoul']
print(f"Here is the starting list\n\t")
print(vacation)

#append()
vacation.append('rome')
print(vacation)

#insert()
vacation.insert(1,'berlin')
print(vacation)

#del
del vacation[1]
print(vacation)

#pop()
vacation.pop(1)
print(vacation)

#remove
vacation.remove('rome')
print(vacation)

#sort()
vacation.sort(reverse=True)
print(vacation)

#sorted()
print(sorted(vacation))
print(vacation)

#reverse()
vacation.reverse()
print(vacation)

#len()
len(vacation)
print(len(vacation))

#End Program
print(f"\nEND PROGRAM\n")