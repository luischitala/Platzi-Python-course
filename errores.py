
countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Escribe el nombre un pais: ')).lower()
    print('La poblacion de {} es: {} millones'.format(country, countries[country]))