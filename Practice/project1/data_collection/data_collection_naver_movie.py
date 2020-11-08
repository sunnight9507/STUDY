import requests
import re
import string
from bs4 import BeautifulSoup

def download(url, params={}, method='GET', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}):
    '''
    url crawling
    :param url: 요청받을 url
    :param params: key
    :param headers:
    :return: response
    '''
    resp = requests.request(method, url,
                            params=params if method == 'GET' else {},
                            data=params if method == 'POST' else {},
                            headers=headers)

    return resp

def naver_movie_user_rating_scraping():
    print('start')

    url = 'https://movie.naver.com/movie/point/af/list.nhn?&page='
    page = 1

    url += str(page)

    resp = download(url,)
    dom = BeautifulSoup(resp.text, 'lxml')
    text = dom.find('tbody')
    text = text.find_all('tr')

    for _ in range(1):
        num = text[_].select_one('td.ac.num').text
        title = text[_].select_one('a.movie').text
        rating = text[_].select_one('em').text
        _text = text[_].select_one('td > br').next_sibling.strip()
        user_id = text[_].select_one('a.author').text
        date = text[_].select_one('td.num > br').next_sibling

        print(num, title, rating, _text, user_id, date)

    print('end')


if __name__ == '__main__':
    naver_movie_user_rating_scraping()
