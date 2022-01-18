#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
def get_middle(s):
    #your code here
    n = len(s)
    mid_index = 0
    if n % 2 != 0:
        mid_index = int(((n+1)/2)-1)
        return s[mid_index]
    else:
        index = int((n/2)-1)
        mid_index = int(n/2)+1
        return s[index:mid_index]
