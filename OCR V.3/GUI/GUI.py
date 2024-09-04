import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox

import easyocr

file_path = ''


def select():
    global file_path
    file_path = filedialog.askopenfilename()


def reselect():
    global file_path
    file_path = ''


def start():
    reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)
    result = reader.readtext(file_path)

    word = '0'

    for i in result:
        word += str(i[1])
    bnt = word.count('BNT')
    az = word.count('A2)')
    mod = word.count('Moderna')
    guan = word.count('高端')

    messagebox.showinfo("辨識完成", "查看結果")
    messagebox.showinfo('辨識結果', 'BNT施打劑數共' + str(bnt) + '劑' "\n" 'AZ施打劑數共' + str(az) + '劑' "\n" 'Moderna施打劑數' + str(
        mod) + '劑' "\n" '高端施打劑數' + str(guan) + '劑')


top = tk.Tk()

top.geometry("400x100")

top.title('健保卡貼紙辨識')

label = Label(top, text="請選擇檔案所在地", font=('標楷體', 12), fg='black')
label.grid(row=0, column=0)

button = Button(top, text='選擇檔案', width=10, height=1, command=select)
button.grid(row=0, column=2)

label1 = Label(top, text=" ", pady=0.5, padx=0.5)
label1.grid(row=0, column=3)

label4 = Label(top, text=" ", pady=0.5, padx=0.5)
label4.grid(row=0, column=4)

label5 = Label(top, text=" ", pady=0.5, padx=0.5)
label5.grid(row=0, column=5)

button1 = Button(top, text='開始辨識', font=('標楷體', 12), fg='black', command=start)
button1.grid(row=2, column=0)

label2 = Label(top, text=" ", pady=0.5, padx=0.5)
label2.grid(row=2, column=1)

button2 = Button(top, text='重新選擇檔案', width=10, height=1, command=reselect)
button2.grid(row=2, column=2)

label3 = Label(top, text=" ", pady=3, padx=3)
label3.grid(row=2, column=3)

button3 = Button(top, text='退出', width=10, height=1, command=top.quit)
button3.grid(row=2, column=5)

label1 = Label(top, text=" ", pady=8, padx=8)
label1.grid(row=1, column=0)

top.mainloop()
