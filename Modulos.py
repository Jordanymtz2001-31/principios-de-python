#Modulos

#Forma de importar de otro fichero
import Modulo_Guia

Modulo_Guia.sum_value(12, 2)
Modulo_Guia.prin_value("Hola :)") 

#----------------------------->

#Otra forma de importar solo el nombre de la funcion (Mas corto)
from Modulo_Guia import sum_value, prin_value

sum_value(1,1)
prin_value("GPI") 


#----------------------------->

import math #math es parte de...proporciona funciones y constantes matemáticas predefinidas 

print(math.pi)  #llamamos a una funcion por parte del sistema
print(math.pow(2,4))


from math import pi as PI_VALUE  #Tambien podemos mandar a traerlo asi y poner u  alias
print(PI_VALUE)


