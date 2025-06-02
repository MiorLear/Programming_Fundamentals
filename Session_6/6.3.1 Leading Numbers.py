'''
Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.
Entrada:
• La primera línea contiene n enteros a₁, ..., aₙ
(1 ≤ aᵢ ≤ 10⁹)
Salida:
• Una línea con todos los números líderes
en el orden en que aparecen en el arreglo.
12
Ejercicio requerido (tarea 9)
'''

numchain = input("Type the num chain: ")
numchain = numchain.split(" ")
numchain = numchain[::-1]
prev = 0
i = 0
result = list()
for x in numchain:
    if i == 0:
        i += 1
        continue
    
    if int(x) > int(prev):
        result.append(x)

    prev = x
    i += 1
    
numchain2 = ""
for y in result:
    numchain2 += y + " "

print(numchain2)
