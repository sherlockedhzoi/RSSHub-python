import json
import requests
from bs4 import BeautifulSoup

domain = 'https://gplt.patest.cn'

def parse(post):
    return {
        'title': post['title'],
        'description': f'#{post["contest"]["name"]}',
        'link': post['href'],
        'pubDate': post['publishedAt'],
        'author': post['contest']['name']
    }

def ctx():
    url = 'https://gplt.pintia.cn/api/cached/notifications'
    posts = requests.get(url).json()['data']['notifications']
    return {
        'title': '蓝桥云课 - 蓝桥杯 - 大赛通知',
        'link': f'{domain}/notification',
        'description': '蓝桥杯全国软件和信息技术专业人才大赛由工业和信息化部人才交流中心主办，包括北大、清华等在内的全国31个省市自治区1200多所院校参加，每年参赛人数超过30000人。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }