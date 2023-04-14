#!/usr/bin/python
# coding :utf-8

import requests # 引入包

link = "http://www.santostang.com/" # 定义link为目标网址

# 定义请求头的浏览器代理，伪装成浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

r = requests.get(link, headers = headers)  # 请求网页

print(r.text)  # 获取网页代码内容

