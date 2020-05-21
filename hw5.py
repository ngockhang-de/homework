from collections import Counter


def save_to_file():
    minsymbol = 3
    maxsymbol = 5
    file = open("text.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("text.txt", "w")
    temp = [0, 0]
    for line in lines:
        line_split = line.split()
        index = 0
        while index < len(line_split):
            if minsymbol <= len(line_split[index]) <= maxsymbol:
                temp[1] = temp[1] + 1
                if temp[1] != 2:
                    temp[0] = index
                if temp[1] == 2:
                    line_split.remove(line_split[index])
                    line_split.remove(line_split[temp[0]])
                    temp[1] = 0
                    index -= 1
                else:
                    index += 1
            else:
                index += 1
        temp[1] = 0
        file.write(f"{' '.join(line_split)}\n")

    file.close()


# save_to_file()

def phone_file():
    file = open("phone.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("phone_K_C.txt", "w")
    for line in lines:
        if line[0] == 'К' or line[0] == 'С':
            file.write(line)
    file.close()


# phone_file()
# Получить файл g, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
def align_right():
    file = open("g.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("g.txt", "w")
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
    for line in lines:
        while len(line) != max_length:
            line = " " + line
        file.write(line)

    file.close()


align_right()


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num
# Дан текстовый файл со статистикой посещения сайта за неделю.
# Каждая строка содержит ip адрес, время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
# Создайте новый текстовый файл, который бы содержал список ip без повторений из первого файла.
# Для каждого ip укажите количество посещений, наиболее популярный день недели.
# Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
def ip():
    ip_list = {}
    file = open("ip.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("ip1.txt", "w")
    for line in lines:
        line = line.split()
        if line[0] not in ip_list:
            ip_list.update({line[0]: [1, {"monday": 0, "tuesday": 0, "wednesday": 0, "thursday": 0, "friday": 0,
                                          "saturday": 0, "sunday": 0},
                                      [line[1][:2]]]})
        else:
            ip_list[line[0]][0] += 1
            ip_list[line[0]][2].append(line[1][:2])
        for ipd in ip_list[line[0]][1].keys():
            if line[2] == ipd:
                ip_list[line[0]][1][ipd] += 1

    for items in ip_list:
        k = Counter(ip_list[items][1])
        high = k.most_common(1)
        file.write(f"{items}, visits-{ip_list[items][0]}, Day-{high[0][0]}\n")


    file.close()
    file = open("ip1.txt", "a")
    most_list = []
    for line in lines:
        line = line.split()
        most = most_frequent(ip_list[line[0]][2])
        most_list.append(most)
    most_all = most_frequent(most_list)
    file.write(f"Most pop time {most_all}")
    file.close()


ip()
