# ВИДЕОЗАПИСЬ УРОКА 8: https://www.youtube.com/watch?v=AbY26EcF-y0
# Работа с файлами.
# w - режим записи, перезаписи (write)
# a - режим добавления (add)
# x - режим бесконфликтной записи
# r - режим чтения
from random import choice
students_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17]
topics = [1, 2, 3, 4, 5, 6, 7, 8]


with open('results.txt', 'w') as file:
    file.write('results 28-3')

while len(students_ids) != 0:
    chosen_student = choice(students_ids)
    chosen_topic = choice(topics)
    name = input(f'name for {chosen_student}'
                 f' topic: {chosen_topic}').title()
    try:
        rate = int(input(f'rate for {name}: '))
        with open('results.txt', 'a') as file:
            file.write(f'\nname: {name} topic: {chosen_topic}: '
                       f'rate: {rate}')
            students_ids.remove(chosen_student)
    except:
        print('только числа от 0 до 10')








# from time import sleep
#
# with open('file.txt') as file:
#     for i in file.readlines():
#         sleep(2.5)
#         print(i, end='')

    # print(file.readlines()[2])





# with open('file.txt', 'r') as file:
#     file_objects = file.readlines()
    # print(file.read())

# data = dict(enumerate(file_objects))

# for i in file_objects:
#     data[file_objects.index(i)] = i
#
# print(data)

# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('file.txt', 'w', encoding='UTF-8') as file:
#     file.write('\nвторая строка')
#
# with open('new.txt', 'a', encoding='UTF-8') as file:
#     file.write('\nчто-то добавили')
#
# with open('new.txt', 'x', encoding='UTF-8') as file:
#     file.write('создать новый файл')
