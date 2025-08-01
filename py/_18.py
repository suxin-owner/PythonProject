# from tkinter import *
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!', font=("Arial", 16))
#         self.helloLabel.pack()
#         self.hello1 = Label(self, text='Hello')
#         self.hello1.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# app.master.geometry("400x300+100+100") # 宽度为 400 像素，高度为 300 像素，窗口左上角位于屏幕 (100, 100) 位置

# app.master.attributes('-topmost', True)  # 置顶窗口

# # 主消息循环:
# app.mainloop()


from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
app.master.attributes('-topmost', True)  # 置顶窗口
# 主消息循环:
app.mainloop()
