from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk

def upload():
    pass

window = Tk()
window.title('Отправка файла в облако')
window.geometry('300x100')

button = ttk.Button(text='Загрузить файл',
                    command = upload)
button.pack(padx=10,pady=10)
entry=ttk.Entry()
entry.pack()

window.mainloop()