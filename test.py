# _*_ coding: utf-8 _*_
"""
1.数据的请求 {获取网页的html数据}
2.数据的处理{解析html数据，提取所需数据，分析网站的数据结构,哪些需要，哪些不需要，需要通过解析方式过滤出来}
3.对过滤数据的存储 {保存在图形界面中}

"""
from tkinter import *
import requests
import re

def find_position():
    url = 'https://www.ipip.net/ip/113.204.68.86.html'
    #print("正在请求网络-------")
    ip=ip_input.get()
    #伪装浏览器，身份的标识
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }
    # 请求网络，获取html数据
    response=requests.get(url.format(ip),headers=header).text
    #print(response)
    #正则表达式的语法   --匹配模式
    address=re.search(r'地理位置.*?;">(.*?)</span>',response,re.S)
    operator=re.search(r'运营商.*?;">(.*?)</span>',response,re.S)
    time=re.search(r'时区.*?;">(.*?)</span>',response,re.S)
    wrap=re.search(r'地区中心经纬度.*?;">(.*?)</span>',response,re.S)
    #判断成功的条件（group是什么意思？）
    if address:
        ip_info=['地理位置:' + address.group(1),'当前的ip：' + ip]
        if operator:
            ip_info.insert(0,'运营商/拥有者:' + operator.group(1))
        if time:
            ip_info.insert(0,'时区:' + operator.group(1))
        if wrap:
            ip_info.insert(0,'地区中心经纬度:' + operator.group(1))
        #添加新元素之前，先清空一下
        display_info.delete(0,5)
        for item in ip_info:
            display_info.insert(0,item)
    else:
        #添加新元素之前，先清空一下
        display_info.delete(0,5)
        display_info.insert(0,'这是一个无效的ip地址！')



# 创建窗口
tk=Tk()
#Title
tk.title('Tony老师在上课')
# 输入框
ip_input=Entry(tk,width=40)
# 回显列表（盒子，装网上爬取的内容，在列表中展示，作用于当前tk窗口）
display_info=Listbox(tk,width=60,height=10)
#按钮
result_button=Button(tk,command=find_position(),text=' 查 询 ')

#程序入口，当前工程
if __name__== '__main__':
    ip_input.pack()
    display_info.pack()
    result_button.pack()
    # 循环
    tk.mainloop()