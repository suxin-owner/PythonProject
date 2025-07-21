#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

from functools import reduce


def normalize(N1):
    return N1[0].upper() + N1[1:].lower()

N1 = ['adam', 'LISA', 'barT']
N2 = map(normalize,N1)
print(list(N2))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(x,y):
    return x * y

L1 = [3,5,7,9]
result = reduce(prod,L1)
print(result)

#简便写法
def prod2(L1):
    def chengJi(x,y):
        return x * y
    return reduce(chengJi,L1)

f = prod2(L1)
print(f)

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

S = '123.456'

def str2float(s):

    def fn(x, y):
        return x * 10 + y
    
    def char2int(_char):
        _dict = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9}
        return _dict[_char]
    
    return reduce(fn,map(char2int, S.split('.')[0])) + reduce(fn,map(char2int, S.split('.')[1]))/1000

print(str2float(S))
