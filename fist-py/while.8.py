i = 0  # 循环语句中习惯初始值为0
while i < 5:
    print('老妈，我错了')
    i += 1  # i=i+1，先算右边再赋值给左边,打印5遍
print('原谅你了')

a = 1  # 准备数据
result = 0  # 结果变量
while a <= 100:
    result = result + a  # 加法运算，前两个数结果加第三个数，每次相加result更新新的值，用下方的优化写法也可
    a += 1
print(result)  # 打印总的求和值，就不用放进循环体内了，前100的求和，可以把100调小验证一下是否正确

"""
1. 准备累加的数字 开始1 结束100 增量1
2. 准备保存结果的变量result
3. 循环加法运算 -- 如果是偶数才加法运算 -- 和2取余数为0
4. 输出结果
5. 验证结果
"""
i = 1
result = 0
while i <= 100:  # while的循环条件是1到100以内的数
    # 条件语句 -- if
    if i % 2 == 0:
        # 满足条件就做加法运算
        result += i
    i += 1  # 放进了while循环里，不放进if里面是因为不只是偶数才加一，1到100内的数

# 输出结果
print(result)
j = 0
while j <= 5:
    i = 0
    while i < j:  # 打印三角形，个数与行数相同
        print('*', end='')  # 打印取消默认换行，打印成一横
        i += 1
    print()
    j += 1
