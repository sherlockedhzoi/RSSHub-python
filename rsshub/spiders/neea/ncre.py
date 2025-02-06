import json
import requests
from bs4 import BeautifulSoup

domain = 'https://ncre.neea.edu.cn'

def parse(post):
    return {
        'title': post.find('span', id='ReportIDname').a.text,
        'description': post.find('span', id='ReportIDname').a.text + post.find('span', id='ReportIDIssueTime').text,
        'link': domain + post.find('span', id='ReportIDname').a['href'],
        'pubDate': post.find('span', id='ReportIDIssueTime').text,
        'author': '中国教育考试网'
    }

def ctx():
    url = f'{domain}/html1/category/1507/872-1.htm'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('ul', id='first_data').find_all('li')
    return {
        'title': 'NEEA - NCRE',
        'link': url,
        'description': '''全国计算机等级考试（National Computer Rank Examination，简称NCRE），是经原国家教育委员会（现教育部）批准，由教育部教育考试院（原教育部考试中心）主办，面向社会，用于考查应试人员计算机应用知识与技能的全国性计算机水平考试体系。NCRE开考之后，受到社会广泛关注和认可，为我国信息化技术人才的培养做出了重要贡献。''',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }