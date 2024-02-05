"""
In a file called grocery.py, implement a program that prompts the user for items,
one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
"""


#dictionary
mylist = {}

while True:
    try:
        str = input().upper()              # convert to UPPERCASE
        if str in mylist:
            mylist[str] = mylist[str] + 1
        else:
            mylist[str] = 1
    except EOFError:
        mylist = dict(sorted(mylist.items())) # dictionary sorted
        for i in mylist:
            print(mylist[i], i)
        break

