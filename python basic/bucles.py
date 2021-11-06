#Se puede tener un tercer parametro que indica la secuencia en la que pasa de valor en valor.
for  i in range (1,5):
    print(i)

for char in "Loops" :
  print(char)

#Listas
listaSimple = [1, 2, 3] 
for num in listaSimple :
  print(num)

#Tuplas
for num in (1, 2, 3):
  print(num)

#Diccionarios, para iterar en las claves.
letras = {"a": 1, "b": 2}
for clave in letras:
  print(clave)

#Para iterar los valores del diccionario.
for valor in letras.values():
  print(valor)

#Para los pares, clave-valor.
for clave, valor in letras.items ( ) :
  print(clave, valor)