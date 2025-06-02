'''
Session:      Session 7        
Exercise:     Numpy Introduction
Description:  Numpy usage and implementation Introduction.

Author:       Miguel Orlando Ledezma Arévalo
Date:         2025-06-02
Status:       [ Finished ]
'''

import numpy as np

#Creación de Matrices con Numpy
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print("Crear una matriz con numpy \n")
print(arr)

#Crear una matriz de ceros
zeros = np.zeros(5)
print("\nCrear una matriz de ceros\n")
print(zeros)

#Crear una matriz de unos
ones = np.ones(5)
print("\nCrear una matriz de unos \n")
print(ones)

#Sumar y multiplicar matrices
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nSumar matrices\n")
resultado = arr1 + arr2
print (resultado)

resultado = arr1 * arr2
print("\nMultiplicar matrices\n")
print (resultado)


#Sumar a matrices
arr = np.array([1, 2, 3])
print("\nSuma a una matriz\n")
result = arr + 5
print(result)

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
print("\nSuma a una matriz\n")
result = arr1 + arr2
print(result)

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales