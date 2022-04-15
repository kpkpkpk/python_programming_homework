import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta, datetime
import requests
import json
import math


def sale(companies, packages):
    prices = []
    price = 0
    for package in packages:
        for i in package:
            for j in companies:
                if j[0] == i[0]: price += i[1] * j[-1][-1]
        prices.append(price)
        price = 0

    return prices


# Евгений
def Evgeniy(list_of_company, sale):
    sum = 0
    res = []
    for i in list_of_company: sum += i[2] * i[-1][-1]
    for i in list_of_company: res.append([i[0], (i[2] * i[-1][-1] / sum) * sale // i[-1][-1]])
    return res


# Анатолий
def anatoliy_task(list_of_company, s):
    pair = []

    for i in range(len(list_of_company) // 2, len(list_of_company)):
        for j in range(0, len(list_of_company) // 2):
            if ((list_of_company[j][-1][0] < list_of_company[j][-1][-1])
                    and (list_of_company[i][-1][0] < list_of_company[i][-1][-1])
                    and i != j):

                k = math.fabs(correlation(list_of_company[i][-1], list_of_company[j][-1]))
                if len(pair) < 3:
                    pair.append([k, i, j])
                else:
                    max = 0
                    for index in range(len(pair)):
                        if pair[index][0] > pair[max][0]: max = index
                    pair[max] = [k, i, j]

    packs = []
    s /= 6
    for i in pair:
        packs.append([list_of_company[i[1]][0], (s) // list_of_company[i[1]][-1][-1]])
        packs.append([list_of_company[i[2]][0], (s) // list_of_company[i[2]][-1][-1]])
    return packs


# Андрей
def andrei_task(list_of_company, s):
    pair = []

    for i in range(len(list_of_company) // 2, len(list_of_company)):
        for j in range(0, len(list_of_company) // 2):
            if ((list_of_company[j][-1][0] < list_of_company[j][-1][-1])
                    and (list_of_company[i][-1][0] < list_of_company[i][-1][-1])
                    and i != j):

                k = math.fabs(correlation(list_of_company[i][-1], list_of_company[j][-1]))
                if len(pair) < 3:
                    pair.append([k, i, j])
                else:
                    min = 0
                    for index in range(len(pair)):
                        if pair[index][0] < pair[min][0]: min = index
                    pair[min] = [k, i, j]

    packs = []
    for i in pair:
        packs.append([list_of_company[i[1]][0], (s / 6) // list_of_company[i[1]][-1][-1]])
        packs.append([list_of_company[i[2]][0], (s / 6) // list_of_company[i[2]][-1][-1]])
    return packs


# корреляция
def correlation(list_1, list_2):
    average_one = sum(list_1) / len(list_1)
    average_two = sum(list_2) / len(list_2)
    disp_1 = 0
    disp_2 = 0
    disp_3 = 0

    for i in range(len(list_1)):
        disp_1 += math.pow(list_1[i] - average_one, 2)
        disp_2 += math.pow(list_2[i] - average_two, 2)
        disp_3 += (list_2[i] - average_two) * (list_1[i] - average_one)

    return disp_3 / (math.sqrt(disp_1 * disp_2))


# получаем сам список компаний
def making_list(requests_list, id):
    list_of_companies = []
    data = requests.get(requests_list[0]).json()
    for i in data["securities"]["data"]:
        if id.count(i[0]) > 0:
            list_of_companies.append(i)
    return list_of_companies


# собираем данные по списку компаний за год
def start_data(list_of_companies, start_date, requests_list, delta):
    result = []
    for i in list_of_companies:
        if start_data_factory_info(i, start_date, requests_list, delta): result.append(i)
    return result


# собираем данные по конкретной компании за год
def start_data_factory_info(company, start_date, requests_list, delta):
    l = start_date.split('-')
    new = str(datetime(int(l[0]), int(l[1]), int(l[2])) + timedelta(days=delta))
    url = (requests_list[1][0:-1] + company[0] +
           requests_list[2][0:-1] + "from=" +
           start_date + "&till=" + new)

    data = requests.get(url)
    data = data.json()
    company.append([])

    for j in data['history']["data"]:
        if j[-1] != None: company[-1].append(j[-1])
    if len(company[-1]) < 100: return False
    return True


# период трейдинга
def trade_game(start):
    res = [[[], []], [[], []], [[], []]]
    list = start_data(making_list(api_moex_list, ID), start, api_moex_list, 365)
    Ev = 10000000
    And = 10000000
    Ant = 10000000
    start = str(datetime(int(start.split('-')[0]), int(start.split('-')[1]), int(start.split('-')[2])) + timedelta(
        days=365)).split()[0]
    for i in range(5):
        res[0][0].append(start)
        res[1][0].append(start)
        res[2][0].append(start)
        res[0][1].append(Ev)
        res[1][1].append(And)
        res[2][1].append(Ant)
        new = start_data(making_list(api_moex_list, ID), start, api_moex_list, 93)
        Ev, And, Ant = sale(new, [Evgeniy(list, Ev), andrei_task(list, And), anatoliy_task(list, Ant)])
        start = str(datetime(int(start.split('-')[0]), int(start.split('-')[1]), int(start.split('-')[2])) + timedelta(
            days=93)).split()[0]
        list = new[:]
    trades_results(res)


# обработка результатов и постройка графиков
def trades_results(data):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(data[0][0], data[0][1], label='Evgeniy')
    ax.plot(data[1][0], data[1][1], label='Andrey')
    ax.plot(data[2][0], data[2][1], label='Anatoliy')
    ax.set_xlabel('x label')
    plt.show()


# cтарт
api_moex_list = open("requesr.txt", 'r')
api_moex_list = api_moex_list.readlines()
ID = ["GAZP", "TATN", "SBER", "VTBR", "ALRS",
      "AFLT", "HYDR", "MOEX", "NLMK", "CHMF",
      "DSKY", "RUSP", "YNDX", "AFKS", "LSRG",
      "LSNG", "LKOH", "MTSS", "NVTK", "PIKK"]

trade_game("2018-05-01")
