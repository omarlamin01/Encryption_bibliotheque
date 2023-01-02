from app import cesar_encrypt, cesar_decrypt, affine_encrypt, affine_decrypt

message = "Hello World"

print(affine_encrypt(message, 23, 19))
print(affine_decrypt(affine_encrypt(message, 23, 19), 23, 19))