import json
import requests
from bs4 import BeautifulSoup

domain = 'https://www.ccf.org.cn'

def parse(post):
    return {
        'title': post.find('div', class_='info').find('a', class_='name').text.decode('utf-8'),
        'description': post.find('div', class_='info').find('div', class_='summary').a.text.decode('utf-8'),
        'link': f'{domain}{post.find('div', class_='info').find('a', class_='name')['href']}',
        'pubDate': post.find('div', class_='info').find('div', class_='time').text,
        'author': 'CCF组委会'
    }

def ctx():
    url = f'{domain}/ccsp/tzgg'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('div', class_='listbox').find_all('div', class_='item')     
    return {
        'title': 'CCF - CCSP',
        'link': url,
        'description': 'CCSP竞赛(Collegiate Computer Systems & Programming Contest，大学生计算机系统与程序设计竞赛)，由中国计算机学会(CCF)于2016年发起的一个面向大学生的竞赛，每年举办一次，考察的是算法、编程以及计算机系统设计能力，旨在进一步提高计算机教育质量，使学生通过竞赛进一步学习和掌握计算机系统知识，同时对高校计算机教育产生引领作用。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }