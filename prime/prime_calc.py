# File: prime_calc.py
# Created by: Michael Napoli
# Created on: 5/20/2021

# Purpose: Program that iterates until stopped, calculating
#          whether the current number is prime.

def is_prime(n):
    for i in range(2, int(n/2)):
        if (n % (i+1)) == 0:
            return False
    return True

# Create infinite loop
n = 1
while True:
    if is_prime(n):
        print(n)
    n += 2
