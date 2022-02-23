import re
import sys
import requests
import os

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

countrycode = {'美国': 'us', '中国': 'cn', '日本': 'jp', '印度': 'in', '法国': 'fr', '德国': 'de', '加拿大': 'ca', '英国': 'gb',
               '全球': 'ww'}
print('需要查看哪天的Bing壁纸?(最多回溯15天)')
day = input('请输入距离今天的日期，默认(回车)查询今日:')
if day == '' or day == '0':
    day = 0
    bingapi = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc='
elif 0 < int(day) < 8:
    day = int(day)
    bingapi = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&cc='
    
else:
    day = int(day) - 8
    bingapi = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=8&n=8&cc='

print(day)

getdate = requests.get(bingapi)
image = getdate.json()
info = image['images']

mo = re.compile(r'(\d{4})(\d{2})(\d{2})')
redate = mo.search(info[day]['startdate'])
date = redate.group(1) + '-' + redate.group(2) + "-" + redate.group(3)

for country, code in countrycode.items():

    print('\n' + country + ' ' + date + ' 的' + 'Bing壁纸：')
    wallpaper = bingapi + code
    res = requests.get(wallpaper)
    if res.status_code != 200:
        print('访问出错，请稍后重试')

    image = res.json()
    info = image['images']
    title = info[day]['title']
    describe = info[day]['copyright']
    url = 'https://www.bing.com' + info[day]['url'].strip('&rf=LaDigue_1920x1080.jpg&pid=hp') + '_1920x1080.jpg'

    print(title)
    print(describe)
    print(url)

print('\n是否需要下载所选Bing壁纸？[输入想要下载的壁纸的国家代码/回车不下载]')
ans = input('国家代码/回车：').lower()
if len(ans) == 0 or ans == 'n':
    pass
else:
    print('下载ing……请稍候……')
    wallpaper = bingapi + ans
    res = requests.get(wallpaper)
    if res.status_code != 200:
        print('访问出错，请稍后重试')

    image = res.json()

    info = image['images']
    url = 'https://www.bing.com' + info[0]['url'].strip('&rf=LaDigue_1920x1080.jpg&pid=hp')
    pic = requests.get(url)

    describe = info[0]['urlbase'].strip('/th?id=OHR.')
    num = re.compile(r'\d*')
    simple = num.sub('', describe)
    date = info[0]['startdate']
    name = date + '-' + simple
    picfile = open(name + '.jpg', 'wb')
    for i in pic.iter_content(10000):
        picfile.write(i)
    picfile.close()

exit = input('请按回车退出程序：')
if exit == '':
    sys.exit()
