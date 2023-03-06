import time as t

mat = 1000
while mat > 5:
    t.sleep(0.5)
    mat -= 7
    print(f'{mat+7}-7 = {mat}')
print('Я гуль')