import random
alphabet = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
message = "lambda"#input("Your message: ").lower()

for i in message:
    print(f"Индекс буквы {i.upper()} - {alphabet.find(i)} \nASCII код - {ord(i)}\nИндекс + ASCII код - {alphabet.find(i) + ord(i)}\nИтоговая кодировка {chr(alphabet.find(i) + ord(i))} - {alphabet[(alphabet.find(i) + ord(i)) % len(alphabet)]}\n")

def encrypt(word):
    return "".join([alphabet[(alphabet.find(i) + ord(i)) % len(alphabet)] for i in word])

def decrypt(word):
    return "".join([alphabet[(ord(i) - alphabet.find(i))] for i in word])

# new_message = encrypt(message)
# print(new_message)
# print(decrypt(new_message))
