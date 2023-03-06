data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letters = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
del numbers[0]
letters.append(numbers[0])
numbers.insert(2, 2)
del numbers[0]
numbers.sort()
letters.reverse()
letters[-2] = 'c'
letters[1] = 'G'
numbers = [i ** 2 for i in numbers]
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)
