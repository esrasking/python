#20191120
#Chapter 2: Strippping Names

#Start Program
print(" ")

name1a = "   AliCia KeyS   "
name2a = "   AmY WinehouSe   "
name3a = "   ArEtHA fRanKliN   "

print("Here are the original entered names:\n")
print(name1a)
print(name2a)
print(name3a)

print(" ")

print("Here are the names formatted and stripped of left whitespace:\n")
name1b = name1a.lstrip()
name2b = name2a.lstrip()
name3b = name3a.lstrip()

print(name1b.title())
print(name2b.title())
print(name3b.title())

print(" ")

#Repeat of original values entered
print("Here are the original names again:\n")
print(f"{name1a}\n{name2a}\n{name3a}\n")

#Printing of formatted names stipped of right (but not left) whitespace
print("Here are the names formatted and stripped of only right whitespace:\n")
name1c = name1a.rstrip()
name2c = name2a.rstrip()
name3c = name3a.rstrip()

print(f"{name1c.title()}\n{name2c.title()}\n{name3c.title()}\n")

#Printing of formatted names stripped of left and right whitespace
print("Here are the names formatted, indented and stripped of left and right whitespace\n")
print(f"\t{name1a.strip().title()}\n\t{name2a.strip().title()}\n\t{name3a.strip().title()}")






#End Program
print(" ")