import json

data = {"name": "python", "age": 18}
r = json.dumps(data)
print(type(r))
print(r)
a = '{"city":"shanghai","country":"china"}'
d = json.loads(a)
print(type(d))
print(d)
print(d["city"])
