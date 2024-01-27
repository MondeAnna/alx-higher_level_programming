#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit = last_digit if number >= 0 else -last_digit

if not last_digit:
    observation = "0"
elif last_digit < 6:
    observation = "less than 6 and not 0"
else:
    observation = "greater than 5"

print(f"Last digit of {number} is {last_digit} and is {observation}")
