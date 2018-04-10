import requests
import win_unicode_console
win_unicode_console.enable()

url = 'http://www.ip138.com/ips138.asp?'
kv = {'ip':'192.168.137.1'}
try:
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('error occurred')