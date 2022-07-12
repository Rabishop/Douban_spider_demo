# 正则表达式：字符串模式（判断字符是否符合一定标准）

import  re

# 创建模式对象

# pat = re.compile("AA") # 此处的AA，是正则表达式，用于匹配其他字符串
# m = pat.search("CBAA") # search字符串被校验的内容
#
# print(m)
#
# 无模式对象
#
# m = re.search("asd", "Aasd") #前面是规则，后面是被校验的字符串
# print(m)
#
# print(re.findall("a", "AdagagdsaAAfdga")) #前面是规则，后面是被校验的字符串
# print(re.findall("[a-z]", "AdagagdsaAAfdga")) #前面是规则，后面是被校验的字符串

# print(re.findall("[a-z]+", "AdagagdsaAAaAfdga")) #前面是规则，后面是被校验的字符串

# sub替换

# print(re.sub("a", "A", "fasfafasfa")) #找到a用A替换，在第三个中找

#建议在正则表达式中， 被比较字符中加上r，不用担心转义

a = r"\aabd-\'";
b = "\aabd-\'";

print(a) # 输出 \aabd-\'
print(b) # 输出 abd-'


