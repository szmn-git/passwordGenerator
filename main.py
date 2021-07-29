import string
import random

def passLen():
    print("Podaj długość hasła nie mniejszą niż 8:")
    length = int(input())
    if length < 8:
        length = 8
    return length


def generate(lista):
    password = ''
    for i in range(0,length):
        password += lista[random.randrange(0, len(lista))]
    return password

def checkCond(pasw):
    lista = [bool(any(letter in pasw for letter in letters)), bool(any(letter in pasw for letter in uppers)),
             bool(any(letter in pasw for letter in numbers)), bool(any(letter in pasw for letter in special))]
    print("Sprawdzanie warunków")
    return all(lista)


letters = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)
numbers = list('0123456789')
special = list('!@#$%^&*')

lista = letters + uppers + numbers + special

length = 10

#ew do zakomentowania
length = passLen()

while True:
    ans = generate(lista)
    if checkCond(ans):
        break

print("Wygenerowane hasło:\n" + "\t" + ans)