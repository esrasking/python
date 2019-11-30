#20191129
#Chapter 2: Changing case in a String with Methods

print (" ")

name = "ada lovelace"
print(name.title())

print (" ")

name="Ada Lovelace"
print(name.lower())
print(name.upper())

print (" ")

#Using Variables in Strings

first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print (full_name)

print (f"Hello, {full_name.title()}!")
print (" ")

#Using an f-string to compose a message
message = f"Hello, {full_name.title()}! You're a cheeky monkey."
print (message)
print (" ")

#Adding Whitespace to Strings with Tabs or Newlines
#Adding Tab Whitespace
print("Python")

print("\tPython")

#Adding Newline Whitespace
print("Languages:\nPython\nC\nJavaScript\n")

#Combining Tabs and Newline Whitespace
print("Languages:\n\tEnglish\n\tGerman\n\tSpanish\n")

#Stripping Hanging Right-side Whitespace
favorite_language = 'python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print (favorite_language)

#Stripping Hanging Left-Side Whitespace
favorite_language = ' Italian'
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)

#Stripping Hanging Left and Right Whitespace
favorite_language = ' German '
favorite_language = favorite_language.strip()
print(favorite_language)
