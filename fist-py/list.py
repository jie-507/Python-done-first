gasd = [13, 14, 15, 16, 18]
print(gasd)
gasd[4] = 17
print(gasd)
# 最后末尾加入append，增加数据，列表名.append（数据），extend也可以在结尾追加
gasd.append(19)
print(gasd)
# 插入insert，可以选插入位置和内容
gasd.insert(5, 18)
print(gasd)
# 删除pop，括号内填索引即可，不填默认删除最后一个
gasd.pop(1)
print(gasd)
# 访问列表长度，即列表中数据的个数，len(序列名)
print(len(gasd))
# 序列.index(数据，开始下标，结束下标），还能查找该数据的位置，只填数据就行,不存在就会报错
# print(gasd.index(150))  ,报错
print(gasd.index(15))  # 说明15在1的位置
print(gasd.index(15, 0, 2))  # 存在则出1，若查找不存在则报错
# 统计出现次数，序列名.count（），不存在就会出现0
gasd[5] = 15
print(gasd.count(15))  # 有两个15，所以输出2
# 序列.insert(位置下标，数据），指定位置增加数据
gasd.insert(0, 9)
print(gasd)


# 练习
rank_list = [100, 98, 88, 80, 75, 64]
score = 70
if score >= rank_list[5]:
    rank_list.pop()
    rank_list.append(score)
print(rank_list)
bag = 50
if bag in rank_list:
    print(f'{bag}在rank_list中')
else:
    print(f'{bag}不在rank_list中')
print(rank_list[1: 4])
rank_list.pop(1)
print(rank_list)
rank_list.insert(1, 99)
rank_list.insert(2, 98)
rank_list.insert(4, 87)
print(rank_list)
# not in 判断不在，与in判断一样的
print(60 not in rank_list)
