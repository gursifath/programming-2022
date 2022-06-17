def runLengthEncoding(string):
    count = 1
    encodedString = []
    for idx in range(1, len(string)):
        if string[idx-1] != string[idx] or count == 9:
            encodedString.append(str(count))
            encodedString.append(string[idx-1])
            count = 1
        else:
            count += 1
            
    encodedString.append(str(count))
    encodedString.append(string[-1])
    return ''.join(encodedString)