phonebook = {}

phonebook["John"] = 999999999
phonebook["Mary"] = 888888888
phonebook["Dave"] = 777777777

print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["John"]
print(phonebook)

phonebook.pop("Dave")
print(phonebook)