ticket = True
contraband = True
if ticket:
    print("车票通过，准备安检")
    if contraband:
        print("不可以上车")
    else:
        print("安检通过")
else:
    print("请先购票")

age = 13
if age >= 12:
    print("负刑事责任")
else:
    print("未达到负刑事责任")

a = 1900
if a % 4 != 0:
    print(f"{a}不是闰年")
elif a % 100 == 0 and a % 400 != 0:
    print(f"{a}不是闰年")
else:
    print(f"{a}是闰年")


number = 123
a1 = number // 100
a2 = number // 60
a3 = number % 60
result = a3*100 + a2*10+a1
print(result)


studentName = ("小明", "小叶", "小曲")
name = "路飞"
mathScore = (90, 80, 85)
if name in studentName:
    print("yes")
else:
    print("no")
print(f"{studentName[0]}的数学成绩是{mathScore[0]}")
print(f"{studentName[1]}的数学成绩是{mathScore[1]}")
print(f"{studentName[2]}的数学成绩是{mathScore[2]}")
