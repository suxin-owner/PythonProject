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