def caesarCipherEncryptor(string, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cipher = []
    for char in string:
        new_char = alphabets[(alphabets.index(char) + key) % 26]
        cipher.append(new_char)

    return ''.join(cipher)
