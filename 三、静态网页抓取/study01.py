# coding: utf-8
# 爬取豆瓣TOP250电影数据

import requests
from bs4 import BeautifulSoup  #Beautiful Soup是一个可以从HTML或XML中提取数据的Python库

def get_movies():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
          'Host':'movie.douban.com'}
    movie_list = []
    for i in range(0,1):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        r = requests.get(link , headers = header, timeout = 20)
        print("第",str(i+1),"页响应码：", r.status_code)

        with open('s_test.html','wb+') as k:
            k.write(r.text.encode('utf-8'))

        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')   #因为class是python的保留关键字，所以无法直接查找class这个关键字,可通过BeautifulSoup中的特别关键字参数class_
    #     for div in div_list:
    #         movie = div.a.span.text.strip()
    #         movie_list.append(movie)
    # return movie_list
    return div_list

movies = get_movies()
print(movies)

with open("d_test.html", "wb+") as f:   # a+追加读写；w+覆盖读写
    f.write(str(movies).encode('utf-8'))


