# 1)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 1.1) отсортировать массив из словарей по значению ключа ‘age' 
# 1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :
city = []
result = {}

def myfunc(e):
    return e['age']


data.sort(key=myfunc,reverse=True)
print(data)


for i, j in enumerate(data):
    result.setdefault(data[i]['city'], []).append({'name': data[i]['name'], 'age': data[i]['age']})

print(result)


# result = {
#     'Kiev': [
#         {'name': 'Viktor', 'age': 30},
#         {'name': 'Andrey', 'age': 34}],
#
#     'Dnepr': [{'name': 'Maksim', 'age': 20},
#               {'name': 'Artem', 'age': 50}],
#     'Lviv': [{'name': 'Vladimir', 'age': 32},
#              {'name': 'Dmitriy', 'age': 21}]
# }


# =======================================================
# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

def most_frequent(list_var):
    counter = 0
    el = 0
    for i in list_var:
        current = list_var.count(i)
        if current > counter:
            counter = current
            el = i
    return el


print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))
# 2 способ
s = ['a', 'a', 'bi', 'bi', 'bi']
print(max(s, key=s.count))




# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.
num = 123405
num = str(num)
counter = None
for i in num:
    if i != '0':
        if counter is None:
            counter = int(num[0])
        else:
            counter *= int(i)


print(counter)


# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
def some_function(array, n):
    if n <= len(array):
        count = array[n] ** n
        return count
    return -1

array = [i for i in range(10)]
print(some_function(array, 3))

# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
my_str = "hello 1 one two three 15 world"
count = 0
alpha_in_row = []
for i in my_str.split():
    if i.isalpha():
        count += 1
    else:
        alpha_in_row.append(count)
        count = 0

print(max(alpha_in_row))


