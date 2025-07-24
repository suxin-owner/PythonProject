#---------------------------------------------------------------------------------#
# 上下文管理器的基本结构
# __enter__
# __exit__
#---------------------------------------------------------------------------------#
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

#---------------------------------------------------------------------------------#
# 上下文管理器的基本结构
# @contextmanager
#---------------------------------------------------------------------------------#
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Alcio') as q:
    q.query()

#---------------------------------------------------------------------------------#
# closing()来把该对象变为上下文对象
#---------------------------------------------------------------------------------#
from contextlib import closing
from urllib.request import urlopen
import os

print(os.path.abspath('.'))

with closing(urlopen('https://www.python.org')) as page:
    print(type(page))

    html = page.read()
    print(html.decode('utf-8'))
    with open('/Users/suxin/Desktop/Self/Python/PythonProject/testfile_16_9_2.txt','a') as f:
        f.write(html.decode('utf-8'))

    # for i in range(20):
    #     html = page.readline()
    #     print(html.decode('utf-8'))
    #     with open('/Users/suxin/Desktop/Self/Python/PythonProject/testfile_16_9_1.txt','a') as f:
    #         f.write(html.decode('utf-8'))
