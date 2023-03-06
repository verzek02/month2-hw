while True:
    data = int(input('Введите день рождения: '))
    month = int(input('Введите месяц рождения: '))

    if (data >= 21 and data <= 31 and month == 3) or (data >= 1 and data <= 20 and month == 4):
        print('ваш знак зодиака Овен')
    elif (data >= 21 and data <= 31 and month == 4) or (data >= 1 and data <= 21 and month == 5):
        print('ваш знак зодиака Телец')
    elif (data >= 22 and data <= 31 and month == 5) or (data >= 1 and data <= 21 and month == 6):
        print('Ваш знак зодиака Близнецы')
    elif (data >= 22 and data <= 31 and month == 6) or (data >= 1 and data <= 22 and month == 7):
        print('Ваш знак зодиака Рак')
    elif (data >= 23 and data <= 31 and month == 7) or (data >= 1 and data <= 21 and month == 8):
        print('Ваш знак зодиака Лев')
    elif (data >= 22 and data <= 31 and month == 8) or (data >= 1 and data <= 23 and month == 9):
        print('ваш знак зодиака Дева')
    elif (data >= 24 and data <= 31 and month == 9) or (data >= 1 and data <= 23 and month == 10):
        print('Ваш знак зодиака Весы')
    elif (data >= 24 and data <= 31 and month == 10) or (data >= 1 and data <= 22 and month == 11):
        print('Ваш знак зодиака Скорпион')
    elif (data >= 23 and data <= 31 and month == 11) or (data >= 1 and data <= 22 and month == 12):
        print('Ваш знак зодиака Стрелец')
    elif (data >= 23 and data <= 31 and month == 12) or (data >= 1 and data <= 20 and month == 1):
        print('Ваш знак зодиака Козерог')
    elif (data >= 21 and data <= 31 and month == 1) or (data >= 1 and data <= 19 and month == 2):
        print('Ваш знак зодиака Водолей')
    elif (data >= 20 and data <= 31 and month == 2) or (data >= 1 and data <= 20 and month == 3):
        print('Ваш знак зодиака Рыбы')
    else:
        print('Ошибка, вы неправильно ввели дату \n'
          'Пример: 03.03')
