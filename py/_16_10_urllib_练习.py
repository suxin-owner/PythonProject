#---------------------------------------------------------------------------------#
# 练习
# 利用urllib读取JSON，然后将JSON解析为Python对象：
#---------------------------------------------------------------------------------#

import json
from urllib import request

class DictPrinter:
    def __init__(self, data):
        self.data = data

    def print_dict(self, data=None, indent=0):
        """
        递归打印多层嵌套字典
        :param data: 当前层级的字典数据
        :param indent: 当前缩进级别
        """
        if data is None:
            data = self.data

        # 遍历字典的键值对
        for key, value in data.items():
            # 打印当前键值对，带缩进
            print(" " * indent + f"{key}: ", end="")
            if isinstance(value, dict):
                # 如果值是字典，递归打印
                print()
                self.print_dict(value, indent + 4)
            else:
                # 如果值不是字典，直接打印
                print(value)

def fetch_data(url):
    # 发送 HTTP GET 请求
    with request.urlopen(url) as response:
        # 读取响应内容
        raw_data = response.read()
        # 将 JSON 数据解析为 Python 字典
        data = json.loads(raw_data)
        return data

URL = 'https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'
data = fetch_data(URL)

printer = DictPrinter(data)
print(printer.print_dict())