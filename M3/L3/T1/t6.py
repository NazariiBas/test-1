'''
Визначіть швидкість, з якою пробіг спортсмен.
Перед Вами програма, яка використовує функцію run () з попередньої задачі.
Підключіть модуль olympic і запустіть програму. 
Якщо модуль olympic написаний правильно,
програма виведе в якості результату швидкість спортсмена.
'''

from olympic import *
s = int(input("Введіть відстань дистанції:"))
t = int(input("Введіть витрачений час на дистанцію:"))
print(run(s, t))
