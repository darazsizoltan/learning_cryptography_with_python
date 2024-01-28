import binascii

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# private key for AES (must be 16 bytes)
# byte representation of the key word
# if not random is used ask for a password and (SHA) hash it to 16 bytes
keyword = get_random_bytes(16)

cipher = AES.new(keyword, AES.MODE_CBC)
cipher_iv = cipher.iv
print('Hexadecimal representation of IV (binary data): ', binascii.hexlify(cipher_iv))

# Padding might be needed if the plain text is not divisible by 128 bits or 16 bytes
# Because each 16 bytes will be split into 4 blocks
plain_text = b'This will be encrypted I hope'
plain_text_after_padding = pad(plain_text, AES.block_size)
cipher_text = cipher.encrypt(plain_text_after_padding)
print('Plain text in byte representation: ', plain_text)
print('Plain text after padding (3 extra bytes are needed): ', plain_text_after_padding)
print('Plain text after padding and encrypted by AES: ', cipher_text)


# For decryption, we must use the same initialization vector to get back the originally encrypted message
decrypt = AES.new(keyword, AES.MODE_CBC, cipher_iv)
decrpyted_before_unpad = decrypt.decrypt(cipher_text)
decrypted_after_unpad = unpad(decrpyted_before_unpad, AES.block_size)
print('Original text after decrpyt: ', decrpyted_before_unpad)
print('Original text after decrpyt and unpad: ', decrypted_after_unpad)
