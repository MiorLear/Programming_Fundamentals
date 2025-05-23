'''
2.3.2. Desarrollar un programa en Python que permita calcular el impuesto que debe
pagar un usuario por el consumo de energía.
El cálculo debe realizarse basado en la siguiente tabla.
| Unidades consumidas	|     impuesto  		|
-------------------------------------------
|	    0 - 100				  |   sin impuesto	 	|
|	    101 - 200			  | $0.70 por unidad 	| #???
|	    201 o mas			  | $0.70 por unidad 	| #??? el mismo impuesto para los dos? 
#dejaré el  último como $1.00 por unidad
'''

eng = input("Type your energy consumption: ")

while (True):
    try:
        eng = int(eng)
        break
    except:
        eng = input("Plese enter your energy consumption: *Digits only* ")

if int(eng) > 0 and int(eng) <= 100:
    print("Your total fee is: $" + str(eng) + " With non extra taxes")
if int(eng) > 100 and int(eng) <= 200:
    print("Your total fee is: $" + str(int(eng)*1.7) + " With taxes ($0.70 per unity)")
if int(eng) > 200:
    print("Your total fee is: $" + str(int(eng)*2) + " With taxes ($1.00 per unity)")