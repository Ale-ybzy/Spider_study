# -*- codeing = utf-8 -*-
# @Time : 2021/1/16 19:49
# @Author : Ale
# @File : spider.py
# @Sofeware : PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url,获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作

# 变量定义
# 影片详情的规则
findLink = re.compile(r'<a class="nbg" href="(.*?)"')  # 创建正则表达式对象，表示字符串的模式规则
# 影片图片的链接
findImgSrc = re.compile(r'<img.* src="(.*?)" width="75"/>')  # re.s表示忽略换行的情况
# 影片的片名
findTitle = re.compile(r'<a class="".*>(.*)/ <span style=.*>', re.S)
# 影片评分
findRating = re.compile(r'<span class="rating_nums">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span class="pl">\((\d*)人评价\)</span>')
# 补充(.*)为贪婪匹配它匹配到不能匹配为止，(.*?)为懒惰匹配一次匹配之后就不在往下进行


# 主函数流程
def main():
    baseurl = "https://movie.douban.com/chart"
    # 1. 爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影top10.xls"
    dbpath = "movie.db"
    # 2. 逐一解析数据
    # 3. 保存数据
    saveData(datalist, savepath)
    # saveData2DB(datalist,dbpath)

    # askURL("https://movie.douban.com/tv/#!type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=")

# 爬取网页解析数据
def getData(baseurl):
    datalist = []
    # for i in range(0,100,20):    #调用获取页面信息的函数，5次
    #     url = baseurl + str(i)
    #       html = askURL(url)    #保存获取到的网页源码
    html = askURL(baseurl)

    # 2. 逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('tr', class_="item"):  # 查找符合要求的字符串形成列表,class是类别所以要加下划线，表示属性值
        # print(item)     #测试查看电影item全部信息
        data = []  # 保存一部电影的全部信息
        item = str(item)
        # print(item)
        # break

        # 获取影片详情的链接
        link = re.findall(findLink, item)[0]  # re库通过正则表达式查找指定的字符串
        # print(link)
        data.append(link)   # 添加链接

        imgSrc = re.findall(findImgSrc, item)[0]
        # print(imgSrc)
        data.append(imgSrc)   # 添加图片

        titles = re.findall(findTitle, item)[0]
        ctitle = titles.replace("\n", "")
        # ctitle = re.sub(" ","", ctitle)  #re.sub替换函数，将ctitle字符串中的空格去除
        ctitle = ctitle.replace(" ", "")
        # print(ctitle)
        # if(len(titles == 2)):
        #     ctitle = titles[0]    #添加中文名
        #     data.append(ctitle)
        #     otitle = titles[1].replace("/", "")   #把外文名前面的/替换去除
        #     data.append(otitle)   #添加中文名添加中文名
        # else:
        #     data.append(titles[0])
        #     data.append(' ')  #外文名留空
        data.append(ctitle)  # 添加标题

        rating = re.findall(findRating, item)[0]
        # print(rating)
        data.append(rating)  # 添加评分

        judgeNum = re.findall(findJudge, item)[0]
        # print(judgeNum)
        data.append(judgeNum)  # 添加评价人数

        datalist.append(data)  #把处理好的一部电影信息放入datalist

    # print(datalist, len(datalist))
    return datalist

# 解析URL，得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向浏览器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    # 用户代理表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html

# 保存数据
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
    sheet = book.add_sheet('豆瓣电影top10', cell_overwrite_ok=True)  #创建工作表,cell_overweite_ok参数是否覆盖单元格原内容
    col = ("电影详情链接","图片链接","影片名称", "评分", "评价数")
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(0,10):
        print("正在保存...")
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])

    book.save(savepath)  # 保存数据表

# 保存数据到数据库
# def saveData2DB(datalist,dbpath):
#     init_db(dbpath)
#     conn = sqlite3.connect(dbpath)
#     cur = conn.cursor()
#
#     for data in datalist:
#         for index in range(len(data)):
#             if index == 3 or index == 4:
#                 continue
#             data[index] = '"'+data[index]+'"'
#         sql = f'''
#                 insert into movie10 (
#                     info_link,pic_link,cname,score,rated)
#                     values(%s)'''%",".join(data)
#
#         print(sql)
#         cur.execute(sql)
#         conn.commit()
#     cur.close()
#     conn.close()

# 初始化数据库
# def init_db(dbpath):
#     sql = '''
#         create table movie10
#         (
#             id integer primary key autoincrement,
#             info_link text,
#             pic_link text,
#             cname varchar,
#             score numeric,
#             rated numeric )
#       '''    # 创建数据表
#     conn = sqlite3.connect(dbpath)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()


if __name__ == "__main__":
    # 调用函数
    main()
    print("爬取完毕！")
