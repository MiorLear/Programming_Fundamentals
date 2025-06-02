'''
Imprime el siguiente patrón usando
bloques for/while:
Salida:
• Patrón solicitado.
Restricciones:
• No se puede imprimir de forma
estática ninguna sección de la
figura.
Conceptos explorados:
• Bloques anidados y manejo de
índices.
'''

pattern_1 = "*"
pattern_2 = "_-"
pattern_3 = "-_"

result = ""

for n in range(1,6,2):
    result += " " *int(n)
    result += pattern_1 * n
    result += "\n"
    # result += pattern_2 * 2 + "_"  
    # result += pattern_1 * n

# for n in range(3,0,-2):
#     result += pattern_1 * n
#     result += "\n"
    # result += pattern_2 * 2 + "_"  
    # result += pattern_1 * n

print(result)