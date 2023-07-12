import os.path
import random
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from Database_process import DB
from PIL import Image,ImageTk
from tkinter import filedialog

#---

def get_image(filename, width = 640, height = 300):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

#---

root = tk.Tk()
root.title("Cirno the brilliant learning English")
root.geometry("640x300")
root.resizable(False,False)

path = tk.StringVar()
str_words = tk.StringVar()
str_trans = tk.StringVar()

Canvas_root = tk.Canvas(root,bg="blue",height=300,width=640)
background = get_image(r"photos/background.png")
Canvas_root.create_image(320,150,image = background)
Canvas_root.pack()

img_transparent = Image.new("RGBA",(640,300),(0,0,0,0))
img_transparent = ImageTk.PhotoImage(img_transparent)
l1 = tk.Label(root,font=("黑体", 20),text="👉"+"【英语学习小程序】"+"👈")
l1.place(x = 20,y = 10,width=200 ,height=40)
image_9 = get_image("photos/9.png",40,40)
l2 = tk.Label(root, text="", font=("黑体", 15),image=image_9)
l2.place(x = 230,y = 10,width=40 ,height=40)

# l3 = tk.Label(root, text="", font=("黑体", 15))
# l3.place(x = 350,y = 170,width=135 ,height=110)

ask_text_word = tk.Entry(root, text="", font=("黑体", 17),textvariable=str_words)  # 创建文本框
ask_text_word.place(x = 20,y = 70,width=290 ,height=60)
ask_text_trans = tk.Entry(root, text="", font=("黑体", 17),textvariable=str_trans)  # 创建文本框
ask_text_trans.place(x = 330,y = 70,width=290 ,height=60)

#---

db = DB()

#---

def bt_1():# 展示英文
    str_words.set(db.word[db.random_number])
    return 0
def bt_2():# 展示中文
    str_trans.set(db.trans[db.random_number])
    return 0
def bt_3():# 抽取英文
    if db.doc_name_path == None:
        str_words.set("需要导入文件")
        str_trans.set("需要导入文件")
        return 0
    words,trans = db.random_pick()
    str_words.set(words)
    return 0
def bt_4():# 抽取中文
    if db.doc_name_path == None:
        str_trans.set("需要导入文件")
        str_words.set("需要导入文件")
        return 0
    words,trans = db.random_pick()
    str_trans.set(trans)
    return 0
def bt_5():
    # 选择文件path_接收文件地址
    path_ = tk.filedialog.askopenfilename()
    db.set_path(path_)
    db.init_words()
    return 0
def bt_6():# 写入文件
    if db.doc_name_path == None:
        str_trans.set("需要导入文件")
        str_words.set("需要导入文件")
        return 0
    new_trans = str_trans.get()
    new_words = str_words.get()
    db.trans.append(new_trans)
    db.word.append(new_words)
    db.write_in(new_words,new_trans)
    return 0
def bt_7():#清空
    str_trans.set('')
    str_words.set('')
    return 0
# 一、窗口上敲键盘触发事件（以Enter键为例）
# root.bind('<Return>', bt)
# root.bind('<Shift_L>', callback2)

# 二、点击窗口按钮触发事件（以鼠标左键单击为例）

button = ttk.Button(root, text="选择文件", bootstyle=(PRIMARY, OUTLINE) ,command = bt_5)
button.place(x = 520,y = 10, width=100 ,height= 40)

button2 = ttk.Button(root, text="抽取中文", bootstyle=(INFO, OUTLINE) ,command = bt_4)
button2.place(x = 20,y = 170,width=135 ,height= 40)

button3 = ttk.Button(root, text="展示英文", bootstyle=(INFO, OUTLINE) ,command = bt_1)
button3.place(x = 175,y = 170,width=135 ,height= 40)

button4 = ttk.Button(root, text="抽取英文", bootstyle=(INFO, OUTLINE) ,command = bt_3)
button4.place(x = 20,y = 240,width=135 ,height= 40)

button5 = ttk.Button(root, text="展示中文", bootstyle=(INFO, OUTLINE) ,command = bt_2)
button5.place(x = 175,y = 240,width=135 ,height= 40)

button6 = ttk.Button(root, text="ENTER", bootstyle=SUCCESS ,command = bt_6)
button6.place(x = 505,y = 170, width=115 ,height= 60)

button7 = ttk.Button(root, text="EMPTY", bootstyle=WARNING ,command = bt_7)
button7.place(x = 350,y = 170, width=135 ,height= 60)

root.mainloop()
