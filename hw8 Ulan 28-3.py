with open('results.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

results = {}
for i in lines[1:]:
    name, topic, rate = i.split()[1], i.split()[3], i.split()[5]
    results[name] = {'topic': topic, "rate": int(rate)}

sorted_results = sorted(results.items(), key=lambda x: x[1]['rate'], reverse=True)
print('Топ-3 лучших студента по оценке:')
for i, (name, results) in enumerate(sorted_results[:3], 1):
    print(f'{i}, {name}: {results["topic"]} {results["rate"]}')

with open('sorted_results.txt', "w", encoding='UTF-8') as file:
    file.write('results 28-3\n')
    for name, result in sorted_results:
        file.write(f'name: {name} topic: {result["topic"]}: rate: {result["rate"]}\n')

with open('sorted_results.txt', encoding='UTF-8') as file:
    print(f'Содержимое файла sorted_results.txt:\n{file.read()}')