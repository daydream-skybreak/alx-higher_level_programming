#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
while True:
    if num < 10 and num > -10:
        break
    num %= 10

print(f"Last digit of {number} is {num} and", end=" ")

if num > 5:
    print("is greater than 5")
elif num == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
