from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# key must be 64 bits ( 8 bytes )
#   ask a password from a user and use the first 8 bytes
# byte representation of the key word
keyword = b'qweasdqw'

# DES will generate the initialization vector automatically, or we can pass an iv as a param.
# Initialization vector is an arbitrary number also called nonce (number used once).
# We use an IV in a cryptographic algorithm as a starting state,
# adding this to a cipher to hide patterns in the encrypted data.
# This helps avoid the need to re-issue a new key after each invocation.
encrypt = DES.new(keyword, DES.MODE_CBC)
iv = encrypt.iv

# Padding maybe needed to be used because of the plain text is not divisible by the block size
plain_text = b'Number of bytes is not divisible by 8'
plain_text_after_padding = pad(plain_text, DES.block_size)
cipher_text = encrypt.encrypt(plain_text_after_padding)
print('Plain text in byte representation: ', plain_text)
print('Plain text after padding: ', plain_text_after_padding)
print('Plain text after padding and encrypted by DES: ', cipher_text)

# For decryption, we must use the same initialization vector to get back the originally encrypted message
decrypt = DES.new(keyword, DES.MODE_CBC, iv)
decrpyted_before_unpad = decrypt.decrypt(cipher_text)
decrypted_after_unpad = unpad(decrpyted_before_unpad, DES.block_size)
print('Original text after decrpyt: ', decrpyted_before_unpad)
print('Original text after decrpyt and unpad: ', decrypted_after_unpad)
