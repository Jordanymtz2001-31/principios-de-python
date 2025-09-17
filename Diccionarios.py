#Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Dany", "Apellido":"Garcia", "Edad":24}
print(my_other_dict)

my_dict={
    "Nombre":"Dany", 
    "Apellido":"Garcia", 
    "Edad":24,
    "Lenguajes":{"Pyhon", "HTML", "java"},
     "Calle":"Nezahualcoyoctl" #Se puede crear diccionarios dentro de otro diccionario
    }
print(my_dict)

#Se puede buscar el dato que se desea colocando corchetes []
print(my_dict["Lenguajes"])

#En los diccionarios si se puede actualizar los valores
my_dict["Apellido"]="Maritnez"
print(my_dict)

#Se puede eliminar datos con del
del my_dict["Calle"]
print(my_dict)

#Forma de confirma si existe con comparacion true o false
print("Dany" in my_dict) #false por que solo busca el primero y antes de Dany es Nombre
print("Nombre" in my_dict) #true por que es el primero

print(my_dict.items()) #El items muestra todos los datos (Tanto como la clave y el valor)
print(my_dict.keys()) #El keys muestra solo las claves del diccionario
print(my_dict.values()) #El values muestra solo los valores

#con el fromkeys da como valore en 0
my_list = ["Nombre", 1 , "piso"]

my_new_dict= dict.fromkeys((my_list) ) #En forma de lista con my_list
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) #En forma de diccionario con my_dic    
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

print(tuple(my_new_dict)) #El tuple me regresa las claves en estructura de tupla
print(set(my_new_dict)) #El set me regrea las claves en forma de ser