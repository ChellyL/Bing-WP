import re
import sys
import requests

bingapi = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc='
countrycode = {'美国': 'us', '中国': 'cn', '日本': 'jp', '印度': 'in', '法国': 'fr', '德国': 'de', '加拿大': 'ca', '英国': 'gb',
               '全球': 'ww'}
print('需要查看哪天的Bing壁纸?')
print('请输入距离今天的日期，默认(回车)查询今日，输入 -1 可查询明日壁纸')
day = input('最多可查到一周前的壁纸：')
if day == '' or day == '0':
    pass
else:
    bingapi = 'https://www.bing.com/HPImageArchive.aspx?format=js&' + 'idx=' + day + '&n=1&cc='
# print(bingapi)

example = 'https://www.bing.com/HPImageArchive.aspx?format=js&' + 'idx=' + day + '&n=1'
getdate = requests.get(example)
image = getdate.json()
# print(image)
info = image['images']
# print(info)
# date = info[0]['startdate']
mo = re.compile(r'(\d{4})(\d{2})(\d{2})')
redate = mo.search(info[0]['startdate'])
date = redate.group(1) + '-' + redate.group(2) + "-" + redate.group(3)
for country, code in countrycode.items():

    print('\n' + country + ' ' + date + ' 的' + 'Bing壁纸：')
    wallpaper = bingapi + code
    # print(wallpaper)
    res = requests.get(wallpaper)
    if res.status_code != 200:
        print('访问出错，请稍后重试')

    image = res.json()
    # print(image)
    info = image['images']
    # print(info)
    title = info[0]['title']
    describe = info[0]['copyright']
    url = 'https://www.bing.com' + info[0]['url'].strip('&pid=hp')
    if len(title) > 4:
        print(title)
    print(describe)
    print(url)

print('\n是否需要下载某国Bing壁纸？[输入想要下载的壁纸的国家代码/回车不下载]')
ans = input('国家代码/回车：').lower()
if len(ans) == 0:
    pass
else:
    print('下载ing……请稍候……')
    wallpaper = bingapi + ans
    res = requests.get(wallpaper)
    if res.status_code != 200:
        print('访问出错，请稍后重试')

    image = res.json()
    # print(image)
    info = image['images']
    # print(info)
    url = 'https://www.bing.com' + info[0]['url'].strip('&pid=hp')
    pic = requests.get(url)
    name = date + '-' + ans.upper()
    picfile = open(name + '.jpg', 'wb')
    for i in pic.iter_content(10000):
        picfile.write(i)
    picfile.close()

exit = input('请按回车退出程序：')
if exit == '':
    sys.exit()
