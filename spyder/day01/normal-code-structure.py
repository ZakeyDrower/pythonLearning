import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() # 如果状态异常产生异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Occur exception'

if __name__ == '__main__':
    url = 'https://user.qzone.qq.com/277218025/infocenter'
    print(getHTMLText(url))