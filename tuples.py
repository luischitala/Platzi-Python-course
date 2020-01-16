my_tuple = (1,)
print(type(my_tuple))
my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
print(my_tuple)

# Reasignación de tuplas
x, y, z = my_other_tuple

def coordenadas():
    return(5,4)

coordenada = coordenadas()
print(coordenada)
