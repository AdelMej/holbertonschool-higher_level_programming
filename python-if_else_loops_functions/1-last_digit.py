#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10 if number >= 0 else -(abs(number) % 10)
print(
    f"Last digit of {number} is {lastdigit} " +
    (
        "and is greater than 5" if lastdigit > 5
        else "and is 0" if lastdigit == 0
        else "and is less than 6 and not 0"
    ), end="\n"
)
