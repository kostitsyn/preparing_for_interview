import asyncio

import requests
import aiohttp
from bs4 import BeautifulSoup as bs

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
              ' (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
URL = 'http://127.0.0.1:8000'


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            soup = bs(response, 'html.parser')
            print()



loop = asyncio.get_event_loop()
loop.run_until_complete(get_data(URL))


# session = aiohttp.ClientSession()
#
#
#
# response = session.get(URL)
# soup = bs(response.text(), 'html.parser')
# spam = soup.findAll('a', {'class': 'catalog-item'})
# for i, j in enumerate(spam):
#     a = j['href']
#     eggs = requests.get(f'{URL}{a}')
#     foo = bs(eggs.text, 'html.parser')
#     with open(f'file_{i+1}.html', 'w') as f:
#         f.write(eggs.text)
#     print()