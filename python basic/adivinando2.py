import random

random.randint(1,10)

number = random.randint(1,10)
intentos = 0

jugar = True
print ("Adivina un numero del 1 al 10")

while jugar :
  intentos += 1

  if intentos <= 5 :
    elegir = int (input  ("Ingrese un número: "))
    if elegir == number :
      print("acertaste! has necesitado", intentos, "intentos. ")
      jugar = False
    elif elegir > number:
        print("Es muy alto. Llevas", intentos, "intentos.")
    elif elegir < number:
          print("Es muy bajo. Llevas", intentos, "intentos. ") 
  else:
      print("Se acabaron los intentos. Has perdido. ")
      jugar = False