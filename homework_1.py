import random
# aaaaaaaaa
# 1
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {i: i * i for i in keys}
print(result)
# 2
my_list = [i for i in range(100) if i % 2 == 0]
print(my_list)
# 3
my_str = 'бессмысленный и тусклый свет'
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
for i in list(my_str):
    if i in vowels or i == ' ':
        continue
    else:
        my_str = my_str.replace(i, random.choice(vowels))

print(my_str)
# 4
my_mass = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

my_mass = list(dict.fromkeys(my_mass))
print(my_mass)
copy_mass = my_mass.copy()
max_el = []
count = 0
i = 0
while count < 3:
    if i not in max_el:
        max_el.append(max(copy_mass))
        copy_mass.remove(max(copy_mass))
        i += 1
        count += 1

print(max_el)


def minlist(my_list):
    minim = my_list[0]
    for i in my_list:
        if i < minim:
            minim = i
    return minim


print(my_mass.index(minlist(my_mass)))
my_mass.reverse()
print(my_mass)
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
similar = []
for key in dict_one.keys():
    for k in dict_two.keys():
        if key == k:
            similar.append(key)
print(similar)
