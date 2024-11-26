from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import  messagebox as mb

def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath,'rb') as f:
                files = {'file':f}
                response=requests.post('https://file.io/',files=files)
                response.raise_for_status()
                data = response.json()
                link= data['link']
                entry.delete(0,END)
                entry.insert(0,link)
    except KeyError:
        mb.showerror('Ошибка','Ссылка не найдена в ответе')
    except Exception as e:
        mb.showerror('Ошибка',f'Ошибка {e}')

window = Tk()
window.title('Отправка файла в облако')
window.geometry('300x100')

button = ttk.Button(text='Загрузить файл',
                    command = upload)
button.pack(padx=10,pady=10)
entry=ttk.Entry()
entry.pack()

window.mainloop()