Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del Geeks['bag']
Geeks['address'] = 'Ibraimova 103'
Geeks['contacts'] = '+996507052018', '@geeks_edu'
Geeks['courses'] += 'ios', 'UX/UI', 'Основы пограммирования'
Geeks['courses'] = set(Geeks['courses'])
Geeks['Foundation date'] = '2018'
Geeks['amount of courses'] = len(Geeks['courses'])
for i in Geeks:
    print(f' {i} : {Geeks[i]}')
print(Geeks.items())

