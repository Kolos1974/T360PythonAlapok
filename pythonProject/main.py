# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


my_int = 4

print(type(my_int))

my_float = 3.14
print(type(my_float))

my_float2 = float(5)
print(type(my_float2))


boolean = False
print(type(boolean))
print(boolean)

nothing = None
print(nothing)

komplex = 1j
print(komplex)
print(type(komplex))

print(f' Szöveges formázott {150 + 65} értékű üzenet')

szoveg = 'Valami szöveg'
print(len(szoveg))


## Az első karaktertől 10 karakterig minden 2 karakter
print(szoveg[0:10:2])

## tagolt szöveg
print(szoveg.split(' '))

## Összefűzött szöveg
print("".join(['Összefűzött',' ','szöveg']))


a = 11
b = 3
## Eredménye 3.6666666666666665
print(a/b)

## Eredménye 3
print(a//b)

## Eredménye 2
print(a%b)

if (5>3):
    print('5 nagyobb mint 3')





