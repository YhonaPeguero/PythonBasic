list = (1,2,3,4,5,6,7,8,9,10)

for value in list:
  pass

new_range = range(10,50, 10)
for value in new_range:
  print(value)


for index,value in enumerate(list):
  print(value, "tiene el indice",)
  index +=1

for value in range(0, len(list)):
  print( len(list))