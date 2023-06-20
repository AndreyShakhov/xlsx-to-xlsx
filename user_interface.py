from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#from tkinter import checkbutton


class Interface:
    def __init__(self):
        self.file_name = ""
        self.checkvar1 = ''

    def open_file(self):
        file_open = filedialog.askopenfilename(filetypes=(("Text files", "*.xlsx"), ("all files", "*.*")))
        self.file_name = file_open

    #def quit(self):
    #    self.window.destroy()

    def dialog_window(self):
        window = Tk()
        #window.title("Сложение столбцов")
        #window.geometry('600x300')
        btn = Button(text="Открыть файл", command=self.open_file)
        btn.pack(side=RIGHT)
        btn_close = Button(text="Сформировать файл", command=window.quit)
        btn_close.pack(side=LEFT)
        window.mainloop()


def error_input_file():
    messagebox.showinfo('Ошибка', 'Вы не выбрали файл \nЗапустите программу заново')