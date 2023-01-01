from app import cesar_encrypt, cesar_decrypt

message = " @#%$^&*() _+{} |:<>?~`"

print(cesar_encrypt(message, 5))
print(cesar_decrypt(cesar_encrypt(message, 5), 5))