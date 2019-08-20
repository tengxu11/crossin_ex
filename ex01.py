import re
import requests
from lxml import etree

url = 'https://www.qiushibaike.com/hot'
for x in range(1, 4):
    six = lambda s: '男' if s == 'manIcon' else '女'

    html = requests.get(url)
    data = html.text

    tree = etree.HTML(data)
    author = tree.xpath('//div [@class="author clearfix"]//h2/text()')
    authors = [str(i).strip('\n') for i in author]
    text = tree.xpath('//div [@class="content"]/span/text()')
    grent = '<div class="articleGender (.*)">'
    grent = re.findall(grent, data)
    grents = list(map(six, grent))
    age = '<div class="articleGender .*">(\d+)</div>'
    ages = re.findall(age, data)
    haoxiao = tree.xpath('//span/i[@class="number"]/text()')
    pinglun = tree.xpath('//span/a/i [@class="number"]/text()')

    results = ''
    for i in range(len(author)):
        results += '作者:{} 性别:{} 年龄{}'.format(authors[i], grents[i], ages[i])
        results += '\n'
        results += text[i]
        results += '好笑:{}  评论:{}\n'.format(haoxiao[i], pinglun[i])
        results += '*' * 10 + '\n\n'

    url = 'https://www.qiushibaike.com/hot/page/%d/' % x

with open('ex01.txt', 'w') as f:
    f.write(results)