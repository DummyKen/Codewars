# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
def spin_words(sentence):
    # Your code goes here
    new_sentence = ""
    for word in sentence.split():
        if len(word) >= 5:
            new_sentence += word[::-1]
            new_sentence += " "
        else:
            new_sentence+=word
            new_sentence += " "
    
    return new_sentence[:-1]
