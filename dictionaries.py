my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50,
}

print(my_dict['David'])
my_dict.get('Juan', 30)
my_dict.get('David', 30)
my_dict['Jaime'] = 20
my_dict['Pedro'] = 70
print(my_dict)

del my_dict['Jaime']
print(my_dict)

for llave in my_dict.keys():
    print(llave)

for value in my_dict.values():
    print(value)

for llave, valor in my_dict.items():
    print(llave,valor)

print('David' in my_dict)
