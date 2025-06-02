'''
Session:      Session 6        
Exercise:     Leading Numbers
Description:  Delete the duplicated values of a string chain.

Author:       Miguel Orlando Ledezma Arévalo
Date:         2025-06-02
Status:       [ Finished ]
'''

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
prev = list()
result = list()
i = 0
for x in numchain:
    prev.append(x)
    if i == 0:
        i += 1
        continue
    add = True
    for y in prev:
        if int(x) < int(y):
            add = False
            break
    if add:
        result.append(x)
    
    i += 1
    
numchain2 = ""
for x in result:
    numchain2 += x + " "

print(numchain2)
