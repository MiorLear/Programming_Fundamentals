'''
2.3.1. Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una mayúscula
'''

while True:
    pwd = input("Type your password! ")

    if len(pwd) < 8:
        print("Your password must have at least 8 digits")
        continue

    hasnum = False
    hascapital = False
    for c in pwd:

        if(hasnum and hascapital):
            break

        if c.isdigit():
            hasnum=True
            continue
        elif c.isupper():
            hascapital=True
            continue
        else:
            continue
    
    if hasnum==False:
        print("Your password must have at least one number")
        continue
    if hascapital==False:
        print("Your password must have at least one capital letter")
        continue
    print("Password succesfully created!")
    break