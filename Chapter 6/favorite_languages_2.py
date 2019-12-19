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
#End Program
print(f"\nEND PROGRAM\n")