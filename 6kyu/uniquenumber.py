# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    # your code here
    n = 0
    diction = dict()
    for i in arr:
        diction[i] = diction.get(i,0)+1
    for j,k in diction.items():
        if k == 1:
            n = j
        else:
            continue
    
    return n   # n: unique integer in the array
