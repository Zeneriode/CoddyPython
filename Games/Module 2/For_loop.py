a = 'Name'  # просто инициализируем переменные для работы с ними
b = 10

for i in a:  # проходим по каждому символу в строке
    print(i)

for i in range(b):  # проходим по каждому числу от 0 до b
    print(i)

for i in range(2, b, 3):  # проходим по каждому числу от 2 до b с интервалом 3
    print(i)

for i in range(len(a)):  # проходим по каждому числу от 0 до числу, равному длине строки a
    print(i)

for i in range(5):  # берем по очереди числа от 0 до 5
    for j in range(0, 9, 2):  # берем по очереди числа 0, 2, 4, 6 и 8
        print(i + j / 10)  # выводим все числа с интервалом 0.2

print(*set(i for i in range(b)))  # более коротка форма вывода чисел от 0 до b