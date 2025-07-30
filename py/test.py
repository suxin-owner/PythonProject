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
'''

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到 <time> 标签
time_tag = soup.find('time')

# 提取日期范围
date_parts = []
for element in time_tag.contents:
    if element.name != 'span':
        date_parts.append(element.strip())

# 拼接日期范围
date_range = ' '.join(date_parts)
print(date_range)  # 输出: 13 Aug. – 14 Aug.