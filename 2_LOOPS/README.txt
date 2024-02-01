Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split, which separates a str into a sequence of values, all of which can be assigned to variables at once. 
For instance, if expression is a str like 1 + 1, then
x, y, z = expression.split(" ")
will assign 1 to x, + to y, and 1 to z.
'''
