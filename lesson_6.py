# 6. Функции, аргументы: *args, **kwargs - keyword arguments.
# DRY - don't repeat yourself
# def - definition (определить)

# sum, min, max

# lst = [2, 4, 1, 3, 7]
#
#def max1(sequence: [list, tuple]) -> int
    #print(max1.__doc__)

    """Эн чон санды табат."""
 #   max_value = sorted(sequence)[-1]
  #  return max_value


# print(help(max1))


    # max_value = lst[0]
    # for i in sequence[1:]:
    #     print(max_value, i)
    #     if max_value > i:
    #         max_value = max_value
    #     else:
    #         max_value = i
    # return max_value

# print(max1((23, 12, 34, 25, 10)))




# def menu(**kwargs):
#     return kwargs
#
# monday = menu(drink='tea', food='pizza', desert='cake')
# print(monday)


# def plus(*args):
#     print(args)
#     return sum(args) / len(args)
#
#
# print(plus(2, 4, 6, 9, 5))




'''схема функции'''
# определение наименование(параметры):
#     тело функции
#     возвращение результата
# вызов функции(аргументы)


# def len1(sequence):
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter


# print(len1('34534'))
# print(len1((23, 45, 56, 67)))
# print(len('python') + 4)


# print(len1('qwerty') + 4)


# def greet(name: str, age: int, surname='unknown'):  # name required positional argument
#     print('hello', name, surname, age, "лет")
#
#
# greet('azamat', 21, 'alymkulov')
# greet(age=19, name='tilek')  # keyword arguments


# def get_square(width=1, length=1):
#     if not isinstance(width, (int, float)):
#         return 'укажите цифры в параметрах'
#     return width * length
#
# square_3 = get_square('2.4', 2)
# print(square_3)
# print(square_3)
# square_hall = get_square(10, 20)
# print(square_3, square_hall, sep='\n')

# width = 5
# length = 8
# square_3 = width * length
# print(square_3)
#
# width = 10
# length = 20
# square_hall = width * length
# print(square_hall)
