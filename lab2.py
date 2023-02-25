# Вариант 11. Натуральные числа, начинающиеся с нечетных цифр. Четные цифры выводить словами.
import re

num = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
       6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
k = False
with open('nums.txt') as file:
    file = file.readline().split()
if not file:
    print('\nФайл в директории проекта закончился')
    exit()
for j in file:
    h = re.findall(r'\b[13579]\d+\b|\b[13579]\b', j)
    if h:
        k = True
        for i in h[0]:
            if int(i) % 2 == 0:
                print(' ' + num[int(i)], end=' ')
            else:
                print(i, end='')
        print()
if not k:
    print('Подходящих под условие чисел не нашлось')

