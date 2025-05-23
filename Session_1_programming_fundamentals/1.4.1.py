'''
1.4.1.
Dados tres enteros a, b y k, imprime el resultado de a / b con k decimales exactos (sin redondear).
Restricciones:
No es posible dar formato utilizando "{:.{k}f}“ para redondear los decimales.
'''

number_1 = float(input("a: "))
number_2 = float(input("b: "))
number_3 = int(input("k: "))
num, dec = str(number_1/number_2).split(".")

periodic = False

if len(dec) > 10:
    previous = dec[0]
    braked = 0

    #In order to include periodic numbers...
    for d in dec:
        if d != previous: 
            if braked < 3 :
                braked +=1
            else:
                periodic = False
                break
        else:
            periodic = True 
        previous = d
    #It works with periodic numbers but only the ones with the same repeated number
    #for instance: 1/3 = 0.333... 1/6 = 0.1666... 
    #But it fails with others like: 1/7 = 0.142857142857142857...

while len(dec) < number_3:
    if periodic :
        dec += previous  
    else:
        dec += "0"

print(num + "." + dec[:number_3])

'''
For this exercise I made use of split method (again) to separate the integers from the decimals then
increase the amout of decimals if necessary also I've used slicing which is [:number_3] this works as 
a limit for the amount of decimals.
'''
