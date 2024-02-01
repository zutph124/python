'''
In a file called extensions.py, implement a program that prompts the user for the name
of a file and then outputs that file’s media type if the file’s name ends, 
case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file’s name ends with some other suffix or has no suffix at all, 
output application/octet-stream instead, which is a common default.
'''

file = input("filename: ").strip().lower()

if file.endswith((".pdf", ".zip")):
    i = file.rfind(".")
    print("application/" + file[i+1:])

elif file.endswith(".txt"):
    i = file.rfind(".")
    print("text/" + file[0:i])

elif file.endswith((".gif", ".png")):
    i = file.rfind(".")
    print("image/" + file[i+1:])

elif file.endswith((".jpg", ".jpeg")):
    i = file.rfind(".")
    print("image/" + "jpeg")

else:
    print("application/octet-stream")

