#Variable Int
mi_variable_int =5
print(mi_variable_int)

#Variable String
mi_variable_string="Hola mundo"
print(mi_variable_string)

#variable boolean
mi_variable_bool=True
print(mi_variable_bool)

#variables juntas con ,
print(mi_variable_string, mi_variable_bool, mi_variable_int)

#convertir u  entero en String
mi_varInt_to_string=str(mi_variable_int)
print(mi_varInt_to_string)
print(type(mi_varInt_to_string))

#concatenacion de variables en un print
print(mi_variable_string, mi_variable_bool, mi_variable_int)
print("El valor del boleano es:", mi_variable_bool)

#Funciones del sistema 

#len cuenta las palabras de un string
print(len(mi_variable_string))

#Variables en una sol alinea
name, surname, alias, age = "Dany", "Fanton", "Gorge", 22
print("Su nombre es", name, surname, "y su alias es", alias, "con", age, "años")

#funcion para pedir datos de la consola o cliente con input
name=input("¿Cual es tu nombre?")
age=input("¿Cuantos años tienes?")

print(name)
print(age)

#Cambios de tipo de dato
name=20
age="dany"
print(name)
print(age)

#¿Forsamos el tipo de dato?
address: str="Mi direccion"
address=20

print(type(address))

