import json

x = '{"name":"khadeeja","age":22}'

# y = json.loads(x) 
# print(y["age"])
  #prints 22


y=json.dumps(x)
print(y)
print(type(y))