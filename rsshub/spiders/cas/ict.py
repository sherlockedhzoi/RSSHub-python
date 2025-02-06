import requests
from bs4 import BeautifulSoup

domain = 'http://www.ict.cas.cn'

def parse(post):
    return {
        'title': post.a.text.strip(),
        'description': post.a.text + post.span.text,
        'link': f'{domain}/yjsjy/zsxx/sszs{post.a['href'].strip('.')}',
        'pubDate': post.span.text.strip('[]'),
        'author': '中国科学院计算技术研究所'
    }

def ctx():
    url = f'{domain}/yjsjy/zsxx/sszs/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('div', id='content').find_all('li')
    return {
        'title': '中国科学院计算技术研究所 - 招生公告',
        'link': url,
        'description': '　中国科学院计算技术研究所（以下简称“计算所”）是全国最早培养计算机专业领域高层次人才的单位之一。建所之初，计算所通过举办训练班、派遣留学生等形式为国家培养了最早一批计算机专业人才。计算所1960年正式开始招收研究生，1978年国家建立学位制度，成为首批硕士和博士学位授予单位，并先后获批为自行增列博士生导师试点单位、国家首批博士后流动站单位等。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }