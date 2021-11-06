#Modos de apertura de archivos:
# r ( read )
# w ( write )
# a ( append - añadir )
# Agregar un + incluye leer. Por ejemplo, w+ es leer y escribir.
with open ("frases_famosas.text", "r") as file: 
  for linea in file:
    print("=== Frase ===")
    print(linea)

# notas = {
#   "Nora" : 87,
#   "Gino" : 100,
#   "Loretto" : 60,
#   "Talina" : 50
# }

# with open ("data_estudiante.txt", 'w') as archivo:
#   for nombre, nota in notas.items():
#     archivo.write(nombre + " - " + str(nota) + "\n")


# nuevas_notas = {
# 	"Emily" : 60,
# 	"Daniel" : 90,
# 	"Julienne" : 70
# }

# with open ("data_estudiantes.txt", 'a') as archivo:
#   for nombre, nota in nuevas_notas.items():
#     archivo.write(nombre + " - " + str(nota) + "\n")