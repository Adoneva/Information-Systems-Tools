# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print('Задание 4(A)')
# a = 5.7
# b = int(a)
# print(b)
# print('\n')
# print('Задание 4(Б)')
# a = -5.7
# b = int(a)
# print(b)
# print('\n')
# print('Задание 4(В)')
# a = 3**39
# b = float(3**39)
# c = int(b)
# d=a-c
# print(d)
# print('\n')
# #Задача 5.
# print('Задание 5')
# name = input("Как вас зовут?"'\n')
# print("Привет,", name, "!Bhb")
# print('\n')
#  #Задача 6.
# print('Задание 6')
# print("Введите количетсво часов:")
# x=int(input())
# print("Введите количество минут:")
# y=int(input())
# print(x*60+y)
# print('\n')
#
# print('Задание 6*')
# x, y = [int(input()) for _ in range(2)]
# print(60*x+y)
# print('\n')
#Задача 7.
# print('Задание 7')
# a= False
# b= True
# c= False
# s='((not a or b) and c)'
# print(eval(s.lower()))
# print('\n')
# #Задача 8.
# print('Задание 8')
# year = int(input("Введите год:"))
# if  year < 1900 or year > 3000:
#  print("Год вне диапазона")
# elif year%4 == 0 and year%100 != 0 or year%400 == 0:
#  print("С днем рождения!")
# else:
#  print("Год обычный")
# print('\n')

#  #Задание 10
# print('Задание 10')
# a = []
# while True:
#     num = int(input("Введите значение: "))
#     if num == 0:
#         print(sum(a))
#         break
#     a.append(num)
# print('\n')
# #Задача 11.
# print('Задание 11')
# print("Введите X = ")
# x = int (input ())
# print("Введите Y = ")
# y = int (input ())
# for i in range (x*y):
#     i+=1
#     if i%x==0 and i%y==0:
#         print ('Пицца разрезана на', i ,'кусков')
#         break
# print('\n')
# #Задание 12
# print('Задание 12')
# for num in range(20):
#     if (num & 1) != 1:
#         print(num, end=' ', sep=' ')
# print('\n')
# #Задание 14
# print('Задание 14')
# def spiralFill(m, n, a):
#     val = 1
#     k, l = 0, 0
#     while (k < m and l < n):
#
#         for i in range(l, n):
#             a[k][i] = val
#             val += 1
#         k += 1
#
#         for i in range(k, m):
#             a[i][n - 1] = val
#             val += 1
#         n -= 1
#
#         if (k < m):
#             for i in range(n - 1, l - 1, -1):
#                 a[m - 1][i] = val
#                 val += 1
#             m -= 1
#
#         if (l < n):
#             for i in range(m - 1, k - 1, -1):
#                 a[i][l] = val
#                 val += 1
#             l += 1
#
# if __name__ == '__main__':
#     m, n = 4, 4
#     a = [[0 for j in range(n)] for i in range(m)]
#     spiralFill(m, n, a)
#     for i in range(m):
#         for j in range(n):
#             print(a[i][j], end=' ')
#         print(' ')
# print('\n')
#Задание 15
print('Задание 15')
import time
from tkinter import messagebox
if __name__ == '__main__':
    while True:
        messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')
        time.sleep(10)