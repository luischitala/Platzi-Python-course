

def protected(func):

    def wrapper(password):

        if password == 'Platzi':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


@protected

def protected_func():
    print('Your password is correct.')

if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    protected_func(password)