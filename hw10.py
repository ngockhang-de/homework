from aiohttp import web
import requests


async def weather(request):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
    country = 'Ukraine'

    querystring = {"country": country}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "b8af9d6883mshd7e92b07860b620p1cf3aejsnaac060abdb6b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    text = f'{country}\nrecovered-{data["data"]["recovered"]}\ndeaths-{data["data"]["deaths"]}\nconfirmed-{data["data"]["confirmed"]}'

    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/weather', weather)])

if __name__ == '__main__':
    web.run_app(app)
