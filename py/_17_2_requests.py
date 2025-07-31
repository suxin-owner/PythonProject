#---------------------------------------------------------------------------------#
# get
#---------------------------------------------------------------------------------#
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get('https://www.douban.com', headers=headers)
print(r.status_code)
print(r.text)

print('-----------------------------------------------------------------------------------')
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'}, headers=headers)
print(r.url)   # 实际请求的URL
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.content)
print(r.headers['Content-Type'])
# print(r.cookies['ts'])

print('-----------------------------------------------------------------------------------')
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

#---------------------------------------------------------------------------------#
# post
#---------------------------------------------------------------------------------#
r = requests.get('https://accounts.douban.com/login', headers=headers)
print(type(r.text))
with open('/Users/suxin/Desktop/Self/Python/PythonProject/_17_2_HTMLfile.txt','w') as f:
    f.write(r.text)

r = requests.post('https://accounts.douban.com/login', 
                  data={'form_email': 'abc@example.com', 'form_password': '123456'}, 
                  headers=headers)
# print(r.status_code, r.reason)
# print(r.headers)
# print(r.text)
# 检查响应状态码
if r.status_code == 200:
    print("请求成功")
else:
    print(f"请求失败，状态码: {r.status_code}")

# 检查响应内容
if '登录成功' in r.text:
    print("登录成功")
else:
    print("登录失败")

