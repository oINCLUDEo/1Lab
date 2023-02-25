# Вариант 11. Натуральные числа, начинающиеся с нечетных цифр. Четные цифры выводить словами.
max_buffer_len = 100
buffer_len = 1
work_buffer = ''
work_buffer_len = buffer_len
num1 = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
k = False
with open('nums.txt') as file:
    a = file.read(buffer_len)
    if not a:
        print('\n Файл в директории проекта пустой')
        exit()
    while a:
        while '0' <= a <= '9' or a.isalpha():
            if '0' <= a <= '9' or a.isalpha():
                work_buffer += a
            a = file.read(buffer_len)
        if len(work_buffer) > 0:
            h = str(work_buffer)
            if h.isdigit() and int(h) >= 1 and int(h[0]) % 2 != 0:
                k = True
                for i in h:
                    if int(i) % 2 == 0:
                        print(num1[int(i)], end=' ')
                    else:
                        print(i, end=' ')
                print()
        work_buffer = ''
        a = file.read(buffer_len)
if not k:
    print('В файле нет подходящих под условие чисел')