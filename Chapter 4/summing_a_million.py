#20191203 
#Chapter 4.5: Summing a Million

#Start Program
print(f"\nSTART PROGRAM\n")

#The code below shows the sum of values 1-5. 
print(f"Here is a quick test that the sum of the range values works:\n")
values = list(range(1,6,1))
print(sum(values))
print('')

#The code below executes the sum of values up to and including 1,000,000.
values = list(range(1,1000001,1))
print(sum(values))

#End Program
print(f"\nEND PROGRAM\n")