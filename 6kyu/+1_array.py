# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

#     the array can't be empty
#     only non-negative, single digit integers are allowed

# Return nil (or your language's equivalent) for invalid inputs.
# Examples

# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

# [4, 3, 2, 5] would return [4, 3, 2, 6]
def up_array(arr):
    #your code here
    if arr == []:
        return None
    else:
        str1 = ""
        result = []
        for i in arr:
            if i < 0:
                return None
            elif i > 9:
                return None
            else:
                str1 += str(i)
            num = int(str1)+1
        for j in str(num):
            result.append(int(j))
        return result
        
