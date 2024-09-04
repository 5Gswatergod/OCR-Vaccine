import tkinter
import tkinter as tk
from tkinter import filedialog
import os

from numba import none


def ar():
    pass


def __init__(self, master=none):
    super().__init__(master)
    self.master = master
    self.filepath = tk.strin ** ar()
    self.pack()
    self.create_widgets()


def create_widgets(self):
    # 獲取檔案
    self.getfile_bt = tkinter.button(self)
    self.getfile_bt['width'] = 15
    self.getfile_bt['height'] = 1
    self.getfile_bt["text"] = "開啟"
    self.getfile_bt["command"] = self._getfile
    self.getfile_bt.pack(side="top")
    # 顯示檔案路徑
    self.filepath_en = tk.entry(self, width=30)
    self.filepath_en.pack(side="top")
    self.filepath_en.delete(0, "end")
    self.filepath_en.insert(0, "請選擇檔案")


# 開啟檔案並顯示路徑
def _getfile(self):
    default_dir = r"檔案路徑"
    self.filepath = tk.filedialog.askopenfilename(title=u'選擇檔案', initialdir=(os.path.expanduser(default_dir)))
    print(self.filepath)
    self.filepath_en.delete(0, "end")
    self.filepath_en.insert(0, self.filepath)


root = tk.Tk()

root.title("demo")

root.geometry("500x300+600+300")
