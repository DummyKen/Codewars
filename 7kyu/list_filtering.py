# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def filter_list(l):
    strings,numbs = [],[]
    for i in l:
        if type(i) == str:
            strings.append(i)
        else:
            numbs.append(i)
    return numbs
