import requests
from bs4 import BeautifulSoup

URL = 'https://yandex.ua/pogoda/donetsk?lang=ru'
HEADERS = {'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/80.0.3987.106 Safari/537.36'}


# соеденение и отправка запроса
def get_html(url, params=None):
    r = requests.get(url, params=params) #отправить get запрос
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='forecast-briefly__day')
    weather = []
    dayD = ''
    day = ''
    tempD = ''
    tempN = ''
    wd = ''

    for item in items:
        dayD = item.find('div', class_='forecast-briefly__name').get_text()
        day = item.find('time', class_='time forecast-briefly__date').get_text()
        tempD = item.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day').get_text()
        tempN = item.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night').get_text()
        wd = item.find('div', class_='forecast-briefly__condition').get_text()
        weathersss = str('День недели: '+dayD+', Дата: '+day+', Температура '+tempD+', Температура '+tempN+', Погодные условия: '+wd)
        weather.append(weathersss)


    print(weather)


    return weather

# Парсинг
def parse():
    html = get_html(URL)
    if html.status_code == 200: # Получаем запрос get если он 200 то Все ОК
      weather = get_content(html.text)
      return weather
    else:
        print('Error')