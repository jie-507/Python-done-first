gasd = [13, 14, 15, 16, 18]
print(gasd)
gasd[4] = 17
print(gasd)
# 最后末尾加入append
gasd.append(19)
print(gasd)
# 插入insert，可以选插入位置和内容
gasd.insert(5, 18)
print(gasd)
# 删除pop，括号内填索引即可，不填默认删除最后一个
gasd.pop(1)
print(gasd)
# 查找内容个数，len
print(len(gasd))


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