import re
import webbrowser

import requests

country = 'cn'
web = 'https://www.bing.com/HPImageArchive.aspx?format=js&n=1&idx=0&cc=' + country
# web = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
bing = requests.get(web)
dicts = bing.json()

print(dicts['images'][0]['startdate'] + '\n' + dicts['images'][0]['title'] + '\n' + dicts['images'][0]['copyright'])
date = dicts['images'][0]['startdate']
# url = 'https://www.bing.com' + dicts['images'][0]['url'].strip('&pid=hp')
urlbase = 'https://www.bing.com' + dicts['images'][0]['urlbase']
url = urlbase + '_1920x1080.jpg'

paper = requests.get(url)
describe = dicts['images'][0]['urlbase'].strip('/th?id=OHR.')

num = re.compile(r'\d*')
simple = num.sub('', describe)
name = date + '-' + simple + '.jpg'
image = open(name, 'wb')
# webbrowser.open(url)


print('是否下载到本地？')
dl = input('[y/n]:')
if dl.lower() == 'y':
    for i in paper.iter_content(10000):
        image.write(i)
    image.close()
