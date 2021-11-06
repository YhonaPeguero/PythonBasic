
def identificador ():
  cars = [

  {"Modelo": "audi","año": 2020, "Precio": 190.000,"velocidad": "305 km/h"},
  {"Modelo": "BMW","año": 2019, "Precio": 130.000,"velocidad": "250 km/h"},
  {"Modelo": "Ford","año": 2021, "Precio": 220.000,"velocidad": "483 km/h"},
  {"Modelo": "Honda","año": 2010, "Precio": 110.000,"velocidad": "200 km/h"},
  {"Modelo": "Hyndai","año": 2001, "Precio": 100.000,"velocidad": "200 km/h"}

  ]

  if cars < 2019 and cars < 150.000 :
      print("El auto es mas viejo y el precio es mas bajo. ")
  elif cars > 2018 and cars > 190.000 :
      print("El auto es mas nuevo y el precio es mas alto. ")
  elif cars < 150.000 :
      print("El auto es mas bajo. ")
  else :
      print("Auto no disponible. ")

print(identificador)