# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    # Bust a move right here
#     put them into list and sort
    numbers = list()
    for i in str(num):
        numbers.append(int(i))
#         sort
    numbers.sort()
#     reverse
    numbers.reverse()
    str1 = ''
#     convert to string
    for j in numbers:
        str1 += str(j)
    return int(str1)
    
