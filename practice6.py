class MyException(TypeError):
    def __init__(self, value, my_list):
        self.value = value
        self.my_list = my_list


    def add(self):
        try:
            self.my_list = self.my_list + [int(self.value)]
            return self.my_list
        except (ValueError, TypeError):
           return 'can only concatenate list (not "str") to list '


my_exception = MyException('10', [1, 2, 3])
m2 = MyException('STR', [1, 2, 3])
print(my_exception.add())
print(m2.add())
