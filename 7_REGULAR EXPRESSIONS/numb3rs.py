'''
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str
and then returns True or False, respectively, if that input is a valid IPv4 address or not.
'''

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip)
    if matches:
        ipnum = ip.split('.')
        ipnum = [int(n) for n in ipnum]    # convert to integers BEFORE you go to For Loop

        for n in ipnum:
            #print("n : ", n)
            if n < 0 or n > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
