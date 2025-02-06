import requests
from bs4 import BeautifulSoup
from datetime import datetime

domain = 'http://iiis.tsinghua.edu.cn'

def parse(post):
    return {
        'title': post.a.text,
        'description': '',
        'link': post.a['href'] if post.a['href'][:4] == 'http' else domain + post.a['href'],
        'pubDate': datetime.now(),
        'author': '清华大学交叉信息研究院'
    }

def ctx():
    url = f'{domain}/graduate/#jy3'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('div', class_='item')
    return {
        'title': '清华大学交叉信息研究院 - 招生公告',
        'link': url,
        'description': '清华大学交叉信息研究院研究生教育包括计算机科学与技术和物理学两个学科方向，以培养富有杰出信息科学才能、优异综合素质和敏锐创新精神的精英人才为宗旨，借鉴国际先进的培养模式和方案，遵循因材施教、重点培养的原则，设置多样化培养模式和个性化培养方案，为培养优秀研究生、充分发挥学生个性、发掘学生潜能提供优越的平台。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }