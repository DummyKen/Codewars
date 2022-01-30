# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
def duplicate_count(text):
    # Your code goes here
    dup = dict()
    count = 0
    for i in text:
        if i.isalpha():
            i = i.lower()
            dup[i] = dup.get(i,0)+1
        else:
            dup[i] = dup.get(i,0)+1
    
    for j,k in dup.items():
        if k > 1:
            count +=1
    return count
     
