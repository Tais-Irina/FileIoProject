import os
import json
from tkinter import *
import requests
import pyperclip #для сохранения в буфер обмена
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
                #возможность копировать в буфер обмена ссылку
                pyperclip.copy(link)
                entry.delete(0,END)
                entry.insert(0,link)
                save_history(filepath,link)
                mb.showinfo("info",'ссылка успешно скопирована в буфер обмена')
    except KeyError:
        mb.showerror('Ошибка','Ссылка не найдена в ответе')
    except Exception as e:
        mb.showerror('Ошибка',f'Ошибка {e}')

def save_history(filepath,link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'file_path':os.path.basename(filepath),
                    'donload_link':link})
    with open(history_file, 'w') as f:
        json.dump(history, f,indent=4)

history_file = "upload_history.json"

window = Tk()
window.title('Отправка файла в облако')
window.geometry('300x100')

button = ttk.Button(text='Загрузить файл',
                    command = upload)
button.pack(padx=10,pady=10)
entry=ttk.Entry()
entry.pack()

window.mainloop()