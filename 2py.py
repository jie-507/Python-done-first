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
