#Condiconales

my_condition = True

if my_condition :   #Aqui no se ocupan las lleves sino que doble punto :
    print("Se ejecuta el if por defecto")

my_condition = 5 * 2  #Damos valor a mi codicion

if my_condition == 12: #Colocamos una limitante para ver si es true o false
    print("Seejecuta por que es verdadera la codicon que se realiza")
else:
    print("Se ejecuta por que es lo contrario a la condicion")

#Otro ejemplo es

if my_condition == 8 and my_condition <10: #Colocamos una limitante para ver si es true o false
    print("Es = a 9 y es - a 10")
else:
    print("Es diferente de 8 y es 10 o mayor")
    #En este caso no existe las llaves para ver los limites de las codiciones
    #Sino con las tabulaciones nos damos cuenta hasta donde esta o termina 
    #Si pegamos nuestro codigo hacia la izquierda deja de estar dentro del else o if 
    print("Vamos bien ^_^")


#Otro ejemplo es

if my_condition <8 and my_condition >10: #Colocamos una limitante para ver si es true o false
    print("Es = a 9 y es - a 10")

elif my_condition==11:   #En el elif tenemos que poner una codicion adicional 
    print("Cumple la condicion que se le dio 11")

else:
    print("Es diferente de 8 y es 10 o mayor")

#Ejemplo de una condicion String

my_string = ""

if my_string == "Hola todos":
    print("Cumple")
else:
    print("No cumple")

#Otro ejemplo con el not
if not my_string:
    print("Cumple por que no tiene nada la cadena de text")
else:
    print(" cumple por que si tiene cade de texto")