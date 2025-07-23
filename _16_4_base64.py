str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for char in str:
    print(char, end=',')

print('\n')

# 打印每个字符及其对应的 6 位二进制值
for i, char in enumerate(str):
    # 将索引转换为 6 位二进制字符串
    binary_value = format(i, '06b')
    print(f"{i}: {binary_value}")

print('\n')
import base64

# 编码字符串
data = "ab"
encoded_data = base64.b64encode(data.encode('utf-8'))
print(encoded_data)  # 输出：b'YWI='

da1 = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(da1)
da2 = base64.b64encode(b'binarystring')
print(da2)

da3 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(da3)
da4 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(da4)
da5 = base64.urlsafe_b64decode('abcd--__')
print(da5)

#---------------------------------------------------------------------#
# 练习：请写一个能处理去掉=的base64解码函数：
#---------------------------------------------------------------------#
print('------------------------练习：请写一个能处理去掉=的base64解码函数---------------------------')
def safe_base64_decode(s):
    suffix = 4 - len(s) % 4
    if suffix != 0:
        s = s + '=' * suffix
    return base64.b64decode(s)

basestr1 = safe_base64_decode('YWJjZA==')
basestr2 = safe_base64_decode('YWJjZA')
print(basestr1)
print(basestr2)