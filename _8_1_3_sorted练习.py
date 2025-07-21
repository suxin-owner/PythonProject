#!/user/bin/env python3
# -*- coding: utf-8 -*-

#假设我们用一组tuple表示学生名字和成绩：
#请用sorted()对上述列表分别按名字排序：
#再按成绩从高到低排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[0][1])

# 按名字排序
def by_name(t): #t = L[0] = ('Bob', 75) 以此类推
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

# 按成绩排序
def by_score(t): #t = L[0] = ('Bob', 75) 以此类推
    return t[1]

L2 = sorted(L, key=by_score, reverse = True)
print(L2)

