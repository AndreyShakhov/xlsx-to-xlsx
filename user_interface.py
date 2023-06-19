from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class A:

    def __init__(self):
        self.file_name = ""


    def open_file(self):
        file_open = filedialog.askopenfilename(filetypes = (("Text files","*.xlsx"),("all files","*.*")))
        self.file_name = file_open

    def dialog_window(self):
        window = Tk()
        window.title("Сложение столбцов")
        window.geometry('400x250')
        btn = Button(window, text="Открыть файл", command=self.open_file)
        btn.grid(column=1, row=1)
        window.mainloop()


def error_input_file():
    messagebox.showinfo('Ошибка', 'Вы не выбрали файл \nЗапустите программу заново')