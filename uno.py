alumnos = {"1": "Luis Ernesto Roman Chitala", "2" : "Mario Alberto", "3": "Jesus"}

alumno = {0: {"nombre": "Cesar Iban", "apellido": "roman chitala"}}

print("-"*100)
print(alumno.get)
print("-"*100)

for a in alumnos.values():
    print(a)

for k,v in alumnos.items():
    print(k,v)