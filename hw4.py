# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
# def dec(fun):
#     def wrapper(*args):
#         result = fun(*args) % 100
#         if result == 0:
#             return "We are Ok!"
#         else:
#             return f"Bad news guys, we got {result}"
#
#     return wrapper
#
#
# @dec
# def sum(a, b):
#     return a + b


# print(sum(100, 101))

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))
# def decor(fun):
#     def wrapper(*args):
#         for arg in args:
#             if isinstance(arg, int):
#                 return fun(*args)
#             elif isinstance(arg, str):
#                 raise ValueError('stringtype is not supported')
#     return wrapper
#
#
# @decor
# def mul(a, b):
#     return a * b
#
#
# print(mul('a', 2))

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.
def my_cache(func):
    cache = {}
    counter_cache = {}
    counter_fun = {func.__name__: 0}

    def wrapper(*args):
        for arg in args:
            if arg not in cache:
                cache[arg] = func(*args)
                counter_cache[arg] = 0
                counter_fun[func.__name__] += 1
                return f'Function executed with counter = {counter_fun[func.__name__]}, function result = {cache[arg]}'
            else:
                counter_cache[arg] += 1
                return f'Used cache with counter = {counter_cache[arg]}'

    return wrapper


@my_cache
def my_args(a):
    return a ** 2


print(my_args(2))
print(my_args(2))
print(my_args(2))
print(my_args(3))
print(my_args(3))
print(my_args(3))
