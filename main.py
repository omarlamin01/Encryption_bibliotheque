from app import cesar_encrypt, cesar_decrypt, affine_encrypt, affine_decrypt, vigenere_encrypt, vigenere_decrypt

message = "Hello World"
key = "music"

print(vigenere_encrypt(message, key))
print(vigenere_decrypt(vigenere_encrypt(message, key), key))
