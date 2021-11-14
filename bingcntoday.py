import re
import webbrowser

import requests

web = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
bing = requests.get(web)
# print(bing.text)

dicts = bing.json()
# print(dicts.keys())
# print(dicts['images'])
# for k, v in dicts['images'][0].items():
#   print(str(k) + ' : ' + str(v))
# print(dicts)

print(dicts['images'][0]['copyright'])
date = dicts['images'][0]['startdate']
# print('https://www.bing.com'+dicts['images'][0]['url'].strip('&pid=hp'))
url = 'https://www.bing.com' + dicts['images'][0]['url'].strip('&pid=hp')
paper = requests.get(url)
describe = dicts['images'][0]['urlbase'].strip('/th?id=OHR.')
# print(describe)
num = re.compile(r'\d*')
simple = num.sub('', describe)
# print(simple)
name = date + '-' + simple + '.jpg'
image = open(name, 'wb')
# webbrowser.open(url)


print('是否下载到本地？')
dl = input('[y/n]:')
if dl.lower() == 'y':
    for i in paper.iter_content(10000):
        image.write(i)
    image.close()
