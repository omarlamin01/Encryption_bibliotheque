import string


def modulo(a, b):
    mod = a % b
    if mod < 0:
        mod += b
    return mod


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modulo_inverse(a, b):
    if pgcd(a, b) != 1:
        return None
    else:
        a = modulo(a, b)
        for x in range(1, b):
            if modulo(a * x, b) == 1:
                return x
        return 1


def cesar_encrypt(text, key):
    result = ""
    for i in range(len(text)):
        index = ord(text[i])
        new_index = modulo(index + key, 255)
        result += chr(new_index)
    return result


def cesar_decrypt(text, key):
    result = ""
    for i in range(len(text)):
        index = ord(text[i])
        new_index = modulo(index - key, 255)
        result += chr(new_index)
    return result


def affine_encrypt(text, key_a, key_b):
    result = ""
    for i in range(len(text)):
        index = ord(text[i])
        new_index = modulo(key_a * index + key_b, 255)
        result += chr(new_index)
    return result


def affine_decrypt(text, key_a, key_b):
    result = ""
    for i in range(len(text)):
        index = ord(text[i])
        new_index = modulo(modulo_inverse(key_a, 255) * (index - key_b), 255)
        result += chr(new_index)
    return result




