# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    summ = 0
    mulist = list()
    for i in range(number):
        if i % 15 == 0:
            mulist.append(i)
        elif i % 5 == 0:
            mulist.append(i)
        elif i % 3 == 0:
            mulist.append(i)
        else:
            if i < 0:
                summ = 0
            else:
                continue
    return summ+sum(mulist)
