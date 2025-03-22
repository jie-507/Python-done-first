# 随机数 导入模块 import random
# 使用功能 random.randint()因为随机一个整数所以int

import random
num = random.randint(0, 8)  # 0到2之间开始结束
print(num)


# 下标或者索引
str1 = 'abcdefg'
print(str1)
print(str1[0])  # 得到a
print(str1[3])

#  切片，字符串，列表，元组都有这个操作
#  序列[开始位置下标：结束位置下标：步长]（左闭右开）步长可以不写默认为1
print(str1[2:5:1])
print(str1[2:5:2])  # 选取间隔为2
print(str1[:5])  # 不写开始默认从0开始
print(str1[2:])  # 不写结束默认到结尾,不写开始结束是选所选全部
print(str1[::-1])  # 如果步长为负数，表示倒叙选取
print(str1[-4:-1])  # 最后一个为-1，还是遵循左闭右开原则

# 查找字符串 语法：字符串序列.find（字串，开始位置下标，结束位置下标）不在会显示-1
mystr = "hello world and itcast and itheima and Python"
print(mystr.find('and'))  # 12 and开始字符下标为12
print(mystr.find('and', 15, 30))  # 23从15到30开始查找
print(mystr.find('ands', 15, 30))  # -1 不存在
# index()
# print(mystr.index('and'))
print(mystr.index('and', 15, 30))
# print(mystr.index('ands', 15, 30))  # 如果index查找子串不存在，报错
# count()统计次数
print(mystr.count('and', 15, 30))
print(mystr.count('and'))
print(mystr.count('ands'))

# replace():替换    字符串序列.replace(旧字串，新子串，替换次数）省略不写代表全部替换
new_str = mystr .replace('and', 'he', 2)  # 次数大于个数时说明全部替换
print(mystr)
print(new_str)
# *****调用了replace函数后，原有字符串的数据并没有做到修改，修改后的数据是返回值，要新的变量接收
# ---说明字符串是不可变数据类型————————，数据是否可以改变划分为：可变类型 和不可变类型
# split() -- 分割， 返回一个列表，丢失分割字符
list1 = mystr.split('and')
print(list1)
list2 = mystr.split('and', 2)
print(list2)

# join() -- 合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
# 结果aa...bb...cc
new_str = '...'.join(mylist)
print(new_str)

# capitalize():将字符串第一个字符转化为大写。2.title（）：将字符串每个单词首字母转化为大写
# lower（）；大写转小写  2.upper（）小写转大写
new_str = mystr.capitalize()
print(new_str)
new_str = mystr.title()
print(new_str)
# lstrip();删除字符串左侧空白字符。 2.rstrip();删除字符串右侧空白字符。  3.strip();删除字符串两侧空白字符。
mystr = "     hello world and itcast and itheima and Python      "
print(mystr)  # 运行结果处拖拽就可以看到有没有空白符
new_str = mystr.lstrip()
print(new_str)
new_str = mystr.strip()
print(new_str)

# 字符串序列.ljust(长度,填充字符），左对齐。  2.rjust右对齐   3.center，居中。

# startswith()判断是否以某一个开头结果为布尔值Ture或者False。 2 endswith()判断是否以某一个为结尾
mystr = 'hello world and itcast and itheima and Python'
print(mystr.startswith('hello'))
print(mystr.endswith('Pythons'))
# 判断
# isalpha():如果字符串至少有一个字符并且所有字符全是字母则，返回Ture
# isdigit():如果字符串至只包含数字，则返回Ture
# isalnum():如果字符串至少有一个字符并且所有字符全是字母或数字或者组合，则返回Ture
# isspace():如果字符串至只包含空白，则返回Ture
print(mystr.isalpha())  # 里面包含空格，不是全是字母所以是False
mystr2 = '12345'
mystr3 = 'abc123'
print(mystr2.isdigit())
print(mystr.isalnum())
print(mystr3.isalnum())