#json= javascript notaion
# rojan is a syntax for string and exanging data.

#json is text, written and javascript object notation.

#python object = everything in python is objcect ie. list, dictionary, set etc.


# json object

# pyton hah a built-in package called json, which can be used to work json data.

import json
#some example of json

x='{"name":"john","age":14,"city":"nework"}'

#parse x:
y=json.loads(x)
print(y["age"])
print(y["name"])