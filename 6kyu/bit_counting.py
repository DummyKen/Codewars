# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    binary = bin(n).replace("0b", "")
    lyst = []
    for i in binary:
        lyst.append(int(i))
    return lyst.count(1)
