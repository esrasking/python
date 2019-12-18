#20191218
#Chapter 6: Exercise 6.3 Glossary

#       append()    ... appends a value to the end of a list, ex: list_name.append('value')
#       insert()    ... inserts a value to a specific position 
#                       ex: list_name.insert(index_no,'value')
#       del         ... deletes a value by position number ex: del list_name[2]
#       pop()       ... temporarily removes a value at the end if left blank, or by index_no
#                       ex: list_name.pop(index_no)
#       remove()    ... removing an item by value ex: list_name.remove('value')

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

terms = {
    'append': "appends a value to the end of a list, ex: list_name.append('value')",
    'insert': "inserts a value to a specific position, ex: list_name.insert(index_no,'value')",
    'del': "deletes a value by position number ex: del list_name[2]",
    'pop': "temporarily removes a value at the end if left blank, or by index_no",
    'remove': "removing an item by value ex: list_name.remove('value')"
}

for key in terms:

    print(f"{key}:\n\t {terms[key]}\n")

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")