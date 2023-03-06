ten = list(range(1,11))

evens = list[0:11:2]

print(evens)

    squares = list(map(lambda x: x**2, evens))

    print(squares)

    def print_list_element(list=ten):
        while True:
            try:
                index = input('Введите индекс элемента списка (для выхода из программы введите "exit"): ')
                if index == 'exit':
                    break
                else:
                    index = int(index)
                    if index >= len(list):
                        raise IndexError
                    else:
                        print(list[index])
            except ValueError:
                print('Некорректное значение. Введите целое число')
            except IndexError:
                print('Введенный индекс не существует. Введите целое число в диапазоне от 0 до 9')

    print_list_element()