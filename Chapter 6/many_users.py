#20200104
#Chapter 6: Nesting dictionaries within dictionaries

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

users = {
    'aeinstein' : {
        'first': 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"Full Name: {full_name.title()}")
    print(f"Location: {location.title()}")




print(f"\n------------------------------")
#End Program
print(f"\nEND PROGRAM\n")