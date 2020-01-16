

def fibonacci():

    """ Serie Fibonacci
    recibe un numero entero

    """
    n = int(input('Digite un numero entero '))

    a =0
    b=1

    for i in range(n):

        print(a)

        c=a+b
        a=b
        b=c

if __name__ =='__main__':
    
    fibonacci()