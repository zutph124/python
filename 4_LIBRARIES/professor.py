'''
In a file called professor.py, implement a program that:

# Prompts the user for a level,
    . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

        import random

        def main():
            ...

        def get_level():
            ...

        def generate_integer(level):
            ...

        if __name__ == "__main__":
            main()
'''


from random import randrange

def main():
    print("hello")
    global level
    level = get_level()
    x, y = generate_integer()

    score = 0
    bad   = 0

    for n in range(10):

        z = x + y
        z = str(z)
        answer = input(f"{x} + {y} = ")

        if answer != z :
            for abc in range(3):
                print("EEE")

                if abc == 2:
                    print(f"{x} + {y} = {z}")
                    bad += 1
                    # print("b ",bad)
                    break
                answer = input(f"{x} + {y} = ")

        elif answer == z :
            score += 1
            # print("s ",score)
            pass
        x, y = generate_integer()
    print("Score: ", score)
    bad   = 0


def get_level():

   while True:
    try:
        level = int(input("Level: "))
        if level not in [1, 2, 3]:         # If the user does not input 1, 2, or 3, the program should prompt again.
            continue
    except ValueError:
        continue
    return level


def generate_integer():

    if level == 1:                          # 0-9
        x = randrange(10)
        y = randrange(10)

    elif level == 2:                        # 10-99
        x = randrange(10,100)
        y = randrange(10,100)

    else:                                   # 100-999
        x = randrange(100,1000)
        y = randrange(100,1000)

    return x, y

if __name__ == "__main__":
    main()
