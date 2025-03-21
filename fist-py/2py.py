a = 135
b = 98
c = 129
number = a * b
if number > a*c:
    print(number)
elif b*c > a*c:
    number = b*c
    print(number)
else:
    number = a*c
    print(number)


age = 20
height = 175
weight = 80
BMI = weight/(height * height)
if (17 <= age <= 27) and (169 <= height <= 185):
    print("ok")
else:
    print("no")
if BMI <= 18.5:
    print("过轻")
elif 18.5 < BMI <= 24:
    print("正常")
elif 24 < BMI <= 28:
    print("过重")
elif 28 < BMI <= 32:
    print("肥胖")
elif BMI > 32:
    print("过于肥胖")
