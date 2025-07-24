#---------------------------------------------------------------------#
# # namedtuple
#---------------------------------------------------------------------#
print('--------------------------------namedtuple Start----------------------------------------')
from collections import namedtuple

Point = namedtuple('Point_a', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print('--------------------------------namedtuple End------------------------------------------')

#---------------------------------------------------------------------#
# deque
#---------------------------------------------------------------------#
print('--------------------------------deque Start----------------------------------------')
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q) 
print('--------------------------------deque End------------------------------------------')

#---------------------------------------------------------------------#
# defaultdict
#---------------------------------------------------------------------#
print('--------------------------------defaultdict Start----------------------------------------')
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
print('--------------------------------defaultdict End------------------------------------------')

#---------------------------------------------------------------------#
# OrderedDict
#---------------------------------------------------------------------#
print('--------------------------------OrderedDict Start----------------------------------------')
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的. {'a': 1, 'c': 3, 'b': 2}

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict的Key是有序的. OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(list(od.keys())) # 按照插入的Key的顺序返回

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

d = LastUpdatedOrderedDict(3)

d['a'] = 1        # add ('a', 1)
d['b'] = 2        # add ('b', 2)
d['c'] = 3        # add ('c', 3)
print(d)

d['a'] = 10       # 已存在 → del 'a' 再写 → set ('a', 10)
print(d)          # 此时顺序：b, c, a

d['d'] = 4        # 逻辑长度=3，超限 → remove ('b', 2)
print(d)          # 再 add ('d', 4)
                  # 最终顺序：c, a, d
print('--------------------------------OrderedDict End------------------------------------------')

#---------------------------------------------------------------------#
# ChainMap
#---------------------------------------------------------------------#
print('--------------------------------ChainMap Start----------------------------------------')
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print('--------------------------------ChainMap End------------------------------------------')

#---------------------------------------------------------------------#
# Counter
#---------------------------------------------------------------------#
print('--------------------------------Counter Start----------------------------------------')
from collections import Counter

c = Counter('programming')
print(c)
print('--------------------------------Counter End------------------------------------------')