def multiplication (*args):
    result = 1
    for i in args:
        result *= i
    return result


print(multiplication (2,3,4,5))

def stroka (word = 'hello'):
    return word == word[::-1]

print(stroka())

def calculator (a, operator, b):
    if operator == '-':
        return a - b
    elif operator == '+':
        return a + b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '%':
        return a % b
    elif operator == '**':
        return a ** b


