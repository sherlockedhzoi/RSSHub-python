import json
import requests
from bs4 import BeautifulSoup

domain = 'https://cet.neea.edu.cn'

def parse(post):
    return {
        'title': post.find('span', id='ReportIDname').a.text,
        'description': post.find('span', id='ReportIDname').a.text + post.find('span', id='ReportIDIssueTime').text,
        'link': domain + post.find('span', id='ReportIDname').a['href'],
        'pubDate': post.find('span', id='ReportIDIssueTime').text,
        'author': '中国教育考试网'
    }

def ctx():
    url = f'{domain}/html1/category/16093/1124-1.htm'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('div', class_='listdiv').find('ul', id='first_data').find_all('li')
    return {
        'title': 'NEEA - CET',
        'link': url,
        'description': '　全国大学英语四、六级考试（CET）是由教育部主办，教育部教育考试院（原教育部考试中心）主持和实施的大规模标准化考试，是全国性的教学考试，其目的是促进我国大学英语教学工作，对大学生的英语能力进行客观、准确的测量，为提高我国大学英语课程的教学质量提供服务。CET始于1987年，已走过了三十多年的历程，对我国大学英语教学的发展和改革产生了积极的影响。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }