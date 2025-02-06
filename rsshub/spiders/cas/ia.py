import requests
from bs4 import BeautifulSoup

domain = 'http://www.ia.cas.cn'

def parse(post):
    return {
        'title': post.a.text.encode('latin1').decode('utf-8'),
        'description': (post.a.text + post.span.text).encode('latin1').decode('utf-8'),
        'link': domain + post.a['href'],
        'pubDate': post.span.text,
        'author': '中国科学院自动化研究所'
    }

def ctx():
    url = f'{domain}/yjsjy/zs/sszs/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('ul', id='content').find_all('li')
    return {
        'title': '中国科学院自动化研究所 - 招生公告',
        'link': url,
        'description': '中国科学院自动化研究所（以下简称自动化所）成立于1956年，以智能科学与技术为主要定位，是中国科学院率先布局成立的“人工智能创新研究院”的总体牵头单位，是我国最早开展智能科学与技术基础理论、关键技术和创新性应用研究的科研机构，也是国内首个“人工智能学院”牵头承办单位。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }