from app import *

message = "Hello World"
key = "music"

print(affine_encrypt(message, 23, 19))
print(affine_decrypt(affine_encrypt(message, 23, 19), 23, 19))
