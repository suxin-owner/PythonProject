from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text.strip())

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python suxin</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

#---------------------------------------------------------------------------------#
# 练习
# 请利用SAX编写程序解析WeatherAPI的XML格式的天气预报，获取天气预报：
#---------------------------------------------------------------------------------#
from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandler(object):
    def __init__(self):
        self.result = {'city': {}, 'weather': {}}
        self.current_tag = ""
        self.is_in_location = False
        self.is_in_current = False
        self.is_in_condition = False

    def start_element(self, name, attrs):
        self.current_tag = name

        if name == 'location':
            self.is_in_location = True
        elif name == 'current':
            self.is_in_current = True
        elif name == 'condition':
            self.is_in_condition = True

    def end_element(self, name):
        if name == 'location':
            self.is_in_location = False
        elif name == 'current':
            self.is_in_current = False
        elif name == 'condition':
            self.is_in_condition = False
        self.current_tag = ""

    def char_data(self, text):
        if self.is_in_location:

            if self.current_tag in ['name', 'region', 'country', 'lat', 'lon', 'tz_id', 'localtime']:
                self.result['city'][self.current_tag] = text

        elif self.is_in_current:

            if self.current_tag in ['last_updated', 'temp_c', 'temp_f', 'is_day']:
                self.result['weather'][self.current_tag] = text

            if self.is_in_condition and self.current_tag == 'text':

                if 'condition' not in self.result['weather']:
                    self.result['weather']['condition'] = {}
                self.result['weather']['condition']['text'] = text

            if self.current_tag in ['wind_kph', 'wind_dir', 'pressure_mb', 'humidity', 'cloud', 
                                    'feelslike_c', 'uv']:
                self.result['weather'][self.current_tag] = text

def parseXml(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data

    parser.Parse(xml_str)
    print(handler.result)
    return handler.result

# 测试:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result['city']['name'])
