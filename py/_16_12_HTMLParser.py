# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''
#                 <time datetime="2025-08-13T00:00:00+00:00">13 Aug.
#         <span id="start-2077" class="say-no-more">
#             2025
#         </span>

#          &ndash;
#             14 Aug.
        

#         <span id="end-2077" class="say-no-more">
#             2025
#         </span>
#     </time>''')


#---------------------------------------------------------------------------------#
# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，
# 用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
#---------------------------------------------------------------------------------#
from html.parser import HTMLParser
from urllib.request import Request,urlopen
import re, gzip, io

def get_data(url):
   '''
   GET请求到指定的页面
   :return: HTTP响应
   '''

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
      }
   req = Request(url, headers=headers)
   with urlopen(req, timeout=25) as f:
      data = f.read()
      raw = gzip.GzipFile(fileobj=io.BytesIO(data)).read()
      print(f'Status: {f.status} {f.reason}')
      # 查看服务器返回的是不是压缩流
      print('---------------------------------------------------------------------')
      print(f.headers.get('Content-Encoding'))
      print('---------------------------------------------------------------------')
      return raw.decode("utf-8")

class MyHTMLParser(HTMLParser):
   def __init__(self):
      super().__init__()
      self.__parsedata_name = False # 设置一个空的标志位
      self.__parsedata_time = False
      self.__parsedata_year = False
      self.__parsedata_location = False
      self.info = []
      self.time = []
      self.year = []
      self.num = 0

   def handle_starttag(self, tag, attrs):
      print(attrs)
      if ('class', 'event-title') in attrs:
         self.__parsedata_name = True  # 通过属性判断如果该标签是我们要找的标签，设置标志位
      if tag == 'time':
         self.__parsedata_time = True
      if ('class', 'say-no-more') in attrs:
         self.__parsedata_year = True
      if ('class', 'event-location') in attrs:
         self.__parsedata_location = True

   def handle_endtag(self, tag):
      if tag == 'time':
        self.__parsedata_time = False    # 在HTML 标签结束时，把标志位清空
        result = ''.join(self.time).replace('.', '')
        self.info.append(f'会议时间:{result}')
        self.time.clear()
        self.info.append(f'会议年份:{self.year[0]}')
        self.year.clear()

      self.__parsedata_name = False
      self.__parsedata_year = False
      self.__parsedata_location = False
      
   def handle_data(self, data):
      if self.__parsedata_name :
         # 通过标志位判断，输出打印标签内容
         self.num += 1
         self.info.append(f'会议号: %5d' % self.num)
         self.info.append(f'会议名称:{data}')

      if self.__parsedata_time :
         if data.strip() != '2025' :
            self.time.append(data.strip().replace('–\n            ', '-'))

      if self.__parsedata_year :
        if re.match(r'\d{4}', data.strip()): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
            self.year.append(data.strip())

      if self.__parsedata_location :
         self.info.append(f'会议地点:{data} \n')

parser = MyHTMLParser()
URL = 'https://www.python.org/events/python-events'
data = get_data(URL)
parser.feed(data)
for s in parser.info:
    print(s)

with open('/Users/suxin/Desktop/Self/Python/PythonProject/HTMLfile_16_12.txt','w') as f:
    f.write(data)


