#Exception sirve para controlar errores y que no interrumpar el programa

number_one = 5
number_two = 9
number_two = "2"  #Colocalor dos variables iguales pero con diferente tipo de dato
number_three=2

#Las exception siempre lleva esta estructura try except
try:
    print(number_two + number_one)
    print("No ha ocurrido error")
except:                    #El exception funciona para mencionar que si el programa tuvo un error nos dara a conocer
    print("Ha ocurrido un error")


#Las exception siempre lleva esta estructura try except else
try:
    print(number_two + number_one)
    print("No ha ocurrido error")
except:                    
    print("Ha ocurrido un error") 
else:
    print("Nuestro programa sigue continuando y paso el except")
finally:                #finally se ejecuta siempre, sea que este bien o no el programa
    print("Siempre se ejecuta, siempre")


#Las exceptions por tipos mas especificos
try:
    print(number_two + number_one)
    print("No ha ocurrido error")
except ValueError:      #Colocamos el error que queremos ver (un error que sea valor)               
    print("Ha ocurrido un ValueError") 
except TypeError:       #Colocamos el error que queremos ver (un error que sea tipo de valor)            
    print("Ha ocurrido un TypeError") 
else:
    print("Nuestro programa sigue continuando y paso el except")

