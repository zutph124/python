'''
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format
and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals,
just like the song from Rent, without any and between words.
Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight
(i.e., 00:00:00) on that date. And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
'''

import re
import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    DoB = input("Date of Birth: ")
    try:
        year, month, day = validate(DoB)
        birthDate = date(int(year), int(month), int(day))
        todayDate = date.today()
        minutes = ((todayDate - birthDate) * 24 * 60)
        words = p.number_to_words(minutes.days, andword="")
        print(words.capitalize() + " minutes")
    except:
        sys.exit("Invalid date")

def validate(DoB):
    if re.search(r'^\d{4}-[0-9]+-[0-3][0-9]$', DoB):
        year, month, day = DoB.split("-")
        return year, month, day
    else:
        return None

if __name__ == "__main__":
    main()
