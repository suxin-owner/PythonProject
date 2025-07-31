#---------------------------------------------------------------------------------#
# 操作图像
#---------------------------------------------------------------------------------#
import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

print('当前路径：', os.path.abspath('.'))

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_test.jpg')

# 获得图像尺寸:
w, h = im.size
print(w, h, im.size)
print('Original image size: %sx%s' % (w, h))
#---------------------------------------------------------------------------------#
# 缩放到50%:
#---------------------------------------------------------------------------------#
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
#---------------------------------------------------------------------------------#
# 切片图像 (左上角坐标, 右下角坐标)
# (x1, y1, x2, y2)
#---------------------------------------------------------------------------------#
p1 = im.crop((0, 0, 300, 300))
print('截图尺寸：', '\n', '(x1, y1, x2, y2)', '\n', '(0, 0, 300, 300)')
#---------------------------------------------------------------------------------#
# 图像旋转
#---------------------------------------------------------------------------------#
p2 = im.rotate(90)
#---------------------------------------------------------------------------------#
# 应用滤镜
# 模糊、边缘增强
#---------------------------------------------------------------------------------#
# 应用模糊滤镜
p3 = im.filter(ImageFilter.BLUR)
# 应用边缘增强滤镜
p4 = im.filter(ImageFilter.EDGE_ENHANCE)
#---------------------------------------------------------------------------------#
# 添加文字
#---------------------------------------------------------------------------------#
# 创建一个可以在给定图像上绘图的对象
draw = ImageDraw.Draw(im)
# 定义字体和文字内容
font = ImageFont.truetype("/Library/Fonts/Supplemental/Arial.ttf", 36)  # 使用 Arial 字体，大小为 36
text = "Hello, Pillow!"
# 在图像上添加文字
draw.text((50, 50), text, font=font, fill=(255, 0, 0))  # 填充颜色为红色
#---------------------------------------------------------------------------------#
# 调整调色板
#---------------------------------------------------------------------------------#
# 转换为灰度图像
p5 = im.convert('L')
# 转换为二值化图像
p6 = im.convert('1')

#把缩放后的图像用jpeg格式保存:
im.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_thumbnail.jpg', 'jpeg')
p1.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p1.jpg')
p2.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p2.jpg')
p3.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p3.jpg')
p4.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p4.jpg')
p5.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p5.jpg')
p6.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p6.jpg')

#---------------------------------------------------------------------------------#
# 生成字母验证码图片
#---------------------------------------------------------------------------------#
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 图片像素 240 x 60:
width = 60 * 4
height = 60
# 创建一个新的图像
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/Library/Fonts/Supplemental/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_code.jpg', 'jpeg')
