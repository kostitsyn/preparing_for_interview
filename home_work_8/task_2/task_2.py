"""
Скрипт парсинга страниц категорий goodsshop проекта с использованием BeatifulSoup.
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup as bs

URL = 'http://127.0.0.1:8000'


async def get_data(url: str) -> None:
    """
    Спарсить страницы каталогов и записать результат в файл.
    :param url: (str) Корневой адрес ресурса.
    :return:
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as main_page_response:
            main_page_text = await main_page_response.text()
            soup = bs(main_page_text, 'html.parser')
            links = soup.findAll('a', {'class': 'catalog-item'})
            for index, tag in enumerate(links):
                link_path = tag['href']
                async with session.get(f'{url}{link_path}') as item_catalog_response:
                    text_in_links = await item_catalog_response.text()
                    with open(f'file_{index+1}.html', 'w') as f:
                        f.write(text_in_links)
            print('Данные в файлы успешно записаны!')

loop = asyncio.get_event_loop()
loop.run_until_complete(get_data(URL))
