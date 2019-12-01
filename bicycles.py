#20191201 
#Chapter 3: Bicycles

#Start Program
print(" ")

bicycles = ['trek','bmx','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0])
print(f"{bicycles[0].title()}\n")

#Index positions start at 0 not 1
print(bicycles[1].title())
print(bicycles[3].title())
print(" ")

#This prints the last item in the list
print(bicycles[-1])

#This prints the second to last item in the list
print(bicycles[-2])
print(" ")

#This creates a message from an individual item in the list
message=f"My first bicyle was a {bicycles[2].title()}.\n"
print(message)

#End Program
print(" ")