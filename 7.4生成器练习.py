#杨辉三角定义如下：
#          1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles(x):
    a = [1]
    n = 1
    while n <= x:
        yield a
        #print(range(1, len(a)))
        a = [1] + [a[x-1] + a[x] for x in range(1, len(a))] + [1]
        n = n + 1
        

d = triangles(7)
while True :
    try:
        x = next(d)
        print('d:',x)
    except StopIteration as e :
        print('Generator return value:',e.value)
        break 

