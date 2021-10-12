'''
File Created: 2021/10/12 11:37:46
Author: ZhengxuanQian (zhengxuanqian@smail.nju.edu.cn)
-----
Last Modified: 2021/10/12 11:47:38
Modified By: ZhengxuanQian (zhengxuanqian@smail.nju.edu.cn>)
'''


import html
import random
import re
import time

import requests
from utils import config

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}

pattern = re.compile(r'<span class="ctt">(.*?)</span>', re.S)

def get_weibo() -> list[str]:
    result = []
    for page in range(1, config.PAGE + 1):
        response = requests.get(config.HOMEPAGE, headers=headers, cookies=config.COOKIES, params={"page": page})
        if response.status_code != 200:
            print(f"error: {response.status_code} + {response.text}")
        else:
            temp = pattern.findall(response.text)
            temp = list(map(lambda x: re.sub(r"<br/>", "\n", x, flags=re.S).strip(), temp))
            for text in temp:
                if "全文</a>" not in text:
                    print(text)
                    result.append(text)
                else:
                    href = re.findall(r"href='(.*?)'", text, flags=re.S)[0]
                    temp_url = f"https://weibo.cn{href}"
                    response = requests.get(temp_url, headers=headers, cookies=config.COOKIES)
                    if response.status_code != 200:
                        print(f"error: {response.status_code}")
                    else:
                        text = pattern.findall(response.text)[0]
                        text = re.sub(r"<br/>", "\n", text).strip()
                        if text.startswith(":"):
                            text = text[1:]
                        print(text)
                        result.append(text)
        time.sleep(60 + random.randint(0, 60))
        result.reverse()
        result = [html.unescape(x) for x in result]
        print(len(result))
        return result

if __name__ == "__main__":
    pass
