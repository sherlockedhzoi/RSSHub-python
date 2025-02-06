import json
import requests
from bs4 import BeautifulSoup

domain = 'https://gplt.patest.cn'

def parse(post):
    return {
        'title': post['title'],
        'description': f'#{post["contest"]["name"]}' if post["contest"] is not None else '',
        'category': post['contest']['name'] if post['contest'] is not None else 'GPLT',
        'link': post['href'],
        'pubDate': post['publishedAt'],
        'author': '主办方'
    }

def ctx():
    url = 'https://gplt.pintia.cn/api/cached/notifications'
    posts = requests.get(url).json()['data']['notifications']
    return {
        'title': '中国高校计算机大赛 - 团体程序设计天梯赛 - 赛事通知',
        'link': f'{domain}/notification',
        'description': '团体程序设计天梯赛是中国高校计算机大赛的竞赛版块之一，赛旨在提升学生计算机问题求解水平，增强学生程序设计能力，培养团队合作精神，提高大学生的综合素质，同时丰富校园学术气氛，促进校际交流，提高全国高校的程序设计教学水平。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }