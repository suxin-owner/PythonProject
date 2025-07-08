#利用切片操作，实现一个trim()函数，去除字符串首尾的空格

def trim(s):
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1
    
    return s[start:end+1] if start <= end else ""

b = '  ABC  '

print(trim(b))
print(len(b))
print(b[0:3])