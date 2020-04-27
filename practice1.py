# 1) Get a string from a given string where all occurrences of its 
# first char have been changed to '$', except the first char itself.
### aaaaaaa

def replace(my_str):
    first_el = my_str[0]
    my_str = my_str.replace(first_el, '$')
    my_str = f'{first_el}{my_str[1:]}'
    return my_str


my_str = "test"
print(replace(my_str))


# 2)Add 'ing' at the end of a given string (length should be at least 3 )
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged. 
def add_ing(my_str):
    if len(my_str) >= 3:
        if my_str.endswith("ing"):
            my_str += "ly"
        else:
            my_str += "ing"
    return my_str


my_str = "read"
print(add_ing(my_str))
# Task1
# Take a string with a couple words and returns the length of the longest word.
string = 'one two three four five'
max_length = []
for i in string.split():
    max_length.append(len(i))
print(max(max_length))


#
# Task2
# Change a given string to a new string where the first and last chars have been exchanged.
#
def change_sring(str1):
    end = str1[-1]
    str1 = str1.replace(str1[-1], str1[0], 1)
    str1 = str1.replace(str1[0], end, 1)

    return str1


str1 = '52341'
print(change_sring(str1))


# Task3
# Sum all the items in a given list
def sum(num):
    num = str(num)
    counter = None
    for i in num:
        if i != '0':
            if counter is None:
                counter = int(num[0])
            else:
                counter += int(i)
    return counter


print(sum(str1))

#
# Task4
# Return the largest number from a list
print(max(list(str1)))
#
# Task5
# Return the smallest number from a list
print(min(list(str1)))
#
# Taks6
# Take two lists and returns True if they have at least one common member
my_list1 = ['a', 'b', 'c']
my_list2 = ['d', 'b', 'a']


def similar(my_list1, my_list2):
    for i in my_list1:
        for j in my_list2:
            if i == j:
                return True
    return False


print(similar(my_list1, my_list2))
# Task7
# Map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
my_dict = {key: value for key, value in zip(keys, values)}
print(my_dict)
# Task8
# Convert a tuple to a string.
tupl = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
my_str1 = ''
for i in tupl:
    my_str1 += i

print(my_str1)
#
# Task9
# Unpack a tuple in several variables.
x1, x2, x3, x4, x5, x6, x7, x8, x9= tupl
print(f"{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x6}\n{x7}\n{x8}\n{x9}")
