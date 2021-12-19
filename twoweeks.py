import requests

countrycode = {'美国': 'us', '中国': 'cn', '日本': 'jp', '印度': 'in', '法国': 'fr', '德国': 'de', '加拿大': 'ca', '英国': 'gb',
               '全球': 'ww'}


def week(cc='cn'):
    w_list = []
    w = 0
    for t in range(2):
        url = 'https://www.bing.com/HPImageArchive.aspx?format=js&n=8&idx=' + str(w) + '&cc=' + cc
        res = requests.get(url).json()
        list = []
        for i in range(7):
            date = res['images'][i]['enddate']
            title = res['images'][i]['title']
            describe = res['images'][i]['copyright']
            url = 'https://www.bing.com' + res['images'][i]['url'].strip('&pid=hp')
            wp = date + ' ' + title + '\n' + describe + '\n' + url
            list.append(wp)
        w_list += list
        w += 8

    two_week = '\n\n'.join(w_list)
    return two_week


print(week())
