import json

json_string = '{"foo": "bar"}'
print(json.loads(json_string))

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    salaries_json = json.dumps(salaries)
    return salaries_json

salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])