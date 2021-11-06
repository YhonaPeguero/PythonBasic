def  decorador(func): 
  def nueva_funcion():
    print("Vamos a ejecutar la funcion")
    func()
    print("Se ejecuto la funcion")

  return nueva_funcion

@decorador
def saluda():
  print("Hola Mundo")

saluda()