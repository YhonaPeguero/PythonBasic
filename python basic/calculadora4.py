def Menu():
    # Funcion que Muestra el Menu
    print
# Calculadora
# Menu
# 1) Suma
# 2) Resta
# 3) Multiplicacion
# 4) Division
# 5) Salir"""
def Calculadora():
    # Funcion Para Calcular Operaciones Aritmeticas
    Menu()
    opc = int(input("Selecione opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print ("La suma es:", x+y)
            opc = int(input("Selecione opcion\n"))
        elif(opc==2):
            print ("La resta es:",x-y)
            opc = int(input("Selecione opcion\n"))
        elif(opc==3):
            print ("La multiplicacion es:",x*y)
            opc = int(input("Selecione opcion\n"))
        elif(opc==4):
            try:
              print ("La division es:", x/y)
              opc = int(input("Selecione opcion\n"))
            except ZeroDivisionError:
              print ("No se permite la division entre 0")
              opc = int(input("Selecione Opcion\n"))
        else:
            print("Alerta, favor ingresar un numero. ")
Calculadora()

