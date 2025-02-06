import requests
from datetime import datetime, timezone

domain = 'https://ccpc.io'

def parse(post):
    timestamp_ms = post['publishtime']
    timestamp_s = timestamp_ms / 1000
    utc_time = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)
    current_time = utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    return {
        'title': post['title'],
        'description': f'{post["views"]} views, {post["create_date"]}, {post["keywords"]}',
        'link': f'{domain}/post/{post["id"]}.html',
        'pubDate': current_time,
        'author': 'CCPC组委会'
    }

def ctx():
    url = f'{domain}/api/archive?apikey=84dfa45fd954ca8421904123b676c5e2&channel=4&page=1&pageSize=%7B%22pageSize%22:200%7D&index=-1'
    posts = requests.get(url).json()['data']
    return {
        'title': 'CCPC - 赛事公告',
        'link': f'{domain}/event',
        'description': '中国大学生程序设计竞赛(China Collegiate Programming Contest，简称CCPC）是由中国大学生程序设计竞赛组委会组织举办的年度性赛事，旨在激发高校学生学习计算机领域专业知识与技能的兴趣，鼓励学生灵活运用计算机知识和技能解决实际问题，有效提升算法设计、逻辑推理、数学建模、编程实现和计算机系统能力，培养团队合作意识、挑战精神和创新能力，培育和选拔出一大批素质优良、结构合理的高素质信息技术人才队伍，服务“两个强国”建设。',
        'author': 'Sherlocked HZOI',
        'items': list(map(parse, posts))
    }