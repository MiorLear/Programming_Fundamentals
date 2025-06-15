import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')

g = 9.81

falcon9 = {
    'nombre': 'Falcon 9',
    'masa_inicial': 549000,
    'empuje': 7607000,
    'tiempo_combustion': 162
}

saturnV = {
    'nombre': 'Saturno V',
    'masa_inicial': 2800000,
    'empuje': 35100000,
    'tiempo_combustion': 150
}

def calcular_aceleracion_vs_tiempo(datos, puntos=500):
    t = np.linspace(0, datos['tiempo_combustion'], puntos)
    masa = datos['masa_inicial'] * (1 - 0.8 * (t / datos['tiempo_combustion']))
    aceleracion = (datos['empuje'] - masa * g) / masa
    return t, aceleracion

t_falcon9, a_falcon9 = calcular_aceleracion_vs_tiempo(falcon9)
t_saturnV, a_saturnV = calcular_aceleracion_vs_tiempo(saturnV)

v_falcon9 = np.cumsum(a_falcon9 * np.diff(np.insert(t_falcon9, 0, 0)))
v_saturnV = np.cumsum(a_saturnV * np.diff(np.insert(t_saturnV, 0, 0)))

falcon9_v_real = 2500
saturnV_v_real = 2700

plt.figure(figsize=(7, 10))
plt.plot(v_falcon9, t_falcon9, label='Falcon 9 - Modelo Teórico', linewidth=2)
plt.plot(v_saturnV, t_saturnV, label='Saturno V - Modelo Teórico', linewidth=2)

plt.axhline(y=162, color='gray', linestyle=':', linewidth=1)
plt.axvline(x=falcon9_v_real, color='red', linestyle=':', label='Falcon 9 - Velocidad Real')
plt.axhline(y=150, color='gray', linestyle=':', linewidth=1)
plt.axvline(x=saturnV_v_real, color='orange', linestyle=':', label='Saturno V - Velocidad Real')

plt.text(falcon9_v_real + 30, 120, '2500 m/s (Falcon 9)', rotation=90, color='red')
plt.text(saturnV_v_real + 30, 100, '2700 m/s (Saturno V)', rotation=90, color='orange')

plt.title('Velocidad Acumulada (m/s) vs Tiempo (s) - Teoría vs Realidad')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('Tiempo (s)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('velocidad_vs_tiempo_cohetes_actualizado.png', dpi=300)
plt.show()