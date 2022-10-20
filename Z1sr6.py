'Zadanie1'
razmer=int(input('Введите размерность массива: '))
C=[0] * razmer #Заполняем массив нулями
from random import uniform #Подключаем функцию uniform
for i in range(razmer): #Перебираем индексы
    C[i]=uniform(1,155) #Случайные числа от 1 до 155
print('Исходный массив:', C)
def large(n): #Создаем функцию, которая находит максимальный элемент массива
    max_=n[0]
    for ele in n:
        if ele>max_:
            max_=ele
    return max_
print('Максимальный элемент: ', large(C)) #Выводим максимальный элемент массива
for i in range(razmer): #Перебираем индексы
    if C[i]==large(C):  #Находим максимальный элемент
        for i in range(i+1, razmer): #Перебираем индексы
             C[i]=0  #Делаем все элементы массива, стоящие после максимального элемента, нулями
print('Конечный массив: ', C)