import string
import random

def generate(lista):
    password = ''
    for i in range(0,9):
        password += lista[random.randrange(0, len(lista))]
    return password


lista = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list('0123456789') + list('!@#$%^&*()?')

print(generate(lista))

