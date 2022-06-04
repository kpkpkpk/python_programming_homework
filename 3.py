import os
from tkinter import *
import re


files = []
file = ''


def finish():
    global file, var, regex
    d = os.path.dirname(os.path.abspath(var.get()))
    os.system(f'start chrome {d}\\{var.get()}')


def create_rbs():
    global var, row, column, regex
    for i in range(len(files)):
        f = files[i]
        text = re.sub(regex, '', f.replace('.pdf', ''), 0)
        rb = Radiobutton(master=frame, text=text, value=files[i], variable=var)
        rb.select()
        rb.grid(row=row, column=column)
        row += 1


if __name__ == '__main__':
    regex = r"\d{4}-\d{2}-\d{2}-"
    for x in os.listdir():
        if x.endswith(".pdf"):
            files.append(x)

    row = 0
    column = 0

    window = Tk()
    window.title('Last lab ;)')
    frame = Frame(master=window)
    label = Label(master=frame, text='Which PDF file you want to open?')
    label.grid(row=row, column=0)
    row += 1

    var = StringVar()
    create_rbs()

    btn = Button(master=frame, text='Open', command=finish)
    btn.grid(row=row, column=0)

    window.minsize(250, 100)
    frame.pack()
    window.mainloop()
