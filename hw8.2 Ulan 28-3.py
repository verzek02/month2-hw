low = 0
high = 100
mid = (low + high) // 2
i = 0
with open('game.txt', 'w', encoding='UTF-8') as file:
    file.write('Угадай цифру\n')

while True:
    print(f"Вы загадали {mid}?")
    user_answer = input(" 'Да' или '<' или '>': ")
    i += 1
    if user_answer.lower() == 'да':
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Попытки: {i}\n")
            file.write(f"Ваше число: {mid}\n")
            file.write(f'Программа завершила задачу:>')
            print("Программа завершено!")
            break
    elif user_answer == '>':
        low = mid
        mid = (low + high) // 2
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"\n Предположение программы: '{mid}' >= Число\n")
    elif user_answer == '<':
        high = mid
        mid = (low + high) // 2
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Предположение программы: '{mid}' <= Число\n")

    else:
        print('Попробуйте еще раз:>')