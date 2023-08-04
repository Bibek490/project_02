#pyhton to josn
# create python object and convert it into json


import json
 #python object is here
x={
  "name":"john",
  "age":30,
  "city":"kathmandu"
 }

#python object lai json ma convert garne

y=json.dumps(x)

print(y)
