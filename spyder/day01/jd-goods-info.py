import win_unicode_console
import requests

win_unicode_console.enable()

r = requests.get('https://item.jd.com/1892028.html')
print(r.status_code)
# r.encoding = 'GB18030'
# print(r.apparent_encoding)
print(r.text)