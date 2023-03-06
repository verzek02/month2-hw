# словари - dict, множества - set
# dictionary
# {key: value}

# menu = {
#     'beshbarmak': {"мясо", "лапша", "лук"},
#     'plov': {"рис", "мясо", "морковь"},
#     'eggs': {'egg', 'tomato'}
# }
#
# while True:
#     choose_option = input('choose: \n'
#                           '1) search_by_name\n'
#                           '2) search_by_ingridient: ')
#
#     if choose_option == 'exit':
#         break
#
#     if choose_option == '1':
#         food_name = input('введите название блюда: ').lower()
#         if food_name in menu:
#             print(menu[food_name])
#         else:
#             print('мы не нашли такого блюда \n'
#                   f'возможно вам будет интересно: {tuple(menu.keys())}')
#
#     elif choose_option == '2':
#         ingridient = input('enter ingridient: ')
#         for name, ingridients in menu.items():
#             if ingridient in ingridients:
#                 print(name)
#     else:
#         print('only 1 or 2 or exit')


# word = 'programmer'
#
# while True:
#     user_answer = input('ввведите слово: ').lower()
#
#     if user_answer == word:
#         print('всё правильно!', word)
#     else:
#         if set(user_answer).issubset(word):
#             print(f'возможно вы хотели написать {word}')
#         else:
#             print('вы написали неверно!')


#
# print(beshbarmak.union(plov))
# print(beshbarmak | plov)
#
# print(beshbarmak.difference(plov))
# print(beshbarmak - plov)
#
# print(beshbarmak.intersection(plov))
# print(beshbarmak & plov)
#
# print(beshbarmak.symmetric_difference(plov))
# print(beshbarmak ^ plov)


# a = set('programmer')
# print(len(a))

# lst = [1, 2, 3, 2, 4, 5, 1]
# lst1 = {1, 2, 3, 2, 4, 5, 1}

# # print(lst)
# print(lst1[0])
# print(type(lst1))


# new = dict([[1, 'one'], [2, 'two'], [3, 'three']])
# new = dict(enumerate('python'))
# print(new)
# new = dict(name='azat', age=21, country='kg')
#
# student = {
#     'name': 'Miras',
#     'age': 16,
#     'height': 1.80,
#     'married': False,
#     'hobby': ['english', 'chess', 'football'],
#     'education': ('school', 'college', 123345),
# }

# print(student.items())
# for k, v in student.items():
#     print(k, '=>', v)

# for i in student:
#     print(i, ':', student[i])

# print(student)

# print(student.get('name', 'такого ключа нет'))


'''удаление'''
# deleted = student.pop('married')
# print(deleted)
# del student['hobby']
# del student['hobby'][1]

'''изменение'''
# student['age'] += 1
# student['married'] = True
# student['education'] = list(student['education'])
# student['hobby'][0] = 'chinese'

'''добавление'''
# student['nation'] = 'kg'
# student['hobby'].append('python')
# student.update(new)
# new.update(student)




# print(student)



# print(student['hobby'])


# print(student.keys())
# print(student.values())

# print(type(student))

# names = ['askar', 'bekbolot', ['miras', 16, 'male'], 'nurbol', 'jetigen']
# print(names[2])


# week_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# data = {}
# for day in week_days:
#     data[day.upper()] = int(input(f'расхлды за {day.upper()}'))
# print(
#     f'{data}\n'
#     f'average: {sum(data.values()) // len(data)}'
# )