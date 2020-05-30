class Ip:
    all_ip = ['10.11.12.13', '1.2.3.4']

    def all_ip_adress(self):
        return self.all_ip

    def full_list(self):
        list_ip = [i for i in self.all_ip]
        for i in range(len(list_ip)):
            split_ip = list_ip[i].split('.')
            split_ip.sort(reverse=True)
            split_ip = '.'.join(split_ip)
            list_ip[i] = split_ip
        return list_ip

    def without_first(self):
        list_ip = [i for i in self.all_ip]
        for i in range(len(list_ip)):
            split_ip = list_ip[i].split('.')
            split_ip.pop(0)
            split_ip = '.'.join(split_ip)
            list_ip[i] = split_ip
        return list_ip

    def last_ip(self):
        list_ip = [i for i in self.all_ip]
        for i in range(len(list_ip)):
            split_ip = list_ip[i].split('.')
            list_ip[i] = split_ip[3]
        return list_ip


ip = Ip()
print(ip.full_list())
print(ip.all_ip)
print(ip.without_first())
print(ip.all_ip)
print(ip.last_ip())

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
#
import json
import os


class Jsonhelper:
    def __init__(self, path_file):
        self.file = path_file

    def write_to_file(self, content):
        with open(self.file, 'w') as file:
            json.dump(content, file)

    def read_from_file(self):
        with open(self.file, 'r') as file:
            data = json.load(file)
        return data

    def combine(self, another_file, new_file):
        with open(self.file, 'r') as first_file:
            json1 = json.load(first_file)
        with open(another_file, 'r') as second_file:
            json2 = json.load(second_file)
        merged_file = json1.copy()
        merged_file.update(json2)
        with open(new_file, 'w') as final_file:
            json.dump(merged_file, final_file)

    def absolute_path(self):
        return os.path.abspath(self.file)

    def relative_path(self):
        return os.path.relpath(self.file)


# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.
class Physunit:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.__unit_name = unit_name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__login = login
        self.__password = password

    @property
    def unit_name(self):
        return self.__unit_name

    @unit_name.setter
    def unit_name(self, value):
        self.__unit_name = value

    @property
    def mac_address(self):
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, value):
        self.__mac_address = value

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value):
        self.__ip_address = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
