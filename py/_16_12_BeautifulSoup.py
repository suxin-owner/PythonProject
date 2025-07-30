from bs4 import BeautifulSoup

html_content = '''
<time datetime="2025-08-13T00:00:00+00:00">13 Aug.
    <span id="start-2077" class="say-no-more">
        2025
    </span>
     &ndash;
        14 Aug.
    <span id="end-2077" class="say-no-more">
        2025
    </span>
</time>
<html>
<head>
    <title>示例网页</title>
</head>
<body>
    <h1>欢迎来到示例网页</h1>
    <p>这是一个段落。</p>
    <a href="https://example.com" class="link">示例链接</a>
    <ul>
        <li>列表项 1</li>
        <li>列表项 2</li>
    </ul>
</body>
</html>
'''

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到 <time> 标签
time_tag = soup.find('time')
print(type(time_tag))
print(time_tag)

# 提取日期范围
date_parts = []
print(time_tag.contents)
for element in time_tag.contents:
    print(element)
    if element.name != 'span':
        date_parts.append(element.strip())

# 拼接日期范围
date_range = ' '.join(date_parts)
print(date_range)  # 输出: 13 Aug. – 14 Aug.

# 获取 <body> 标签
body = soup.body

# 使用 .contents 遍历 <body> 的所有子节点
for child in body.contents:
    print(child.name)

for child in body.descendants:
    if child.name != None:
        print(child.name, child.text)
