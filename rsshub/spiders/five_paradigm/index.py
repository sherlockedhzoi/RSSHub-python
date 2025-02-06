import json
import requests
from bs4 import BeautifulSoup

domain = 'https://www.5paradigm.cn/'

def parse(post):
    views = post.find('div', class_='Meta').find('span', class_='ViewCount').span.text
    comments = post.find('div', class_='Meta').find('span', class_='CommentCount').span.text
    return {
        'title': post.find('div', class_='Title').a.text,
        'description': f'{views} views, {comments} comments',
        'category': post.find('div', class_='Meta').find('span', class_='Category').a.text,
        'link': post.find('div', class_='Title').a.attr['href'],
        'pubDate': post.find('div', class_='Meta').find('span', class_='LastCommentDate').time.attr['datetime'],
        'author': post.find('div', class_='Meta').find('span', class_='LastCommentBy').a.text
    }

def ctx():
    url = domain
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', class_='ItemContent')        
    return {
        'title': 'Welcome to 5paradigm (欢迎来到第五范式）',
        'link': url,
        'description': 'Founded by DeepMath Team, www.5paradigm.cn is a free open community where you can share your knowledge on AI for Science, Science for AI and also large AI models. We are also developing a Human-Machine Interactive Platform for Mathematical Research. Come to join us!',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }