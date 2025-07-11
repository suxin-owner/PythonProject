#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：

from functools import reduce

def str2num(s):
    if '.' in s:                     #在s字符串中检查是否有'.'
        return float(s)
    else:
        return int(s)                #int() 强制转换会自动去掉前后空格，中间的空格去除不了

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
