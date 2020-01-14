import csv

archivo = csv.reader( open("datos.csv",  encoding="utf8") )


for a in archivo:
    print(a[1].lower())
    print("".join(a[1].split("")))
