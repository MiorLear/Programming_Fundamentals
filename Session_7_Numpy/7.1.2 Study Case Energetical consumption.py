import numpy as np



consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones: ", consumo.ndim)
print("Forma: ", consumo.shape)
print("Tipos de datos: ", consumo.dtype)
print("Consumo primer hogar: ", consumo[0])
print("Consumo el miércoles (día 3): ", consumo[:,2])

#Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis = 1)
#Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis = 0)
#suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

maximos = np.max(consumo, axis= 1)
minimos = np.min(consumo, axis= 0)
desviacion = np.std(consumo)

#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
#Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
#Indice del hogar con menor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis = 1)
print(f"Consumo total de cada hogar durante la semana:  {consumo_total_hogar}")

#compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
#Filtrando hogares que cumplen la condición
consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogares con mayor consumo a 100: {consumo_mayor_100}")

#Aplicando normalizacion MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min() / (consumo.max() - consumo.min()))
#Resultado
print(consumo_normalizado)

'''
Cuestionario.
1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
'''

# Pregunta 1

print (f"El consumo del hogar 5 el día viernes es {consumo[4,4]} kWh")
print (f"Consumo de los ultimos 3 hogares el domingo {consumo[-3:,6]} kWh")

print(f"Promedio de consumo en fines de semana: {np.mean(consumo[:, [5, 6]]):.2f} kWh")

desviaciones_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviaciones_por_dia)
print(f"El dia con mayor desviacion estandar es el dia {dia_mayor_desviacion} con un valor de {desviaciones_por_dia[dia_mayor_desviacion]:.2f}")

consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print(f"Indices de los 3 hogares con menor consumo: {indices_menor_consumo}")
print(f"Valores de consumo total: {valores_menor_consumo}")


