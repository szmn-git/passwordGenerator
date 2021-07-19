import string
import random

def generate(lista):
    password = ''
    for i in range(0,10):
        password += lista[random.randrange(0, len(lista))]
    return password

uppers = list(string.ascii_uppercase)
numbers = list('0123456789')
special = list('!@#$%^&*()?')

lista = list(string.ascii_lowercase) + uppers + numbers + special

ans = generate(lista)

print(ans)