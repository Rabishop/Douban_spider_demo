from bs4 import BeautifulSoup

file = open("./final.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")

#文档的遍历

for item in bs.div.contents:
    print(item.string, end="")
    if(item.string.endswith("。")):
        print("\n")