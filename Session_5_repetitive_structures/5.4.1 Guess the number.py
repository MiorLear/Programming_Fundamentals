'''
Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.
Entrada:
• Números enteros entre 1 y 100.
Salida:
• Tres posibles salidas: “El número secreto es menor”, “El número secreto
es mayor”, ¡Felicidades! Has adivinado el número secreto”
'''
from random import randrange

n = randrange(1,100)
ans = ""
print (n)
while ans != n:
    ans = int(input("Guess the secret number: "))

    if ans < n :
        print("The secret number is major")
    elif ans > n:
        print("The secret number is minor")

    
print("You've guessed the secret number!")