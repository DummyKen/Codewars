# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    #your code here
    empty = ''
    copy = string
    nonrepeat = []
    if string == empty:
        return empty
    string = string.casefold()
    
    for i in string:
        if string.count(i) > 1:
            continue
        elif string.count(i) == 1:
            nonrepeat.append(i)
            
    if len(nonrepeat) == 0:
        return empty
    else:
        if nonrepeat[0].lower() in copy:
            return nonrepeat[0].lower()
        else:
            return nonrepeat[0].upper()
