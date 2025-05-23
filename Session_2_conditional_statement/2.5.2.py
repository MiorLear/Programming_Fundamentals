'''
Eres parte del equipo de desarrollo de un sistema de defensa automatizado para una base
científica ubicada en una zona volcánica peligrosa. Por cuestiones de seguridad,
el sistema debe identificar si un objeto detectado por sensores
(un punto con coordenadas (x, y)) se encuentra en una zona peligrosa,
de manera que pueda activarse una alerta inmediata. Las zonas de peligro están definidas como:

-  Zona de peligro 1: el punto se encuentra en el primer cuadrante, es decir, x > 0 y y > 0.
-  Zona de peligro 2: el punto está dentro de un círculo de radio 5 centrado en el origen (0, 0),
es decir, x² + y² <= 25.

Restricciones:
• Sin usar librería math, solo operaciones
aritméticas y lógica booleana

Formato de Entrada 

(-10, 5)

'''

entrada = input("Ingrese las coordenadas del punto (formato (x, y)): ")

entrada = entrada.replace("(", "").replace(")", "").replace(" ", "")
x_str, y_str = entrada.split(",")

x = int(x_str)
y = int(y_str)

dng_1 = x > 0 and y > 0
dng_2 = x * x + y * y <= 25

if dng_1:
    print("Peligro")
    exit()

if dng_2:
    print("Peligro")
    exit()
    
if not (dng_1 or dng_2):
    print("Seguro")
