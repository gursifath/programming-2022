def firstNonRepeatingCharacter(string):
    uniqueChars = dict()
    for char in string:
        uniqueChars[char] = uniqueChars.get(char, 0) + 1

    for idx, char in enumerate(string):
        if uniqueChars[char] == 1:
            return idx
    return -1