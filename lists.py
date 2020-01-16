my_list = [1, 2, 3]
print(my_list[1:])

my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

#elimina el último elemento
print(my_list.pop())
print(my_list)

for element in my_list:
    print(element)

a = [1, 2, 3]
b = a

#side-effects
c= [a,b]
a.append(5)

print(c)


a = [1, 2, 3]
b = a
#clone lists
c = list(a)

my_list = list(range(100))
print(my_list)

double = [i * 2 for i in my_list]
print(double)

pares = [i for i in my_list if i % 2 == 0]
print(pares)