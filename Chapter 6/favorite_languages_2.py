#20191218
#Chapter 6:

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#Creating a loop through each key-value pair in the dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print(f"------------------------------")

#Looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())
print(f"------------------------------")

#Now we want to print tailored msgs for specific friends.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print(f"------------------------------")

#Looking for a value not in the dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

if 'erin' not in favorite_languages.keys():
    print(f"Erin, please take our poll.")

print(f"------------------------------")

#Looping through a dictionary's keys is a particular order.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print(f"------------------------------")

#Looping through all the values in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())
print(f"------------------------------")

#Looking for unique values in a dictionaries by using set method.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("The following languages have been mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())
print(f"------------------------------")

#End Program
print(f"\nEND PROGRAM\n")