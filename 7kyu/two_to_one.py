# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    # your code
    a = []
    result = ""
    for i in a1:
        if i not in a:
            a.append(i)
    for j in a2:
        if j not in a:
            a.append(j)
    a.sort()
    for k in a:
        result += k
    
    return result
