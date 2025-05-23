'''
1.3.2.
Solicita al usuario su nombre completo (asume dos nombres y dos apellidos).
Luego, el programa generará, su correo con el formato:
primer_nombre.primer_apellido@keyinstitute.edu.sv
'''

fullname = input("please enter your full name: *two names & two lastnames* ")
name, ignore, lastname, ignore = fullname.split(" ")
print("Your key email is: \n" + name + "." + lastname + "@keyinstitute.edu.sv")

'''
For this exercise I made use of the split method to separate each name & lastname
then I simply ignore the second name and the second lastname to finally print
the solicitated email. 
'''