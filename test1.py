import requests
import bs4

url = 'https://www.ipip.net/ip/119.86.43.214.html'


    #print("正在请求网络-------")
    #ip=ip_input.get()
    #伪装浏览器，身份的标识
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }

    # 请求网络，获取html数据
r=requests.get(url,headers=header).text
print(r)