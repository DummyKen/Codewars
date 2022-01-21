#Find the shortest word in a given sentence

def find_short(s):
    shortest = None
    for word in s.split():
        if shortest == None:
            shortest = word
        elif len(shortest) > len(word):
            shortest = word
    return len(shortest)
