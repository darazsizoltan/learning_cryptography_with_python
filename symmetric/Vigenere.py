ASCIIMAXNUMBER = 256

def vigenere_encrypt(plain_text, key):
    cipher_text = ''
    key_index = 0

    for character in plain_text:

        # find the index of the current character and
        # create the modified index with the help of the key value and calculate the shifted position
        asiirepresentation = ord(character) % ASCIIMAXNUMBER + ord(key[key_index]) % ASCIIMAXNUMBER

        # append the shifted characters to each other
        cipher_text = cipher_text + chr(asiirepresentation)

        # increment the key_index, so we walk through the key
        key_index = key_index + 1

        # if the key_index reaches the end of the key length set it back to zero and start again from the first character of the key
        if key_index == len(key):
            key_index = 0

    return cipher_text


def vigenere_decrypt(cipher_text, key):
    plain_text = ''
    key_index = 0

    for character in cipher_text:

        # find the index of the current character and
        # create the modified index with the help of the key value and calculate the shifted position
        asiirepresentation = ord(character) % ASCIIMAXNUMBER - ord(key[key_index]) % ASCIIMAXNUMBER

        # append the shifted characters to each other
        plain_text = plain_text + chr(asiirepresentation)

        # increment the key_index, so we walk through the key
        key_index = key_index + 1

        # if the key_index reaches the end of the key length set it back to zero and start again from the first character of the key
        if key_index == len(key):
            key_index = 0

    return plain_text


if __name__ == '__main__':
    text = 'cryptography is quite IMPORTANT IN CRYPTOCURRENCIES'
    encrypted_text = vigenere_encrypt(text, 'ANIMAL')
    print(encrypted_text)
    print(vigenere_decrypt(encrypted_text, 'ANIMAL'))

