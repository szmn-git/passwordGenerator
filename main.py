import string
import random

def generate(lista):
    password = ''
    for i in range(0,10):
        password += lista[random.randrange(0, len(lista))]
    return password

def checkCond(pasw):
    lista = [bool(any(letter in pasw for letter in letters)), bool(any(letter in pasw for letter in uppers)),
             bool(any(letter in pasw for letter in numbers)), bool(any(letter in pasw for letter in special))]
    return lista


letters = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)
numbers = list('0123456789')
special = list('!@#$%^&*()?')

lista = letters + uppers + numbers + special

ans = generate(lista)

temp = False

print(checkCond(ans))