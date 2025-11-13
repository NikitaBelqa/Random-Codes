import random
alphabet = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
message = "lambda"#input("Your message: ").lower()

def encrypt(word):
    return "".join([alphabet[alphabet.find(i) + 1] for i in word])

def decrypt(word):
    return "".join([alphabet[alphabet.find(i) - 1] for i in word])

new_message = encrypt(message)
print(new_message)
print(decrypt(new_message))
