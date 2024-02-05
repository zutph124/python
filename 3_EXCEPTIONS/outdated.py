'''
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:

[
    "January",
    ..........,
    "December"
]
Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days.
'''


mthlist = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
           ]

while True:

    str = input("Date: ").strip()

    try:
        if "/" in str:                           # if (str1.index('/')) > 0:  can fail with ValueError
            mm, dd, yyyy = str.split('/')        # mm/dd/yyyy
            mm   = int(mm)
            dd   = int(dd)

            if (mm < 12) and (dd < 31):
                mm  = (f"{mm:02}")                    # change to strings before you print
                dd  = (f"{dd:02}")                    # change to strings before you print
                newdate = yyyy + "-" + mm + "-" + dd  # elements must all be string type
                print(newdate)
                exit()

        elif  "," in str:
            mm, dd, yyyy = str.split(' ')             # MONTH Day, Year

            if mm in mthlist:                         # check month
                mm = mthlist.index(mm)
                mm = int(mm)
                mm += 1
                mm = (f"{mm:02}")                     # changes to string
                dd = dd.strip(',')
                dd = int(dd)
                if (dd < 31):
                    dd  = (f"{dd:02}")                # changes to string
                    newdate = yyyy + "-" + mm + "-" + dd  # elements must all be string type
                    print(newdate)
                    exit()

    except EOFError:
        break
    except ValueError:
        continue
