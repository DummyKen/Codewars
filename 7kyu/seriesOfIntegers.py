# Write a function generateIntegers/generate_integers that accepts a single argument n/$n and generates an array containing the integers from 0 to n/$n inclusive.

def generate_integers(n):
    integers = []
    i = 0
    while i <= n:
        integers.append(i)
        i+=1
    return integers
