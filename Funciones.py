#Funciones
#Las Funciones son fraccmentos de codigos que realizan x funcionamientos para
#posteriormente solo llamarlos por su nombre

def my_function ():  #Usamos la palbra reservada de def y colocamos el nombre de nuestra funcion
    print("Esta es una funcion")

my_function()  #Aqui solo llamamos nuestra funcion y imprime lo que esta dentro de ella

print("SIgue el programa")


#Otro ejemplo con operaciones
def my_function_oper(firt_number1, second_number1): 
    print(firt_number1 + second_number1)

#my_function_oper(25,55) #Llamamos la funcion de operacion y metemos los paremtros que queremos sumar
#my_function_oper(1,2.2)
#my_function_oper("2","2")
#my_function_oper("hola", " papus")
#my_function_oper(1.5,2.6)

#Otro ejemplo con operaciones
def my_function_opera1(firt_number: int, second_number : int, thrre_number: int): #Tambien podemos definir que tipo de datos queremos que sea
    print(firt_number * second_number + thrre_number)

my_function_opera1(25,55,2) #Llamamos la funcion de operacion y metemos los paremtros que queremos 
my_function_opera1(1,2.2,2)
my_function_opera1(1.5,2.6, 2)

#Otro ejemplo con cadena de tex
def my_function_txt(firt_text: str, second_text : str): 
    print(firt_text + second_text)

my_function_txt("2","2")
my_function_txt("hola", " papus")

#Ejemplo con return -> no regresa valores
def my_function_whith_return(number_one, number_two):
    my_suma = (number_one - number_two)
    return  my_suma  #Reresamos el valor obtenido pero sin guardarlo o imprimirlo

my_result = my_function_whith_return(10,5) #Metemos los parametros para que nuestra funcion lo suyo, pero necesitamos

#Ejemplo, una funcion con formato de ordenacion horizontal
def my_function_name(name, surname):
    print(f"{name, surname}")

my_function_name(surname="dany", name="martinez") #Podemos cambiar el lugar del los valores en los parametros


#Ejemplo de defaul ---> los datos se pasan por defecto que ya tiene asiganado
def my_function_defaul(name, surname, alias = "yorch"):
    print(f"{name, surname, alias}")

my_function_defaul("Dany","Martinez")   #En este caso no le coloque un alias y por defecto le podra el que tiene en la funcion
my_function_defaul("Melany","Martinez", "Flaca")

#Otro ejemplo con paramatro infinito con *
def function_text(*text):
    print(type(text))
    for text in text:
        print(text.upper())

function_text("hola")
function_text("hola", "Dylan", "como", "has", "estado")
function_text("hola", "adios")