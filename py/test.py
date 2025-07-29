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

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_time = False
        self.pieces = []

    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            self.in_time = True

    def handle_endtag(self, tag):
        if tag == 'time':
            self.in_time = False

    def handle_data(self, data):
        if self.in_time:
            # 去掉首尾空白并过滤纯空白文本
            piece = data.strip()
            print(piece)
            if piece:
                # 把 2025 去掉，只保留月份和日期
                if '2025' not in piece:
                    self.pieces.append(piece)

parser = MyParser()
URL = 'https://www.python.org/events/python-events'
data = get_data(URL)
parser.feed(data)

# 拼接得到 '13 Aug.–14 Aug.'，再统一去掉句点
result = ''.join(parser.pieces).replace('.', '')
print(result)        # -> 13 Aug–14 Aug