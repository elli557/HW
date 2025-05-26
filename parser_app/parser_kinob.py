import requests
from bs4 import BeautifulSoup as BS

URL = 'https://kinob.net/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS(html, features='html.parser')
    items = bs.find_all("li", class_='item')
    kinob_list = []

    for item in items:
        title = item.find("div", class_='title').get_text(strip=True)
        kinob_list.append({
            'title': title,
        })
    return kinob_list

def parsing_kinob():
    response = get_html(URL)
    print('Main page status:', response.status_code)
    if response.status_code == 200:
        kinob_list_2 = []
        for page in range(1, 2):
            response = get_html('https://kinob.net/serials', params={'page':page})
            kinob_list_2.extend(get_data(response.text))
        return kinob_list_2
    else:
        raise Exception('error in parse')

if __name__ == '__main__':
    print(parsing_kinob())