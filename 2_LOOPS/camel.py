'''
In a file called camel.py, implement a program that prompts the user for the name of a 
variable in camel case and outputs the corresponding name in snake case.

preferredFirstName --> preferred_first_name
'''
charC = ""
charS = ""
s = input("camelCase: ")
for char in s:
    charC += char
    if char.isupper():
        charS += "_" + char.lower()
    else: charS += char
print("camelCase: ", charC)
print("snake_case:", charS)
