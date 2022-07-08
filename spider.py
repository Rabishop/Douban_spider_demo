# -*- codeing = utf-8 -*-
# @Time :  4:16
# @Author : JIN XIUSHU
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import sqlite3


def main():
    #1.爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250.xls"
    # askURL("https://movie.douban.com/top250?start=0")


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }#用户代理，模拟头部信息

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用指定不同网页10次
        url = baseurl + str(i*25)
        html = askURL(url) #保存网页源码

        #逐一解析网页

    return datalist


#3.保存数据
def saveData(savepath):
    print("save...")



if __name__ == "__main__":
    main()
