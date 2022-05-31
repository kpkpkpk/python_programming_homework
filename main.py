from tkinter import *
from tkinter import messagebox
import gspread
import datetime


def alert(title, message, type_of_alert='info'):
    show_method = getattr(messagebox, 'show{}'.format(type_of_alert))
    show_method(title, message)


def finish(event):
    import pandas as pd
    import matplotlib.pyplot as plt
    global e_time, e_speed, e_name
    flag = False
    try:
        time_in_minutes = str(int(e_time.get()))
        speed = str(int(e_speed.get()))

        cell_c1 = gsheet.acell('B1')
        if str(cell_c1.value) != str(datetime.date.today()):
            gsheet.update('B1', str(datetime.date.today()))
        gsheet.update('B3', time_in_minutes)
        gsheet.update('B4', speed)
        alert('Success!', 'Data successfully updated!')
        flag = True
    except ValueError:
        alert('Error!', 'You should input 2 integers', 'error')
    if flag:
        name = str(datetime.date.today()) + '-' + e_name.get()
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        df = pd.DataFrame(gsheet.get_all_records())
        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        fig.tight_layout()
        plt.savefig(f'{name}.pdf')
        alert('Success!', 'Data successfully saved!')


gc = gspread.oauth()
gsheet = gc.open("MySheet").get_worksheet(0)

window = Tk()
window.title('Last lab ;)')
frame = Frame(master=window)
label_time = Label(master=frame, text='Time in minutes:')
label_time.grid(row=0, column=0)
e_time = Entry(master=frame)
e_time.grid(row=0, column=1)
label_speed = Label(master=frame, text='Speed in meters per minutes:')
label_speed.grid(row=1, column=0)
e_speed = Entry(master=frame)
e_speed.grid(row=1, column=1)
label_name = Label(master=frame, text='Name of PDF file:')
label_name.grid(row=2, column=0)
e_name = Entry(master=frame)
e_name.grid(row=2, column=1)
btn_confirm = Button(master=frame, text='Confirm')
btn_confirm.grid(row=3, column=0)
btn_confirm.bind('<Button-1>', finish)

frame.pack()
window.mainloop()
