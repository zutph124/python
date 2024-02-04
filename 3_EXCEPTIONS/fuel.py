# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
#
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


while True:
   x, y  = input("Fraction: ").split('/')
   x = int(x)
   y = int(y)

   try:
       dec_n = round(x/y,2)
       if x > y: continue
   except ValueError: pass
   except ZeroDivisionError: pass

   else:
       break

#
# no need to print out percentages if fuel gauge is full or empty
#
if dec_n <=  1/100: print("E")
if dec_n >= 99/100: print("F")
percentage = f"{dec_n:.0%}"

#
# print out percentages if fuel gauge is neither full or empty
#
if (dec_n > 1/100 and dec_n < 99/100): print(percentage)
