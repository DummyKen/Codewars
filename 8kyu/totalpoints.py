# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.
# For example: ["3:1", "2:2", "0:1", ...]
# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

def points(games):
    total = 0
    for scores in games:
        if scores[0] > scores[2]:
            total += 3
        elif scores[0] == scores[2]:
            total += 1
        else:
            continue
    return total
