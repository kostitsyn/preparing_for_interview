"""
Скрипт парсинга страниц категорий goodsshop проекта.
"""

import asyncio
import aiohttp

URLS = [
    'http://127.0.0.1:8000/catalog/c8de92c6-6390-451b-b558-b1a43ce7b9a4/',
    'http://127.0.0.1:8000/catalog/680eab69-3c40-4418-8f09-09b9e7654029/',
    'http://127.0.0.1:8000/catalog/65440c56-62c4-4add-8cc1-57677c7f2103/'
]


async def call_url(url: str) -> None:
    """
    Спарсить страницу и записать результат в файл.
    :param url: (str) Адрес страницы конкретного каталога.
    :return:
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            with open(f'file_{URLS.index(url)+1}.html', 'w') as f:
                f.write(data)
            print('Данные в файлы успешно записаны!')

futures = [call_url(url) for url in URLS]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
