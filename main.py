#!/usr/bin/env python3

# tkinter - стандартный binding к Tk, который загружает библиотеку Tk в систему.
# ttk - подмодуль tkinter, который реализует Python binding к новым виджетам Tk.
from tkinter import *
from tkinter import ttk

# Путь к изображению с заданием.
IMAGE_FILE = "example.png"


class App:

    def __init__(self, window: Tk):

        # Инициализируем поля для ввода значений, выводы результата и изображения.
        # StringVar - класс, который помогает более эффективно управлять значением виджета.
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.x = StringVar()
        self.y = StringVar()
        self.image = PhotoImage(file=IMAGE_FILE)

        self.init_ui(window)

    def init_ui(self, window: Tk):
        window.title("Python 3 с Tkinter")
        window.resizable(False, False)

        # Создание всех виджетов.
        mainframe = ttk.Frame(window, padding=(8, 8, 8, 8))
        label_a = ttk.Label(mainframe, text="a =")
        label_b = ttk.Label(mainframe, text="b =")
        label_c = ttk.Label(mainframe, text="c =")
        label_x = ttk.Label(mainframe, text="x =")

        # textvariable - это параметр, из которой Label будет брать значение, при
        # любом изменении этого значения.
        label_y = ttk.Label(mainframe, textvariable=self.y)

        label_image = ttk.Label(mainframe, width=144, image=self.image)
        label_image.photo = self.image

        # textvariable - это параметр, указывающий на переменную, которую Tk будет
        # автоматически обновлять при любом изменении Entry.
        entry_a = ttk.Entry(mainframe, textvariable=self.a)
        entry_b = ttk.Entry(mainframe, textvariable=self.b)
        entry_c = ttk.Entry(mainframe, textvariable=self.c)
        entry_x = ttk.Entry(mainframe, textvariable=self.x)

        # command - ссылка на функию, которая будет выполняться при нажатии на кнопку.
        button_solve = ttk.Button(mainframe, text="Решить", command=self.solve)
        button_clear = ttk.Button(mainframe, text="Очистить", command=lambda: self.clear(entry_a))
        button_exit = ttk.Button(mainframe, text="Выход", command=window.destroy)

        # Расположение всех виджетов на экране с помощью сетки.
        mainframe.grid(column=0, row=0)
        label_image.grid(column=0, row=0, rowspan=3)
        label_a.grid(column=1, row=0, sticky=(N, S, E))
        label_b.grid(column=1, row=1, sticky=(N, S, E))
        label_c.grid(column=1, row=2, sticky=(N, S, E))
        label_x.grid(column=1, row=3, sticky=(N, S, E))
        entry_a.grid(column=2, row=0, pady=2)
        entry_b.grid(column=2, row=1, pady=2)
        entry_c.grid(column=2, row=2, pady=2)
        entry_x.grid(column=2, row=3, pady=2)

        # Привязываем событие "Нажатие на Enter" к функциям.
        entry_a.bind("<Return>", (lambda event: entry_b.focus()))
        entry_b.bind("<Return>", (lambda event: entry_c.focus()))
        entry_c.bind("<Return>", (lambda event: entry_x.focus()))
        entry_x.bind("<Return>", (lambda event: self.solve()))

        button_solve.grid(column=0, row=4, pady=8)
        button_clear.grid(column=1, row=4, pady=8)
        button_exit.grid(column=2, row=4, sticky=(N, S, E), pady=8)
        label_y.grid(column=0, row=5, columnspan=3, sticky=(N, S, W))

        # Устанавливаем фокус на первое поле.
        entry_a.focus()

    def solve(self):
        try:
            a = float(self.a.get())
            b = float(self.b.get())
            x = float(self.x.get())
            if x < 4:
                c = float(self.c.get())
                y = ((x * x + a * a) * c) / (2 * b)
            else:
                y = (x * x * x) * (a - b)
            self.y.set(f"y = {y:.2f}")
        except ValueError:
            self.y.set("Неверные входные данные!")
        except ArithmeticError:
            self.y.set("Нет решения!")
        except Exception:
            self.y.set("Ошибка!")

    def clear(self, entry: ttk.Entry):
        self.a.set("")
        self.b.set("")
        self.c.set("")
        self.x.set("")
        self.y.set("")
        entry.focus()


def center(window: Tk):
    """
    Centers a Tkinter window
    :param window: the main window or Toplevel window to center
    """
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()


if __name__ == '__main__':
    root = Tk()
    root.attributes('-alpha', 0)

    App(root)
    center(root)

    root.attributes('-alpha', 1)
    root.mainloop()
