'''
Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.
Entrada:
• Un numero entero.
Restricciones:
• 1 ≤ número ≤ 10^9
Conceptos explorados:
• Bucles y control de flujo.
'''

chain = input("Type a chain of numbers: ")

while len(chain)  > 1:
    sum = 0
    for n in chain:
        sum+= int(n)
    chain = str(sum)
    
print(sum)
