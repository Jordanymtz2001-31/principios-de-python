#Lists
#Cual quier de los dos constructores se puede utilizar
my_list= [11,2,1,1,12,52] 
my_other_list = list()

print(len(my_list))

#Podemos crear listas con diferentes tipos de datos 
my_other_list = [48, 1.8, "Dany"]
print(len(my_other_list))
print(type(my_other_list))

print(my_other_list[1])
#El numero Negativo regresa de adelante hacia tras
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])

#El len sirve para contar mientras el count sirve para contar la 
# cantidad de veces repetidas dentro de ina lista
print(my_list.count(1))

edad, altura, name = my_other_list
print(edad)

#Se puede sumar dos listas con diferentes tipos de datos
print(my_list + my_other_list)

#El .append agrega una objeto al final de la lista
my_other_list.append("Martinez")
print(my_other_list)

my_other_list.insert(4, "Garcia")
print(my_other_list)

#El .po elimina la ultima variable (Se puede selescionar tambien) 
# de una lista pero al mismo tiempo de retorna o lo guarda a una variable
print(my_list.pop())
print(my_list)

my_pop_list= my_list.pop(0)
print(my_pop_list)
print(my_list)

#El del alimina definitivo a una variable
del my_list[1]
print(my_list)

#El .copy es para copiar el calor de una variable y pasarlo a otra variable antes de.Eli
my_new_list = my_list.copy()

#el .clear limpia toda la lista
my_list.clear()
print(my_list)

#Se imprime la nueva lista que se limpio pero con una nueva referebcia
print(my_new_list)



