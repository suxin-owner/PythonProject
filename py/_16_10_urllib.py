#---------------------------------------------------------------------------------#
# get
# # 抓取url，并返回响应
#---------------------------------------------------------------------------------#
from urllib import request

with request.urlopen('https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print(data.decode('utf-8'))

#---------------------------------------------------------------------------------#
# 模拟浏览器发送GET请求
#---------------------------------------------------------------------------------#
from urllib import request

req = request.Request('https://httpbin.org/headers')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

from urllib.request import urlopen, Request

url = 'https://httpbin.org/headers'
req = Request(url, headers={'User-Agent': 'MyBot/1.0'})
with urlopen(req) as resp:
    print(resp.read().decode())

#---------------------------------------------------------------------------------#
# Post
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
#---------------------------------------------------------------------------------#
from urllib import request, parse

print("Login to weibo.cn...")
email = input("Email: ")
passwd = input("Password: ")
# body 
login_data = parse.urlencode([("username", email), 
                              ("password", passwd), 
                              ("entry", "mweibo"), 
                              ("client_id", ""), 
                              ("savestate", "1"), 
                              ("ec", ""), 
                              ("pagerefer", "https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom&jumpfrom=weibocom")])

# 响应体中的请求头
req = request.Request("https://passport.weibo.cn/sso/login")
req.add_header("Origin", "https://passport.weibo.cn")   # 请求来自哪个源
req.add_header("User-Agent", "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
req.add_header("Referer", "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom")

with request.urlopen(req, data=login_data.encode("utf-8")) as f:
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", f.read().decode("utf-8"))

import json
from urllib.request import urlopen, Request

payload = json.dumps({'key': 'value'}).encode()

req = Request('https://httpbin.org/post',
              data=payload,
              headers={'Content-Type': 'application/json/',  # 发过去的请求头，并不是真的响应头
                      'Accept-Encoding': 'gzip'},
              method='POST')

with urlopen(req) as resp:
    print('状态码:')
    print(resp.status, '\n')            
    print('响应头:')
    print(resp.headers, '\n')  
    print('响应体:')
    print(resp.read().decode(),'\n') 
    print(resp.getheader('Content-Type'))  # 获取单个响应头



    
