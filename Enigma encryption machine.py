import random
alphabet = "abcdefghijklmnopqrstuvwxyz "
message = "lambda"#input("Your message: ").lower()


def hash(num):
    return num % 30 * 3 - 20
    

b = [[] for i in range(100)]
# b[3].append(56)
# b[3].append(78)    


for i in range(100):
    b[hash(i)].append(i)

print(b)



# def encrypt(letter):
#     new_letter = alphabet[random.randrange(len(alphabet))]
#     return new_letter if letter != new_letter else encrypt(letter)


# for i in range(30):
#     print("".join(map(encrypt, message)))