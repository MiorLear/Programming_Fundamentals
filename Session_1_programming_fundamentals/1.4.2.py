'''
1.4.2.
Dados dos números enteros positivos muy grandes como cadenas de texto A y B.
Calcula (A + B) e imprímelo como cadena de texto.

Restricciones
10^100 ≤ A, B ≤ 10^1000
No convertir a formato de números. La operación se debe realizar utilizando cadenas de texto.
'''

n1 = input("a: ") # --> len 5
n2 = input("b: ") # --> len 3

ans = ""
i=0

if len(n1) > len(n2) : 
    minlen = n2 
    maxlen = n1
else: 
    minlen = n1
    maxlen = n2

while len(minlen) < len(maxlen):
    minlen = minlen[::-1]
    minlen+= "0"
    minlen = minlen[::-1]

ans = ""

for i in range (len(maxlen)):
    ans += str(int(minlen[i]) + int (maxlen[i]))

# ans = ans[::-1]
# ans = str(int(n1) + int(n2))

print ("minlen: "+minlen +"\nmaxlen: "+maxlen + "\nans: " +ans)

'''
For this exercise I use some While loops and inverted arrays in order to make both quantities the same length
and then sum each other.
'''