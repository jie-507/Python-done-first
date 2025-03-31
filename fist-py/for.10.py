number = [10, 20, 30, 40, 50]
for i in number:  # 赋值给i，第一变是10，第二遍是20
    print(i)
else:
    print('over')


# 打印一个列表让值变一半
numberList = [10, 20, 30, 40, 50, 60]
newList = []
for a in numberList:
    b = a / 2
    newList.append(b)
print(newList)  # 因为结果只要一个表，把print放在外面打印最后的结果

products = {'可乐': 10, '薯条': 15, '冰淇淋': 5}
for key in products:
    print(key)  # 打印键
    print(products[key])  # 对应打印键相应的值
    # 这两个完成算一次循环，根据表中总共循环三次才结束，这种也称为遍历，有序的
for key in products:
    print(f'{key}的价格是{products[key]}')
