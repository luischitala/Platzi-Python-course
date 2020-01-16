my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

my_range == my_other_range

for i in my_range:
    print(i)

for i in my_other_range:
    print(i)

print(id(my_range))

my_range is my_other_range


for i in range(0, 101, 2):
    print(i)

for i in range(1, 100, 1):
    if i % 2 !=0:
        print(i)