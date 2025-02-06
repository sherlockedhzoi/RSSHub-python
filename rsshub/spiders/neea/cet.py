import json
import requests
from bs4 import BeautifulSoup

domain = 'https://cet.neea.edu.cn'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def parse(post):
    return {
        'title': post.find('span', id='ReportIDname').a.text.encode('utf-8'),
        'description': post.find('span', id='ReportIDname').a.text.encode('utf-8') + post.find('span', id='ReportIDIssueTime').text.encode('utf-8'),
        'link': domain + post.find('span', id='ReportIDname').a['href'],
        'pubDate': post.find('span', id='ReportIDIssueTime').text,
        'author': '中国教育考试网'
    }

def ctx():
    url = f'{domain}/html1/category/16093/1124-1.htm'
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('ul', id='first_data').find_all('li')
    return {
        'title': 'NEEA - CET',
        'link': url,
        'description': '　全国大学英语四、六级考试（CET）是由教育部主办，教育部教育考试院（原教育部考试中心）主持和实施的大规模标准化考试，是全国性的教学考试，其目的是促进我国大学英语教学工作，对大学生的英语能力进行客观、准确的测量，为提高我国大学英语课程的教学质量提供服务。CET始于1987年，已走过了三十多年的历程，对我国大学英语教学的发展和改革产生了积极的影响。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }