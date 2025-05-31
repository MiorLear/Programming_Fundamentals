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

for n in range(1,3):
    result += " "*(5-n) +pattern_1*n
    result += pattern_2 * 2 + "_"  
    result += " "*(5-n) +pattern_1*n
    pattern_1 +="**"
    result += "\n"

print(result)