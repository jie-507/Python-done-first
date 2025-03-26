name_list = ['Lisa', 'Tom', 'ROSE']
name = input('请输入您的名字：')
if name in name_list:
    print(f'您输入的名字是{name},此用户名已存在')
else:
    print(f'您输入的名字是{name},可以注册')

name_list.append(['ok', 'Davia'])
print(name_list)  # 追加整个序列
name_list.extend(['ok', 'Davia'])  # 把序列的数据拆开再逐步加入，字符串也会拆开
print(name_list)
name_list.extend('xiaoming')
print(name_list)

# 删除操作
# del目标，可以直接删除列表，也可以删除列表指定下标数据
# 列表序列.pop（下标）删除，也是删除指定下标数据，如果不写默认删除最后一个，并返回该数据
# 列表序列.remove（数据），移除某一项
# 列表序列.clear（），清空这个列表里的数据

# 修改操作，最基础的可以修改下标数据来完成
# 列表序列.reverse（）把里面的数据进行逆置，就是反过来12345变成54321
# 排序， 列表序列.sort( key=None, reverse=False)，reverse=False是升序，reverse=Ture是降序，括号内不填默认升序
# 复制是copy（）
