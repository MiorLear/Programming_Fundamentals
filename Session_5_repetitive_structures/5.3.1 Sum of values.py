'''
Dada una lista de longitud variable de números enteros ingresada por el usuario,
calcula e imprime la suma de todos los números usando un bucle for.
Entrada:
• Una lista de longitud variable ingresada por el usuario.
Salida:
• Suma de todos los componentes de la lista.
Restricciones:
• Sin restricciones
12
'''

n = int(input ("type an amount of numbers: "))
array = []

for i in range(n):
    valor = int(input("Type the value #" + str(i + 1) + ": "))
    array.append(valor)

sum = 0
for a in array:
    sum+=a

print("Total: "+str(sum))