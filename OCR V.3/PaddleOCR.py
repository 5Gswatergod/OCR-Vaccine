import tkinter as tk
from tkinter import *
import easyocr
from tkinter import messagebox, filedialog


def back():
    entry.delete(0, END)


def start():
    img_path = filedialog.askopenfilename()
    reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)
    result = reader.readtext(img_path)

    word = '0'

    for i in result:
        word += str(i[1])
    bnt = word.count('BNT')
    az = word.count('A2)')
    mod = word.count('Moderna')
    guan = word.count('高端')
    messagebox.showinfo('資訊:', message=str(bnt))
    messagebox.showinfo('資訊:', message=str(az))
    messagebox.showinfo('資訊:', message=str(mod))
    messagebox.showinfo('資訊:', message=str(guan))


top = tk.Tk()

top.geometry("700x100+500+400")

top.title('健保卡貼紙辨識')

label = Label(top, text="輸入檔案位置: ", font=('標楷體', 12), fg='black')
label.grid(row=0, column=0)

entry = Entry(top, width=50)
entry.grid(row=0, column=1)

button = Button(top, text="辨識", width=10, height=1, command=start)
button.grid(row=2, column=0)

button1 = Button(top, text="清空", width=10, height=1, command=back)
button1.grid(row=2, column=1)

top.mainloop()
