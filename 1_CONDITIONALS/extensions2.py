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
i = len(file)
suffix = file.rfind(".")
type = file[suffix+1:]
#print(type)              d e b u g g e r

match type: 
    case "pdf" | "zip":
        print("application/" + type)

    case "txt":
        print("text/" + type)

    case "gif" | "png": 
        print("image/" + file[suffix+1:])

    case "jpg" | "jpeg":
        print("image/" + "jpeg")

    case _:
        #else:
        print("application/octet-stream")
