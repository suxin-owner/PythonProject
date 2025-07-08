#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
#>>> L = ['Hello', 'World', 18, 'Apple', None]
#>>> [s.lower() for s in L]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 1, in <listcomp>
#AttributeError: 'int' object has no attribute 'lower'
#使用内建的isinstance函数可以判断一个变量是不是字符串：
#>>> x = 'abc'
#>>> y = 123
#>>> isinstance(x, str)
#True
#>>> isinstance(y, str)
#False
#使用内建的isinstance函数可以判断一个变量是不是字符串：

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

print(L2)

