import yfinance as yf
import matplotlib.pyplot as plt
from pandas import DataFrame
from tkinter import *
from tkinter.ttk import Combobox
import re
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
import pandas as pd
import math

tikers = ["Введите свой тикер или выберите из списка", "YNDX.ME", "ALRS", "POLY", "YNDX", "MSFT", "AAPL", "GAZP.ME",
          "SBER.me", "SNGS.me", "RT-KM.me", "PICK.me",
          "DSKY.me", "ONE", "DFK", "DRI", "TSLA", "TTLK.ME", "LSRG.ME", "MSTT.ME" ]

type_of_recovery = ["Винзорирование", "Линейная аппроксимация", "Ничего не выбрано"]

smothing = ["Взвешенный метод скользящего среднего", "метод скользящего среднего со скользящим окном наблюдения",
            "ничего не выбрано"]


def dowload_data(start, finish, company):
    data = yf.download(company, start, finish)
    data = data["Adj Close"].to_dict()
    data2 = {"year": [], "action": []}
    for time in data.keys():
        data2["year"].append(str(time)[:10])
        data2["action"].append(float(data[time]))
    return data2


def close():
    global conv
    if conv:
        conv.get_tk_widget().destroy()


def reformat_data_file(data):
    start = data["year"][0].split("-")
    finish = data["year"][-1].split("-")
    start_date = dt.datetime(int(start[0]), int(start[1]), int(start[2]))
    finish_date = dt.datetime(int(finish[0]), int(finish[1]), int(finish[2]))
    res = pd.date_range(start_date, finish_date).strftime('%Y-%m-%d').tolist()
    dates = []
    actions = []
    count = 0
    for i in range(len(res)):
        if res[i] not in data["year"]:
            dates.append(res[i])
            actions.append(None)
        else:
            dates.append(res[i])
            actions.append(data["action"][data["year"].index(res[i])])
        count += 1
    data2 = {"year": dates, "action": actions}
    return data2


def recovering_1(data):
    # vinzor
    array = data["action"]
    j = {}
    for index in range(len(array)):
        if array[index] is None:
            dop_index = 0
            while array[index] is None:
                if index - dop_index > 0 and array[index - dop_index] is not None:
                    array[index] = array[index - dop_index]
                    j[index] = array[index - dop_index]
                if index + dop_index < len(array) and array[index + dop_index] is not None:
                    array[index] = array[index + dop_index]
                    j[index] = array[index + dop_index]
                dop_index += 1
    data["action"] = array
    return data


def line(x_1, y_1, x_2, y_2):
    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_2 - k * x_2
    return [k, b]


def recovering_2(date):
    arr_2 = date["action"]
    for i in range(len(arr_2)):
        if arr_2[i] is None:
            if i == 0:
                key = i + 1
                if arr_2[key] == None:
                    while arr_2[key] is None:
                        key += 1
                key_2 = key + 1
                if arr_2[key_2] is None:
                    while arr_2[key_2] is None:
                        key_2 += 1
            elif i == len(arr_2):
                key = i - 1
                if arr_2[key] is None:
                    while arr_2[key] is None:
                        key -= 1
                key_2 = key - 1
                if arr_2[key_2] is None:
                    while arr_2[key_2] is None:
                        key_2 -= 1
            else:
                key = i - 1
                if arr_2[key] is None:
                    while arr_2[key] is None:
                        key -= 1
                key_2 = i + 1
                if arr_2[key_2] is None:
                    while arr_2[key_2] is None:
                        key_2 += 1
            a, b = line(key, arr_2[key], key_2, arr_2[key_2])
            arr_2[i] = a * i + b
            date["action"] = arr_2
    return date


def smoothing_1(data, k):
    res = []
    m = []
    arr = data["action"]
    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i])
        else:
            window = arr[:i + 1]
            f = False
            while math.fabs((arr[i] - (sum(window) / len(window))) / arr[i]) > k:
                f = True
                if len(window) > 1:
                    window.pop(0)
                else:
                    break
            if f:
                m.append(len(window))
            res.append(sum(window) / len(window))
    data["action"] = res
    return data


def smoothing_2(data, k, n):
    arr = data["action"]
    for i in range(0, len(arr), n):
        window = []
        index = []
        for j in range(n):
            window.append(arr[i + j])
            index.append(j + 1)
        for j in range(n):
            while math.fabs((arr[i + j] - (sum(window) / sum(index))) / arr[i + j]) > k:
                if len(window) > 1:
                    window.pop(0)
                else:
                    break
            arr[i + j] = sum(window) / sum(index)
    data["action"] = arr
    return data


def clicked():
    global if_graf
    global conv
    figure2 = plt.Figure(figsize=(10, 8), dpi=120)
    ax2 = figure2.add_subplot(111)
    if if_graf:
        conv.get_tk_widget().destroy()
        if_graf = False
    company = combo.get()
    n = nnn.get()
    k = kkk.get()
    if n != "":
        n = float(n)
    if k != "":
        k = int(k)
    start_time = time_start.get()
    finish_time = time_finish.get()
    smoth = combo2.get()
    recover = combo1.get()
    if re.match(r"\d{4}-\d{2}-\d{2}", start_time) or re.match(r"\d{4}-\d{2}-\d{2}", finish_time):
        lbl.configure(text="")
        lbl4.configure(text="")
        data = dowload_data(start_time, finish_time, company)
        data = reformat_data_file(data)
        if recover == type_of_recovery[0]:
            data = recovering_1(data)
        elif recover == type_of_recovery[1]:
            data = recovering_2(data)
        if smoth != smothing[2]:
            if 0 <= n <= 1:
                if smoth == smothing[0]:
                    data = smoothing_2(data, k, n)
                else:
                    data = smoothing_1(data, n)
            else:
                lbl4.configure(text="коэфф должен быть в промежутке [0,1]")
        conv = FigureCanvasTkAgg(figure2, str4)
        conv.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = DataFrame(data, columns=['year', 'action'])
        df2 = df2[['year', 'action']].groupby('year').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', fontsize=10)
        ax2.set_title('Graph')
        if_graf = True
    else:
        lbl.configure(text="введен неверный формат даты")
        conv.get_tk_widget().destroy()
        if_graf = False


# Build UI
file = open("actions", "w")

file.close()
window = Tk()
conv = None
if_graf = False

str1 = Frame(window)
str2 = Frame(window)
str3 = Frame(window)
str4 = Frame(window)

str1.pack()
str2.pack()
str3.pack()
str4.pack()
window.title("")
canvas1 = None
window.geometry('1000x700')
lbl = Label(str1, text="", fg="red")
lbl.grid(column=1, row=5)
start = Label(str1, text="введите дату в формате: 'ГГГГ-ММ-ДД' ")
start.grid(column=0, row=3)
time_start = Entry(str1, width=20)
time_start.grid(column=1, row=3)
time_finish = Entry(str1, width=20)
time_finish.grid(column=2, row=3)
btn = Button(master=str1, text="Build", command=clicked)
btn.grid(column=2, row=5)
combo = Combobox(str1)
combo['values'] = tikers
combo.current(1)
combo.grid(column=1, row=0)
combo1 = Combobox(str1)
combo1['values'] = type_of_recovery
combo1.current(1)
combo1.grid(column=1, row=1)
combo2 = Combobox(str1)
combo2['values'] = smothing
combo2.current(1)
combo2.grid(column=1, row=2)
lbl1 = Label(str1, text="Выберите способ восстановления данных")
lbl1.grid(column=0, row=1)
lbl2 = Label(str1, text="Выберите способ сглаживания данных")
lbl2.grid(column=0, row=2)
lbl4 = Label(str1, text="", fg="red")
lbl4.grid(column=0, row=5)
tiker = Label(str1, text="укажите тикер компании")
tiker.grid(column=0, row=0)
nnn = Entry(str1, width=20)
nnn.grid(column=1, row=4)
kkk = Entry(str1, width=20)
kkk.grid(column=1, row=5)
lbl6 = Label(str1, text="Введите период сглаживания(для взвешенного скользящего среднего)")
lbl6.grid(column=0, row=5)
lbl3 = Label(str1, text="Введите коэффицент отклонения сглаженного процесса от реального")
lbl3.grid(column=0, row=4)
window.mainloop()
