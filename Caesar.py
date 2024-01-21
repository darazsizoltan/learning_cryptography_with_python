import matplotlib.pylab as plt
KEY = 3
ASCIIMAXNUMBER = 256


def caesar_encrypt(plain_text, key):
    cipher_text = ''

    # make it upper case because so a match can be found in the given set of characters stored in ALPHABET variable
    plain_text = plain_text.upper()

    # go through all the possibilities
    for c in plain_text:
        # find the index of the current character
        asiirepresentation = ord(c)
        # create the modified index with the help of the key value and calculate the shifted position
        asiirepresentation = (asiirepresentation + key) % ASCIIMAXNUMBER
        # append the shifted characters to each other
        cipher_text = cipher_text + chr(asiirepresentation)
    return cipher_text


def caesar_decrypt(cipher_text, key):
    plain_text = ''

    for c in cipher_text:
        # find the index of the current character
        asiirepresentation = ord(c)
        # create the modified index with the help of the key value and calculate the shifted position
        asiirepresentation = (asiirepresentation - key) % ASCIIMAXNUMBER
        # append the shifted characters to each other
        plain_text = plain_text + chr(asiirepresentation)
    return plain_text


def crack_caesar(cipher_text):

    for key in range(ASCIIMAXNUMBER):
        plain_text = caesar_decrypt(cipher_text, key)
        print('With key %s, the result is: %s ' % (key, plain_text))


if __name__ == '__main__':
    encrypted = caesar_encrypt('Hello World', KEY)
    decrypted = caesar_decrypt(encrypted, KEY)
    print('Encrypted: ', encrypted)
    # print('Decrypted: ', decrypted)
    crack_caesar(encrypted)
