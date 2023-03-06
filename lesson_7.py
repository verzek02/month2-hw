# lambda, и работа с исключениями
# lambda arguments: expression

# try:
#     code
# except:
#     code
#     message
# finally:
#     code
#     message

from random import choice

students_ids = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15]

data = {}

while len(students_ids) != 0:
    print(f'осталось: {len(students_ids)}')
    chosen_student = choice(students_ids)
    name = input(f'name for {chosen_student}: ').title()
    try:
        rate = int(input(f'rate for {name}: '))
        if rate not in range(1, 11):
            print('rate must be in 1 to 10')
            continue
        else:
            data[name] = rate
            students_ids.remove(chosen_student)
    except:
        print('rate must be integer')

for name, rate in data.items():
    print(name, ' : ', rate)




# word = 'Kyrgyzstan'
# while True:
#     try:
#         index_letter = int(input('введите индекс: '))
#         print(word[index_letter])
#     except:
#         print('индекс неверный, только цифры')
    # except IndexError:
    #     print('индекс неверный')
    # except ValueError:
    #     print('только цифры')


# try:
#     print(2 + 2)
# except:
#     print('типы данных не соответствуют')
# finally:
#     print('проверка завершена')


# print(2 + '2')
# print(int('2sdf'))
# print('234'[4])


# print('2' + '2')
# print(2 + 2)
# print(2 * 4)
# print((1, 2, 3) * 2)


# map, filter
# numbers = list(range(1, 16))
# print(numbers)

# numbers_mapped = list(map(lambda n: [n], list(range(1, 101))))
# numbers_mapped = [i * 2 for i in numbers]
# print(numbers_mapped)numbers_mapped

# filtered_numbers = list(filter(lambda n: n > 7, numbers))
# filtered_numbers = [i for i in numbers if i > 7]
# print(filtered_numbers)


# func_l = lambda a, b: a + b
#
# def func_d(a, b):
#     return a + b
#
# print(type(func_l))
# print(type(func_d))


# def up_letter(word: str):
#     return word.title()
#
#
# def show_words(func, sequence):
#     for i in sequence:
#         print(func(i))
#
#
# words = ['python', 'geeks', 'bishkek']
# show_words(lambda word: word.upper(), words)


# show_words(up_letter, words)
# show_words(len, words)


# Мирас  :  8
# Жетиген  :  6
# Бекболот  :  1
# Ислам  :  9
# Батырхан  :  6
# Даниель  :  11
# Жаннат  :  10
# Аскар  :  7
# Арген  :  1
# Улан  :  7
# Абил  :  7
# Нурбол  :  5