import requests

bigger_price = [{"name": "bread", "price": 100}, {"name": "wine", "price": 138}, {"name": "meat", "price": 15},
                {"name": "water", "price": 1}]


# == [     {"name": "wine", "price": 138},     {"name": "bread", "price": 100} ]


def bigger(limit, data):
    price = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[j]["price"] > data[i]["price"]:
                data[i], data[j] = data[j], data[i]
    ans = []
    for i in range(limit):
        ans.append(data[i])
    return ans


# print(bigger(2, bigger_price))


def sort_func(amount, bigger_price):
    return sorted(bigger_price, key=lambda price: price['price'], reverse=True)[:amount]


# print(sort_func(2, bigger_price))
info = requests.get('https://lego-super-heroes.herokuapp.com/')
content = info.json()


def name_all(data, url):
    info = requests.get(url)
    data = info.json()
    name = []
    for i, j in enumerate(data):
        name.append(data[i]['name'])
    return name


# print(name_all(content, 'https://lego-super-heroes.herokuapp.com/'))


def weapon(data, url):
    info = requests.get(url)
    data = info.json()
    nw = [{data[i]['name']: data[i]['weapon']} for i, j in enumerate(data) if data[i]['weapon'] != '']
    return nw


print(weapon(content, 'https://lego-super-heroes.herokuapp.com/'))
