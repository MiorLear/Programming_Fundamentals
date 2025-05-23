'''
2.4.2. Determina si un año es bisiesto, considerando las reglas gregorianas.
'''

while True:
    n = int(input("Type a number: "))

    if n % 4 == 0 :
        print("Bisiesto")
        break
    elif n % 400 == 0 and n % 400 == 0:
        print("Bisiesto")
        break
    else:
        print("No Bisiesto...\n")