# Write a function that doubles every second integer in a list, starting from the left.
def double_every_other(lst):
    i= 1
    while i<len(lst):
        lst[i]*=2
        i+=2
    return lst
