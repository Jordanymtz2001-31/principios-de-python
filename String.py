# String
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
my_new_string= "Un string\nconsalto de tiempo"
print(my_new_string)

#Formateo

name, surname, age = "Juan", "Daniel", 21

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
#print("Mi nombre es %s %s y mi edad es $d" %(name, surname, age))

#Inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#desempaquetado
language= "Python"
a,b,c,d,e,f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Divicion

language_slice= language[1:3]
print(language_slice)

language_slice= language[1:]
print(language_slice)

language_slice= language[-2]
print(language_slice)

#Reverse

reserved_language = language[::-1]
print(reserved_language)

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))
