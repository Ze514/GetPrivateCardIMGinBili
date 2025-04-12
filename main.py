import requests
import os
import getcookie
import re
import getname
usr_id = str(input(":"))
strlikecookie = r"YOUR_COOKIE"
cj = getcookie.str_to_cookiejar(strlikecookie,".bilibili.com")
headers = {
    'User-Agent':"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Referer':'https://message.bilibili.com/',
    'Origin':'https://message.bilibili.com'
}
js = {
    'talker_id':usr_id,
    'session_type':"1",
    'size':"200",
    'mobi_app':'web',
    'build':"0"
}
html = requests.get("https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs",headers=headers,cookies=cj,params=js) #353840826
tr_html = html.json()
print("Response Status:", html.status_code)
print("Response Cookies:", html.cookies)
print("Response JSON:", html.json())
container = []
for msg in tr_html['data']['messages']:
    if msg['msg_type'] != 1:
        container.append(msg)
def download(listobj):
    #'{"pic_url":"http://i0.hdslb.com/bfs/location/2fc71d6391eb9aa81d8a5f968e32e8cbb2418305.png",
    # "jump_url":"https://game.bilibili.com/pcr/kyarlyabaival",
    # "title":"凯露被魔物抓走了！"}'
    for i in listobj:
        sender = getname.getname_for_folder(i['sender_uid'])
        os.makedirs(sender,exist_ok=True)
        if len(re.findall(r"title",i['content'])) == 0:
            name = str(i['timestamp'])
        else:
            name = re.findall(r"title\":\"(.*?)\"",i['content'])[0]
        try:

            url = re.findall(r"http(.*?)\"",i['content'])[0]
            url = "http" + url
            data = requests.get(url,timeout=5)
            data = data.content
            with open(f"{sender}\\{name}.webp","wb") as f:
                f.write(data)
        except IndexError:
            pass
    return ""
download(container)