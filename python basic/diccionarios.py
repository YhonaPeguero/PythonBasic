#Los diccionarios son mutables.
#Acceder a un valor de un diccionario.
edades = {"Gino": 15, "Nora" : 45}
edades ["Gino"]
#Otra alternativa es usando el metodo get.
edades.get("Gino")

#Modificar valor en un diccionario.
#Si la clave ya existe, se reemplaza.
edades = {"Gino": 15, "Nora" : 45}
edades ["Yhona"] = 23 

#Para borrar.
edades = {"Gino": 15, "Nora" : 45, "Yhona": 23}
del edades ["Yhona"]

#Revisar la existencia de un elemento en el diccionario.
edades = {"Gino": 15, "Nora" : 45}
"Gino" in edades

