#---------------------------------------------------------------------------------#
# 最常见的哈希算法:MD5
#---------------------------------------------------------------------------------#
print('------------------------MD5 Start---------------------------')
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
str1 = md5.hexdigest()
print(str1, len(str1))

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
print('------------------------MD5 End-----------------------------')
#---------------------------------------------------------------------------------#
# 另一种常见的哈希算法:SHA1
#---------------------------------------------------------------------------------#
print('------------------------SHA1 Start---------------------------')
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
str2 = sha1.hexdigest()
print(str2, len(str2))
print('------------------------SHA1 End-----------------------------')
#---------------------------------------------------------------------------------#
# 练习1:根据用户输入的口令，计算出存储在数据库中的MD5口令：
#      存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
#      设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
#---------------------------------------------------------------------------------#
print('------------------------练习1 Start---------------------------')
import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calc_md5(password):
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    return pw_md5.hexdigest()

def login(user, password):
    pw = calc_md5(password)
    if db[user] == pw:
        return True
    else:
        return False

print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))
print(login('michael', '1234567'))
print(login('bob', '123456'))
print(login('alice', 'Alice2008'))
print('------------------------练习1 End-----------------------------')
#---------------------------------------------------------------------------------#
# 练习2:根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
#      然后，根据修改后的MD5算法实现用户登录的验证
#---------------------------------------------------------------------------------#
print('------------------------练习2 Start---------------------------')
import hashlib, random

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(self, password)

def get_md5(user, password):            # 第一个参数是一个User对象 User(username, password)
    pw_md5 = hashlib.md5()
    pw_md5.update(f'{password + user.salt}'.encode('utf-8'))
    return pw_md5.hexdigest()

db = {}

def register(username, password):
    db[username] = User(username, password)

def login(username, password):
    user = db[username]                        # 取得的是一个User对象 User(username, password)
    print('username:', username, 'password:', user.password, len(user.password))
    print('username:', username, 'password:', get_md5(user,password))
    return user.password == get_md5(user,password)

register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))
print(login('michael', '1234567'))
print(login('bob', '123456'))
print(login('alice', 'Alice2008'))
print('------------------------练习2 End-----------------------------')








