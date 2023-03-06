monday = float(input('расходы на понедельник: '))
tuesday = float(input('расходы на вторник: '))
wednesday = float(input('расходы на среду: '))
thursday = float(input('расходы на четверг: '))
friday = float(input('расходы на пятницу: '))
saturday = float(input('расходы на субботу: '))
sunday = float(input('расходы на воскресенье: '))

average = (monday + tuesday + wednesday + thursday + friday + saturday + sunday) / 7
print('среднее значение- ', round(average, 1))
