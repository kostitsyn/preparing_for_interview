import gevent
import gevent.monkey
from urllib.request import urlopen

gevent.monkey.patch_all()


def get_data(url):
    print(f'Cetting {url}')
    data = urlopen(url).read()
    data_len = len(data)
    print(f'received: {data_len}')
    # print(f'received: {data}')

urls = ['http://yandex.ru', 'http://google.com', 'http://ria.ru']
jobs = [gevent.spawn(get_data, u) for u in urls]
gevent.wait()
