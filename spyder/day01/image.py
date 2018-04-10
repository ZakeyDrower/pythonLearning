import requests
import os
import win_unicode_console
win_unicode_console.enable()

url = 'http://image.nationalgeographic.com.cn/2017/0907/20170907051330421.jpg'
mp4 = 'http://www.happytreefriendscn.com/index/eye-candy.mp4'
root = 'F:\\pythonLearn\\spyder\\day01\\'
path = root + mp4.split('/')[-1]
print(path)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('image saved.')
    else:
        print('image existed!')
except:
    print('failed!')
