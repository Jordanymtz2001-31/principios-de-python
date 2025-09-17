#Tuples
#Los contructores para las tuplas es muy similar a las listas
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 1.80, "Dany", "Martinez")
print(my_tuple)
print(type(my_tuple))
my_other_tuple = (1,2,3,4)

#Tambien puede uno extraer datos dentro de las duplas
print(my_tuple[0])
print(my_tuple[1])

#Tambien puede uno contar con .count cuantas veces existe ese valor dentro de...
print(my_tuple.count("Dansy"))

#Con index localiza en que lugar se encuentra el valor
print(my_tuple.index("Dany"))

my_sum_tuple = (my_other_tuple + my_tuple)
print(my_sum_tuple)

#Imprimimos solo de los limites
print(my_sum_tuple[3:7])

#LAS DUPLAS NO SE PUEDEN MODIFICAR SUS VALORES, AUN QUE SOLO SE PUEDE
#CUANDO LAS PASA DE TIPO LISTA PARA PODER MODIFICAR LOS VALORES

my_tuple = list(my_tuple)
print(type(my_tuple))

#Modificamos
my_tuple[2]= "Melany"
my_tuple.insert(4, "Martinez")
print(my_tuple)

#Volvemos a cambiar a una Tupla con las modificaciones de los valores
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


