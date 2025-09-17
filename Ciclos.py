#ciclos/bucles

#WHILE se rige con codiciones limitantes para detenerse
my_condition = 0

while my_condition < 16: #Colocamos la condicion o el limitante de hasta 16
    print(my_condition)
    my_condition +=1     #El bucle buscara el valor de la condicion para eso le aumentaremos
else:                    #de 1 en 1 para aumentar y llegue al valor de la condicion
    print("La condicion es mayor a 16") #Si el valor llega al limite, se detendra y matendra ese valor

print("Continua la ejecucion")  #Continua 

#Otro ejemplo
while my_condition < 20:   #Aqui my_condition tiene el valor de 16 
    my_condition += 1
    if my_condition ==19:  #Aqui si el valor suma hasta llegar a 19 ahi se detiene sin 
        print("Se detiene")#que llegue a limite 20 
        break

    print(my_condition)

print("Continua la ejecucion")

#FOR solo regresa los datos dentro del objeto sin repetirse, a menos con condiciones
#Se puede usar con listas, sets, tuples y diccionarios
my_list = [12,56,88,92,0,12]
for elemt in my_list:
    print(elemt)

my_sets = {24, "Dany", "Martinez", "Matinez"}
for elemt in my_sets:
    print(elemt)

my_tuple = (24, 1.80, "Dany", "Martinez")
for elemt in my_tuple:
    print(elemt)

my_other_dict = {"Nombre":"Dany", "Apellido":"Garcia", "Edad":24}
for elemt in my_other_dict:  #en este for solo aparecen las claves y no los valores
    print(elemt)

my_other_dict = {"Nombre":"Dany", "Apellido":"Garcia", "Edad":24}
for elemt in my_other_dict.values(): #en este for si aparecen los valores con el .values
    print(elemt)

my_other_dict = {"Nombre":"Dany", "Apellido":"Garcia", "Edad":24, "Color":"Piel"}
for elemt in my_other_dict: 
    print(elemt)
    if elemt == "Ewdad":
            break  #Se detiene hasta llegar a Apellido
    print("Se ejecuto")
else:
    print("No existe")

    
