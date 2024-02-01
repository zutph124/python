'''
we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.

percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
'''


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.removeprefix('$')
    return float(d)

def percent_to_float(p):
    p = p.removesuffix('%')
    p = float(p)/100           # calculate percentage
    return float(p)

main()
