#20191217
#Chapter 6: Using get() to access values

#Start Program
print(f"\nSTART PROGRAM\n")
print(f"------------------------------")

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#Remember, if you use get() to access a value and that value doesn't exist,
#then you have to define a default value ... like above. Otherwise, Python
#will return None as a value.

print(f"------------------------------")
#End Program
print(f"\nEND PROGRAM\n")