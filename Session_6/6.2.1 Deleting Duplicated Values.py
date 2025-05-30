'''
Dada una lista ingresada por el usuario, elimina los elementos duplicados
manteniendo la primera aparición de cada número.
Entrada:
• La primera línea contiene n enteros a, ....
an (1 ≤ aj ≤ 106)
Salida:
• Una línea con los enteros únicos en su orden de aparición, separados por espacios.
'''

num = input("Type a list of numbers, with each number separated by a space: ")

numbers = num.split()
seen = set()
result = []

for n in numbers:
    if n not in seen:
        seen.add(n)
        result.append(n)

print(" ".join(result))

