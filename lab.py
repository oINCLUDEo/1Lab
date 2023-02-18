max_buffer_len = 100
buffer_len = 1
work_buffer = ''
work_buffer_len = buffer_len
num1 = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
num2 = {1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
        5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
        8: 'восемьдесят', 9: 'девяносто'}
num3 = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
        14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
        17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
num4 = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
        5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот',
        9: 'девятьсот'}
num5 = {1: 'одна тысяча', 2: 'две тысячи', 3: 'три тысячи', 4: 'четыре тысячи',
        5: 'пять тысяч', 6: 'шесть тысяч', 7: 'семь тысяч', 8: 'восемь тысяч', 9: 'девять тысяч'}
with open('nums.txt') as file:
    a = file.read(buffer_len)
    if not a:
        print('\n Файл в директории проекта пустой')
        exit()
    while a:
        while '0' <= a <= '9':
            if '0' <= a <= '9':
                work_buffer += a
            a = file.read(buffer_len)
        if len(work_buffer) > 0:
            i = work_buffer
            h = str(i)
            if h.isdigit() and int(h) >= 1:
                if int(h[0]) % 2 != 0 and int(h) % 2 == 0:
                    d = len(i)
                    count = 0
                    if d == 4:
                        if i[count] != '0':
                            print(num5[int(i[count])], end=' ')
                        count += 1
                        d -= 1
                    if d == 3:
                        if i[count] != '0':
                            print(num4[int(i[count])], end=' ')
                        count += 1
                        d -= 1
                    if d == 2:
                        if i[count] != '0':
                            if int(i[count]) == 1:
                                print(num3[int(i[count:])], end=' ')
                                d -= 2
                                count += 2
                            else:
                                print(num2[int(i[count])], end=' ')
                                d -= 1
                                count += 1
                        else:
                            d -= 1
                            count += 1
                    if d == 1:
                        if i[count] != '0':
                            print(num1[int(i[count])], end=' ')
                        d -= 1
                    print()
        work_buffer = ''
        a = file.read(buffer_len)