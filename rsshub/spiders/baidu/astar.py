import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz

timezone = pytz.timezone("Asia/Shanghai")

domain = 'https://astar.baidu.com'

def parse(post):
    timestamp_ms = post['updateTime']
    timestamp_s = timestamp_ms / 1000
    utc_time = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)
    current_time = utc_time.astimezone(timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
    return {
        'title': post['title'],
        'description': post['simpleContent'],
        'link': f'https://astar.baidu.com/#/news-info?tab=3&id={post["encryptId"]}',
        'pubDate': current_time,
        'author': '百度之星主办方'
    }

def ctx():
    url = f'{domain}/web/getArticlesByClassId.do?classId=14&start=0&limit=10'
    posts = requests.get(url).json()['data']['datas']
    return {
        'title': '百度 - 百度之星程序设计竞赛',
        'link': f'{domain}/notification',
        'description': '百度之星程序设计大赛（亦称百度之星·程序设计大赛）由百度在线网络技术（北京）有限公司（简称百度公司）举办，是一项旨在展示学生创新能力和编写程序、分析、解决问题能力的年度竞赛，从2005年至今已成功举办了20届，累计参赛选手三十余万名，覆盖数千所院校，成为中国最具知名度、最有影响力的程序设计大赛之一，大量优秀人才通过大赛脱颖而出，被誉为国内程序员的“黄埔军校”和“造星工厂”。大赛已入选中国高等教育学会“全国普通高校大学生竞赛排行榜”竞赛项目榜单。百度之星是百度500万大模型人才培养计划的组成部分，长期致力于搭建一个以赛促教、以赛促学的程序设计和人工智能人才培养平台，推动中国互联网和AI领域人才成长。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }