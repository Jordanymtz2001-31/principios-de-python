#Clases

class MyPersona:  #Colocamos es pass para completar la clase
    pass          #En las clases los nombre siempre llevan la primera letra de la palabra mayuscula  

print(MyPersona)  #Funciona asi 
print(MyPersona())#O asi

class Persona:
    def __init__(self, name, surname): #El self sirve para asignar siertos valores asociados a la clase
        self.name1 = name               #Tenemos que guardar los datos para poder extraerlos 
        self.surname1 = surname         #Las propiedades se pasan a self y sin el pass pasan hacer fuera

        self.full_name = f"{name}{surname}"  #Aqui estamos metiendo el nombre completo en una sola variable


my_persona = Persona(name="Dany", surname="Martinez")
print({my_persona.name1, my_persona.surname1})
print([my_persona.name1, my_persona.surname1])
print(f"{my_persona.name1, my_persona.surname1}")

print(my_persona.full_name)

#Otro ejemplo de clase pero dentro una funcion --------------------------------->
class Persona:
    def __init__(self, name, surname):

        self.full_name = f"{name}{surname}"  #Aqui estamos metiendo el nombre completo en una sola variable
        self.__namep = name                  #Variable privada
    
    def get_name (self):                     #Creamos el get_name para poder obtener el valor de nombren y que nos regrese su valor
        return self.__namep
   
    def walk (self): #Creamos una fuccion donde persona hace la accion de caminar
        print(f"{self.full_name}" "Esta caminando")

my_persona = Persona("Dany","Martinez")
print(my_persona.full_name)

my_persona.walk() #Unimos la clase Persona (con sus valores) y la funcion wal para imprimir

my_other_person = Persona("Melany", "Martinez")        #Creamos otra variable para meter otros datos de otra persona
my_other_person.full_name= "Melany la caza unicornios" #Cambiamos el valor de full_name
print(my_other_person.full_name)
print(my_persona.get_name())                           #Imprimimos el valor del nombre que es privado, pero con la funcion get
