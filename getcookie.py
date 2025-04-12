import requests
from http.cookiejar import CookieJar
from urllib.parse import unquote  # 新增导入
# 修改 getcookie.py，使用更严格的 Cookie 属性
def str_to_cookiejar(cookie_str, domain='.bilibili.com'):
    jar = requests.cookies.RequestsCookieJar()
    for cookie in cookie_str.split(';'):
        cookie = cookie.strip()
        if '=' not in cookie:
            continue
        name, value = cookie.split('=', 1)
        name = name.strip()
        value = unquote(value.strip())  # 解码
        # 设置 Secure 和 HttpOnly
        jar.set(
            name, value,
            domain=domain,
            path='/',
            secure=name in ['SESSDATA', 'bili_jct'],  # 关键 Cookie 启用 Secure
            rest={'HttpOnly': True}
        )
    return jar

# 使用示例

