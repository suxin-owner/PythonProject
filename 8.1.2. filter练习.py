#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
#str(n)：将整数 n 转换为字符串。
#[::-1]：字符串切片操作，表示从后向前以步长 -1 取出所有字符（即反转字符串）。

def is_palindrome(n):
    return str(n)[::-1] == str(n)[::]

output = filter(is_palindrome, range(1, 200))
print(list(output))

    