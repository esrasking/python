#20200105
#Chapter 6: Exercise 6.7 People

#START PROGRAM
print(f"\nSTART PROGRAM")
print("--------------------\n")

#Recalling the info from page 99. 
##Storing the information of someone I know in a dictionary.
#person = {'first_name': 'georgia','last_name': 'blackwell','age': 40,'city':'frankfurt'}
#print(person['first_name'])
#print(person['last_name'])
#print(person['age'])
#print(person['city'])

person = {
    'friend_1' : {
        'first' : 'georgia',
        'last' : 'blackwell',
        'age' : 40,
        'location' : 'frankfurt',
    },
    'friend_2' : {
        'first' : 'jason',
        'last' : 'brown',
        'age' : 43,
        'location' : 'ellicott city',
    },
    'friend_3' : {
        'first' : 'caroline',
        'last' : 'van zoggel',
        'age' : 50,
        'location' : 'christchurch',
    },

}

for friend, friend_info in person.items():
    full_name = friend_info['first'] + " " + friend_info['last']
    print(f"Full Name: {full_name.title()}")
    print(f"Age: {friend_info['age']}")
    print(f"Location: {friend_info['location'].title()}\n")


print("--------------------\n")
#END PROGRAM
print(f"END PROGRAM")