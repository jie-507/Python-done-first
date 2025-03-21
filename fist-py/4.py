number = (1, 2, 3, 4, 5)
position = ("东", "西", "南", "北")
result1 = 2 in number
result2 = 9 in number
result3 = "中" in position
print(result1)
print(result2)
print(result3)
print(number[0])
print(number[2])

age = 18
name = 'tom'
weight = 75.5
stu_id = 1
stu_id2 = 1000
print("我的年龄是%d岁" % age)
print("我的名字是%s" % name)
print("我的体重是%.2f公斤" % weight)  # 一般默认保留6位小数点，加.2表示保留俩位小数
print("我的学号是%d" % stu_id)
print("我的学号是%03d" % stu_id)  # 不足的用0补全，超出的原样输出
print("我的学号是%03d" % stu_id2)
print("我的名字是%s,今年%d岁了" % (name, age))
print("我的名字是%s,明年%d岁了" % (name, age + 1))
print("我的名字是%s, 今年%d岁了, 体重%.2f, 公斤学号是%06d" % (name, age, weight, stu_id))
print(f"我的名字是{name},今年{age}岁了")
print(f"我的名字是{name},今年{age + 1}岁了")
print(f"我的名字是{name},\n今年{age}岁了")  # 转义字符换行\n
print("\tabcd")  # 制表符一个tab距离四个空格号/t

a = 1
b = 2
c = a if a > b else b
print(c)
