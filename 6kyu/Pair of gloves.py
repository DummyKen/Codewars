def number_of_pairs(gloves):
    gloves_dict = dict()
    count = 0
    lyst = []
    for glove in gloves:
        gloves_dict[glove] = gloves_dict.get(glove,0)+1
    for i,j in gloves_dict.items():
        if j >= 2:
            count += j//2
        else:
            continue
    return count
        
