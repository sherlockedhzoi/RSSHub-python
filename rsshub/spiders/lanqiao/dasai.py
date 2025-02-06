import json
import requests
from bs4 import BeautifulSoup

domain = 'https://dasai.lanqiao.cn'

def parse(post):
    return {
        'title': post['title'],
        'description': post['synopsis'],
        'link': f'{domain}/notices/{post["nnid"]}',
        'pubDate': post['publishTime'],
        'author': post['author']
    }

def ctx():
    url = 'https://www.guoxinlanqiao.com/api/news/find?status=1&project=dasai&progid=20&pageno=1&pagesize=10'
    posts = requests.get(url).json()       
    return {
        'title': '蓝桥云课 - 蓝桥杯 - 大赛通知',
        'link': f'{domain}/notices/?progid=20',
        'description': '蓝桥杯全国软件和信息技术专业人才大赛由工业和信息化部人才交流中心主办，包括北大、清华等在内的全国31个省市自治区1200多所院校参加，每年参赛人数超过30000人。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }