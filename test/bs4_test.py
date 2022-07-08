import re

from bs4 import BeautifulSoup
import urllib.request

# try:
#     response = urllib.request.urlopen("https://www.baidu.com", timeout=1)
#     file = open("./baidu.html", "w")
#     html = response.read().decode('utf-8')
#
#     print(str(html))
#
#     file.write(str(html))
#     file.close()
# except urllib.error.URLError as e:
#     print("time out")

file = open("./baidu.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")
'''
#1.Tag 标签及其内容：拿到第一个指定内容
print(bs.title)
print(type(bs.title))

#2.NavigableString 标签里面的内容(文字内容和标签属性)
print(bs.title.string)
print(type(bs.title.string)) #输出文字内容
print(bs.a.attrs) #输出标签属性值

#3.BeautifulSoup 表示整个文档
print(type(bs))
print(bs)

#4.Comment 特殊的NavigableString 输出不包括注释符
print(bs.a.string)
print(type(bs.a.string))

'''
#----------------------------------------
'''
#文档的遍历

for item in bs.head.contents:
    print(item)

#文档的搜索

#1.find_all() 字符串搜索
#1.1.字符串过滤与其完全相匹配的标签
t_list = bs.find_all("a")
print(t_list)

#1.2.正则表达式搜索
t_list = bs.find_all(re.compile("a"))
print(t_list)

#1.3.根据函数搜素，用于自定义
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)
print(t_list)

#2.kwargs 参数收索
t_list = bs.find_all(id="head")
t_list = bs.find_all(class_=True)
t_list = bs.find_all(href="//www.baidu.com/licence/")

for item in t_list:
    print(item)
#3.text参数
t_list = bs.find_all(text="百度APP扫码登录") #查询文本内容
t_list = bs.find_all(text=re.compile("百度")) #查询正则表表达式文本内容

for item in t_list:
    print(item)

#4.limit 参数
t_list = bs.find_all(text=re.compile("百度"), limit=3) #设置查找数量

for item in t_list:
    print(item)
'''

#5.css选择器

t_list = bs.select('title') #标签查找
t_list = bs.select(".mnav") #类名查找
t_list = bs.select("#u1") #id查找
t_list = bs.select("a[class='text-color']") #属性查找
t_list = bs.select("head > meta") #子标签查找
t_list = bs.select(".mnav ~ .mnav") #兄弟标签查找

for item in t_list:
    print(item.get_text())
