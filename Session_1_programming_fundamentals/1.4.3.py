'''
1.4.3.
Dado un arreglo de n fracciones (representadas como cadenas "a/b"),
calcula la suma total y expresa el resultado como una fracción irreducible.

'''
n = int(input("Type the num of fractions you wanna evaluate: "))
fractions = []

for i in range(n):
    fraction = input("Type the fraction # " + str(i + 1) + ": ")
    fractions.append(fraction)

num1, den1 = fractions[0].split("/")
num1 = int(num1)
den1 = int(den1)

for i in range(1, n):
    num2, den2 = fractions[i].split("/")
    num2 = int(num2)
    den2 = int(den2)

    num1 = num1 * den2 + num2 * den1
    den1 = den1 * den2

i = 2
while i <= abs(num1) and i <= abs(den1):
    if num1 % i == 0 and den1 % i == 0:
        num1 = num1 // i
        den1 = den1 // i
    else:
        i += 1

print("result:", str(num1) + "/" + str(den1))
