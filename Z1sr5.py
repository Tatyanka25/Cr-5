'Zadanie1sr5'
sist=int(input('Введите систему счисления: ')) #Вводим с клавиатуры нужную систему счисления
number=int(input('Введите число в десятичной системе счисления: ')) #Вводим с клавиатуры число
def print_bin(p): #Создаем функцию, которая переводит число в двоичную систему счисления (разрядность 8 бит)
    m=128
    while m>0:
        d=p//m
        print(d, end="")
        p=p%m
        m=m//2
def print_eig(p): #Создаем функцию, которая переводит число в восьмиричную систему счисления (разрядность 8 бит)
    m=2097152
    while m>0:
        d=p//m
        print(d, end="")
        p=p%m
        m=m//8
if (sist==2) or (sist==8): #Проверяем, ввел ли пользователь нужную систему счисления
    if (0<=number) and (number<=255): #Проверяем, ввел ли пользователь число, которое может быть переведено с 8-ми битной разрядностью
        if sist==2:
            print_bin(number) #Переводим число в двоичную систему, если пользователь ввел систему счисления 2
        else:
            print_eig(number) #Переводим число в восьмиричную систему, если пользователь ввел систему счисления 8
    else:
        print('Ошибка')
else:
    print('Ошибка')