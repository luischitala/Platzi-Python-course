import random

def binary_search(numbers,number_to_find,low,high):
  
    if low > high:
      return False
    
    mid = (low + high) // 2
    
    if numbers[mid] == number_to_find:
      return True
    elif numbers[mid] > number_to_find:
      return binary_search(numbers,number_to_find,low,mid-1)
    else:
      return binary_search(numbers,number_to_find,mid + 1,high)
    
    
    
    

if __name__ == "__main__":
    large = 0
    numbers = []

    while large <= 10:
      numbers.append(random.randint(1,100))
      large += 1
      
    numbers.sort()
      
    print(numbers)
    
    number_to_find = int(input('Indica el número que quieres buscar: '))
    
    result = binary_search(numbers,number_to_find,0,len(numbers)-1)
    
    if result is True:
      print('El número {} si esta en la lista.'.format(number_to_find))
    else:
      print('El número {} no esta en la lista.'.format(number_to_find))