import json
import requests
from bs4 import BeautifulSoup

domain = 'http://icpc.pku.edu.cn'

def parse(post):
    return {
        'title': post.a.text.split('[')[0],
        'description': post.a.text,
        'link': post.a['href'],
        'pubDate': post.a.span.text.strip('[]'),
        'author': 'ICPC 北京总部'
    }

def ctx():
    url = f'{domain}/tzgg/index.htm'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('div', class_='article').find('ul', class_='item-list').find_all('li')        
    return {
        'title': 'PKU - ICPC 北京总部',
        'link': url,
        'description': '''国际大学生程序设计竞赛（International Collegiate Programming Contest，简称ICPC）是世界上规模最大、水平最高的国际大学生程序设计竞赛之一。赛事由各大洲区域赛（Regional Contests）和全球总决赛（World Finals）两个主要阶段组成，每个赛季持续时间约9个月，来自全球6大洲、超过100个国家和地区的两千余所高校的近五万名大学生参与该项赛事。经过五十余年的发展，国际大学生程序设计竞赛已经成为全球最具影响力的大学生计算机竞赛，被誉为计算机软件领域的奥林匹克。竞赛提倡创新和团队协作，鼓励学生在构建全新的软件程序时尽情发挥创意，帮助学生检验自己在强压力下的工作能力，是世界各地计算机程序设计者大显身手的舞台，也是世界一流大学展现教育成果的最佳窗口。不论是区域赛还是总决赛，ICPC都一直受到国际各知名大学的重视，并受到全世界各著名计算机公司的高度关注。该比赛曾在美国的亚特兰大、加拿大的温哥华、瑞典的斯德哥尔摩、摩洛哥的马拉喀什等世界多地举办。

    竞赛的历史可以追溯到1970年，当时在美国德克萨斯Texas A&M University举办了首届比赛。1977年，在ACM计算机科学会议期间举办了首次总决赛，并演变成为目前的一年一届、多国参与的国际性比赛。最初几届比赛的参赛队伍主要来自美国和加拿大，后来逐渐发展成为一项世界范围内的竞赛。特别是自1997年IBM开始赞助赛事之后，赛事规模增长迅速。在1997年，总共有来自560所大学的840支队伍参加比赛。而到了2004年，这一数字迅速增加到840所大学的4109支队伍并以每年10%-20%的速度在增长。

　　中国大陆高校自1996年开始参加此项赛事的亚洲区预赛。1996年起设立中国大陆地区预选赛赛区，当年由上海大学承办。之后在大陆地区设置多个赛点，由各大学轮流主办地区性竞赛。此外，大陆地区还承办过三次全球总决赛：2005年4月，上海交通大学承办第29届国际大学生程序设计竞赛全球总决赛；2010年2月，哈尔滨工程大学承办第34届国际大学生程序设计竞赛全球总决赛；2018年4月，北京大学承办第42届国际大学生程序设计竞赛全球总决赛。
''',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }