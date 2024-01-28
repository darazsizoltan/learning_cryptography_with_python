from random import randint

ASCIIMAXNUMBER = 256


def encrpyt(text, key):
    cipher_text = ''

    # enumerate returns the index and a char itself
    for index, char in enumerate(text):
        key_index = key[index]

        # find the index of the current character and
        # create the modified index with the help of the key value and calculate the shifted position
        asiirepresentation = (ord(char) + key_index) % ASCIIMAXNUMBER

        # append the shifted characters to each other
        cipher_text = cipher_text + chr(asiirepresentation)

    return cipher_text


def decrpyt(cipher_text, key):
    plain_text = ''

    # enumerate returns the index and a char itself
    for index, char in enumerate(cipher_text):
        key_index = key[index]

        # find the index of the current character and
        # create the modified index with the help of the key value and calculate the shifted position
        asiirepresentation = (ord(char) - key_index) % ASCIIMAXNUMBER

        # append the shifted characters to each other
        plain_text = plain_text + chr(asiirepresentation)

    return plain_text


def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0, ASCIIMAXNUMBER - 1))
    return random


if __name__ == '__main__':
    message = 'Random message test_qwe%asd::EwqQQQ'
    sequence = random_sequence(message)
    print("Original message: %s" % message)
    cipher = encrpyt(message, sequence)
    print("Encrypted message: %s" % cipher)
    decrypted = decrpyt(cipher, sequence)
    print("Decrypted message: %s" % decrypted)
