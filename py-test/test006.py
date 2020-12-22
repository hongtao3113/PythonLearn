'''
Created on 2018年5月23日

@author: wk
'''
import tkinter #导入支持库
def def1():
    """按钮1"""
    var1.set('看，我变啦！')

def def2():
    '''按钮2'''
    var2.set("百叶窗折射的光影")

def def3():
    '''按钮3'''
    var3.set('因为中间空白的时光 如果还能分享 也是一种浪漫')

root = tkinter.Tk()#创建一个root窗口
root.title('我只是一个测试的窗口')#设置窗口标题
bt = tkinter.Button(root, text="我是来占位的").pack(fill=tkinter.X, side=tkinter.TOP)
# root.geometry('500x300+300+300')#设置窗口的大小及位置
m_frame = tkinter.Frame(root)# 一个部件容器
m_frame.pack(fill=tkinter.X, side=tkinter.TOP)
# 创建一个快捷方式,用来生成小部件。
LEFT, Label, Buttom = tkinter.LEFT, tkinter.Label, tkinter.Button
label_line = tkinter.Frame(m_frame, relief=tkinter.RAISED, borderwidth=1)# 创建一个容器放入info_frame中
label_line.pack(side=tkinter.TOP, padx=2, pady=2)
var1 = tkinter.StringVar()
var1.set('默认文字')
var2 = tkinter.StringVar()
var2.set('听见下雨的声音')
var3 = tkinter.StringVar()
var3.set("#眼角的泪这不是错觉")
# fg="red" 文字颜色,颜色可以接受"cc0000" WEB颜色值等。
l1 = Label(label_line, width=20, textvariable=var1, fg="#c00").pack(side=LEFT)
l2 = Label(label_line, width=20, textvariable=var2, bg="#c00").pack(side=LEFT)
# show='*' 可以使文本框内容显示为*****
e3 = tkinter.Entry(label_line, textvariable=var3).pack(side=LEFT)

buttom_line = tkinter.Frame(m_frame)
buttom_line.pack(side=tkinter.BOTTOM, padx=2, pady=1)
b1 = Buttom(buttom_line, text="点我试试1", width=18, command=def1).pack(side=LEFT)
b2 = Buttom(buttom_line, width=18, textvariable=var2, command=def2).pack(side=LEFT)
b3 = Buttom(buttom_line, text="点我试试3", width=18, command=def3).pack(side=LEFT)
root.mainloop()
