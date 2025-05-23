'''
2.4.1. Crea un programa en Python para determinar si un número es "mágico“.
Un número es “mágico” si es divisible por 7 pero no por 5.
'''

while True:
    n = int(input("Type a number: "))

    if n % 7 == 0 and n % 5 != 0 :
        print("Congrats! you find a magic number")
        break
    else:
        print("Give it another try...\n")