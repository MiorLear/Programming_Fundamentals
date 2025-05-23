'''
2.5.1. En un edificio hay dos elevadores (A y B) en distintos pisos.
Un usuario llama al elevador desde un piso p. El elevador más cercano responde,
pero si ambos están a la misma distancia, elige el A.
'''

n = input()

a, b, p = n.split(" ")

a = int(a)
b = int(b)
p = int(p)

if abs(a-p) < abs(b-p):
    print("Elevador A")
elif abs(a-p) == abs(b-p):
    print("Elevador A")
else:
    print("Elevador B")