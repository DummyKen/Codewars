# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

def is_isogram(string):
    #your code here
    result = True
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            result = False
    return result
