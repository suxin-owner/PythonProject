from turtle import *

setup(500, 400)
tracer(0)  # 关闭自动刷新
width(4)

# 绘图部分
forward(200)
right(90)
pencolor('red')
forward(100)
right(90)
pencolor('green')
forward(200)
right(90)
pencolor('blue')
forward(100)
right(90)

update()  # ⭐ 手动刷新显示
done()