'''
1.3.1.
Pide al usuario el total de una cuenta y el porcentaje de propina (por ejemplo, 10%, 15%, 20%).
Calcula y muestra en pantalla el total a pagar.
'''

bill = input("Plese enter your current bill: ")
while (True):
    try:
        bill = float(bill)
        break
    except:
        bill = input("Plese enter your bill: *Digits only* ")
        
tip = input("Plese enter your tipping percentage: (10% - 20% - 30%) ")
while (True):
    try:
        tip = float(tip)
        break
    except:
        tip = input("Plese enter your tipping percentage: (10% - 20% - 30%) *Digits only* ")

total_bill = round(bill * (1+tip*0.01), 2)
print("Yout tottal bill is $" + str(total_bill))

'''
I've made this code validating the possibility of using chars, to made this possible I've used 
try except, I known that we're making a review, but I already have good programming fundamentals.
Also I used the str() function to print the total bill
'''