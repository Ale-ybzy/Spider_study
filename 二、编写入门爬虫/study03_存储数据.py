#!/usr/bin/python
# coding :utf-8

import requests # 引入包
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup

link = "http://www.santostang.com/" # 定义link为目标网址
# 定义请求头的浏览器代理，伪装成浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

r = requests.get(link, headers = headers)  # 请求网页
soup = BeautifulSoup(r.text, "html.parser") # 使用BeautifulSoup解析
title = soup.find("h1", class_ = "post-title").a.text.strip()
print(title)

#打开一个空白的txt, 然后使用f.write写入刚刚的字符串title
with open('title_test.txt', "a+") as f:
    f.write(title)

