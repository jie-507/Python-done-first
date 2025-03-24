products = {'可乐': 10, '薯条': 15, '冰淇淋': 5}  # 字典没有顺序，没有索引，只能通过字典的键来找对应的值，键与值用：隔开
print(products)
print(products['薯条'])
# 字典的添加与修改，还有注意中括号
# 字典的键不能重复，可以对已存在的键重新赋值
products['other'] = '七折'
print(products)
products['可乐'] = 8
print(products)
# 查找键keys，后面跟了括号
print(products.keys())
a = '炸鸡' in products.keys()
print(a)  # 考验in运算，布尔值
# print(products[1:2])  #不能对字典使用索引或者切片
num = products['可乐']
if num <= 10:
    products['可乐'] = '可乐降价了'
print(products)
