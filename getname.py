import requests
def getname_for_folder(mid):
    staticlink = r"https://api.bilibili.com/x/web-interface/card"
    headers = {
    'User-Agent':"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Referer':f'https://space.bilibili.com/{mid}',
    'Origin':'https://space.bilibili.com'        
    }
    params = {
        'mid':mid
    }
    html = requests.get(staticlink,params=params,headers=headers)
    resp = html.json()
    return resp['data']['card']['name']