import os
print(os.name) # 操作系统类型
print(os.uname().sysname)

print(os.environ)
print(os.environ.get('USER'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/Users/suxin/Desktop/Self/Python/PythonProject', 'testdir'))

# 然后创建一个目录:
os.mkdir('/Users/suxin/Desktop/Self/Python/PythonProject/testdir')

# 删掉一个目录:
os.rmdir('/Users/suxin/Desktop/Self/Python/PythonProject/testdir')

# 拆分路径
print(os.path.split('/Users/michael/testdir/file.txt'))

# 得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# 创建新文件
from pathlib import Path

Path(r'/Users/suxin/Desktop/Self/Python/PythonProject/newfile.txt').touch(exist_ok=True)
# exist_ok=True → 已存在时不报错

# 对文件重命名:
os.rename('newfile.txt', 'test.py')

# 删掉文件:
os.remove('test.py')

# 列出当前目录下的所有目录
L1 = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L1)

# 列出所有的.py文件
L2 = [x for x in os.listdir('/Users/suxin/Desktop/Self/Python/PythonProject') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# 排序  有两个key，一个是not.isdigit() 按返回值0或者1排序，第二个是int（）排序
k1 = lambda x :(not x.split('.')[0].isdigit() , int(x.split('.')[0]) if x.split('.')[0].isdigit() else x.split('.')[0])
for n in sorted(L2 , key = k1):
    print(n)

