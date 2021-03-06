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
    # 1.爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    #savepath = ".\\豆瓣电影Top250.xls"
    dbpath = "movie.db"

    # 3.保存数据
    #saveData(datalist, savepath)
    savaData2DB(datalist, dbpath)

# re库用来通过正则表达式获取指定的字符串

# 影片的链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片的图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符含在字符中
# 获得片名
findTitle = re.compile(r'<span class="title">(.*?)</span>', re.S)  # re.S 让换行符含在字符中
# 获得评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)  # re.S 让换行符含在字符中
# 评分人数
findJudge = re.compile(r'<span>(\d*)人评价</span>', re.S)  # re.S 让换行符含在字符中
# 影片概况
findInq = re.compile(r'<span class="inq">(.*?)</span>', re.S)  # re.S 让换行符含在字符中
# 相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # re.S 让换行符含在字符中


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }  # 用户代理，模拟头部信息

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用指定不同网页10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存网页源码

        # 2.逐一解析网页
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item) 查看电影item
            data = []  # 保存一部电影的所有信息
            item = str(item)

            # 影片详情
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")  # 外文名字留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = re.findall(findInq, item)[0]
                inq = inq.replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            data.append(bd.strip())  # 去掉前后空格

            datalist.append(data)
        #     print(data)
        # print(datalist)
    return datalist


# 3.保存数据
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="uft-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建工作表

    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(250):
        print("第%d条" % (i+1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])

    book.save(savepath)

# 4.保存到数据库
def savaData2DB(datalist, dbpath):
    init_db(dbpath)

    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'

        sql = '''
            insert into movie (
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values (%s)
        ''' % ",".join(data)

        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


# 5.创建数据库
def init_db(dbpath):
    sql = '''
        create table if not exists movie
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''  # 创建数据库
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



if __name__ == "__main__":
    main()
    #init_db("movie_test.db")
    print("爬取完毕")
