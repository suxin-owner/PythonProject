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
      print()
      # 查看服务器返回的是不是压缩流
      print('---------------------------------------------------------------------')
      print(f.headers.get('Content-Encoding'))
      print('---------------------------------------------------------------------')
      return raw.decode("utf-8")

class MyHTMLParser(HTMLParser):
   def __init__(self):
      super().__init__()
      self.__parsedata = 'name' # 设置一个空的标志位
      self.info = []

   def handle_starttag(self, tag, attrs):
    #   if ('class', 'event-title') in attrs:
    #      self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
      if tag == 'time':
         self.__parsedata = 'time'
    #   if ('class', 'say-no-more') in attrs:
    #      self.__parsedata = 'year'
    #   if ('class', 'event-location') in attrs:
    #      self.__parsedata = 'location'

   def handle_endtag(self, tag):
      if tag == 'time':
        self.__parsedata = ''# 在HTML 标签结束时，把标志位清空

   def handle_data(self, data):

    #   if self.__parsedata == 'name':
    #      # 通过标志位判断，输出打印标签内容
    #      self.info.append(f'会议名称:{data}')

      if self.__parsedata == 'time':
         print(data)
         self.info.append(f'会议时间:{data}')

    #   if self.__parsedata == 'year':
    #      if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
    #         self.info.append(f'会议年份:{data}')

    #   if self.__parsedata == 'location':
    #      self.info.append(f'会议地点:{data} \n')

parser = MyHTMLParser()
URL = 'https://www.python.org/events/python-events'
# URL = 'https://www.baidu.com'
data = get_data(URL)
with open('/Users/suxin/Desktop/Self/Python/PythonProject/HTMLfile_16_12.txt','w') as f:
    f.write(data)
parser.feed(data)
# for s in parser.info:
#     print(s)


