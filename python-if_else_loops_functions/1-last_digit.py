#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit_signed = -last_digit
else:
    last_digit_signed = last_digit


if last_digit_signed == 0:
    print(f"Last digit of {number} is {last_digit_signed} and is 0")
elif last_digit_signed > 5:
    print(
        f"Last digit of {number} is {last_digit_signed} "
        "and is greater than 5")
else:
    print(
        f"Last digit of {number} is {last_digit_signed} "
        "and is less than 6 and not 0")
