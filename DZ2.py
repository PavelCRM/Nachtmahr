#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

#x = input('Введите число ')
#def summa(x):                      
#    if float(x) < 0:                            
#        x = float(x) * (-1)
#    number = 0
#    for i in str(x):
#        if i != '.':
#            number += int(i)
#    return number
#print(f'Сумма чисел равна {summa(x)}')

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

#n = int(input('Введите число: '))
#factorial = 1
#for i in range(1, n+1):
#    factorial *= i
#print(factorial)

#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

#k = int(input('Введите число: ')) 
#def get_squerence(k):
#    return [round((1 + 1 / x)**x, 5) for x in range (1, k + 1)]
#nums = get_squerence(k)
#print(nums)


#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем через пробел позициях

#from random import randint

#numbers = []
#for i in range(10):
#    numbers.append(randint (-10,10))
#print(numbers)

#def get_numbers(numbers):
#    count =0 
#    for element in numbers:
#        count +=1
#    return count
#print('Number of elements: ', get_numbers(numbers))

#x = int(input('Enter  position of first element: '))
#y = int(input('Enter position of second element: '))

#for i in range(len(numbers)):
#    mult = numbers[x -1]*numbers[y - 1]
#print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

#Реализуйте алгоритм перемешивания списка

#import random
#lst = [random.randint(0,10) for i in range(random.randint(5,20))]
#print(f"исходный список:\n {lst}")
#random.shuffle(lst)
#print(f"список после перемешивания:\n{lst}")








