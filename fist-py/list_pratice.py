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
