import requests
import win_unicode_console
win_unicode_console.enable()

url = 'https://www.amazon.cn/dp/B00QJDOLIO?_encoding=UTF8&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=8caaabb8-184d-4c98-9db9-834ca4b98521&pf_rd_r=PGJR3QKPGKVGF0YTEZ1W&pf_rd_s=Tcg-slide-1&pf_rd_t=36701&ref_=p-Tcg-slide-1--2efc1934-96f8-455f-bc30-b0debca468f9'
kv = {'user-agent':'Mozilla/5.0'}
r = requests.get(url, headers=kv)
print(r.text[1000:2000])