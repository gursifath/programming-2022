def generateDocument(characters, document):
    if document == "":
        return True

    charCount = dict()
    for char in characters:
        charCount[char] = charCount.get(char, 0) + 1

    for element in document:
        if element not in charCount or charCount[element] == 0:
            return False
        charCount[element] -=1 

    return True