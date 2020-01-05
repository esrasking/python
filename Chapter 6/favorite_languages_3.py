#20200104
#Chapter 6: Continuing a list in a dictionary

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

favorite_languages = {
    'jen' : ['python','ruby'],
    'sarah' : ['c'],
    'edward' : ['python','go'],
    'phil' : ['python','haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"{language.title()}")
print(f"\n------------------------------")
#End Program
print(f"\nEND PROGRAM\n")