import tkinter as tk
from PIL import Image, ImageTk
import os

# 创建主窗口
root = tk.Tk()
root.title("Label 示例")
root.configure(bg="white")  # 防深色背景

# 创建一个 Label 控件，显示文本
label1 = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16), fg="blue", bg="lightgray")
label1.pack(pady=10)

# 创建一个 Label 控件，显示图像
img = Image.open("/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p1.png")
print("/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p1.jpg")
print("图片尺寸:", img.size)
img = img.resize((300, 200))  # 缩小图片

photo = ImageTk.PhotoImage(img)
label2 = tk.Label(root, image=photo)
# label2.image = photo  # 防止被垃圾回收
label2.pack(pady=10)

# 创建一个 Label 控件，显示多行文本
label3 = tk.Label(root, text="这是一个多行文本示例。\n第二行文本。", justify="left", padx=10, pady=10)
label3.pack(pady=10)

if not os.path.exists("/Users/suxin/Desktop/Self/Python/PythonProject/JPG/17_1_p1.jpg"):
    print("文件不存在，请检查路径")
else:
    print("文件存在")

root.attributes('-topmost', True)  # 置顶窗口

# 运行主循环
root.mainloop()



from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("test")
root.configure(bg="red")

photo = tk.PhotoImage(file="/Users/suxin/Desktop/Self/Python/PythonProject/JPG/test.gif")

lab = tk.Label(root, image=photo, bg="red")
lab.pack(pady=10)

print("/Users/suxin/Desktop/Self/Python/PythonProject/JPG/test.gif")

root.attributes('-topmost', True)  # 置顶窗口

root.mainloop()
