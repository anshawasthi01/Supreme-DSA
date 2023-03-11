def getLength(name):
    length = 0
    i = 0
    # while name[i] != '\0':
    for i in name:
        length += 1
    return length
    
print(getLength(['A','N','S','H']))