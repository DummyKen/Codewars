# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
def array_diff(a, b):
    #your code here
    result=[]
    for i in a:
        if i not in b:
            result.append(i)
    return result
