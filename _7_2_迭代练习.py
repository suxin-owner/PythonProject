#请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if L == [] :
        return(None,None)
    
    max_value = min_value = L[0]
    
    for x in L:
        if x >= max_value :
            max_value = x
        if x <= min_value :
            min_value = x
    
    return (max_value,min_value)

L = [1,2,3,4,5]

print(findMinAndMax(L))