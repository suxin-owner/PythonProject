#---------------------------------------------------------------------------------#
# 练习：计算圆周率可以根据公式
#      利用Python提供的itertools模块，我们来计算这个序列的前N项和
#---------------------------------------------------------------------------------#
import itertools

def pi(N):
    index = 0
    sum = 0
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    for i in list(itertools.islice(natuals, N)):
        #print('i = ', i)
    # # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    #     if index % 2 == 0:
    #         num = -(4 / i)
    #     else:
    #         num = 4 / i
    #     #print('num = ', num) 
    # # step 4: 求和:
    #     sum = sum + num
    #     #print('sum = ', sum) 
        sum = sum + (4 / i * (-1) ** index)
        index += 1
    return  sum

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))


