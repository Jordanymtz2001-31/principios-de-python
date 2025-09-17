#sets
my_sets = set() #la forma de ser un set
my_other_sets= {} #otra forma de decir que es un sets pero cuando esta vacia es una lista

print(type(my_sets)) 
print(type(my_other_sets))

my_other_sets = {24, "Dany", "Martinez", "Matinez"}
print(type(my_other_sets))

print(len(my_other_sets)) #lent Cuenta la cantidad la cantidad de elementos

my_other_sets.add("1.80") #En os sets al agregar un elemento no lo ordena
print(my_other_sets) 

my_other_sets.add("1.80") #En los sets no podemos agrgar elementos repetitivos
print(my_other_sets) 

print("1.80" in my_other_sets) #Podemos relaizar busquedas en los sets

my_other_sets.remove("1.80") #Podemos quitar elementos con remove
print(my_other_sets) 

my_other_sets.clear() #Quitamos o limpiamos con clear
print(len(my_other_sets)) 

#Convertimos el set en lista (NO ES MUY RECOMENDADO YA QUE CAMBIANAN LAS POSISION)

my_sets = {24, "Dany", "Martinez", "Matinez"}
my_sets = list(my_sets)

print(my_sets)
print(my_sets[0])


